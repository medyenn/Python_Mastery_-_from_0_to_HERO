import requests, sys, os, dotenv


def main():
    # You better create a .env file in which you put a variable that holds you api key
    # Then the dotenv.load_dotenv() method is going to inject the variable
    # and its value in the environments vars
    # and you can get it form your environment safely using os.getenv()
    # without exposing it to the public
    # Just don't forget to put the .env files in the .gitignore
    dotenv.load_dotenv()

    if len(sys.argv) != 2:
        sys.exit("Missing Command-line argument")

    try:
        amount = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")

    else:
        kapi = os.getenv('API_KEY', None)
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={kapi}"

        try:
            req = requests.get(url)
            req.raise_for_status()

        except requests.RequestException:
            sys.exit("Request failed")

        req_dict = req.json()
        price = float((req_dict.get("data")).get("priceUsd"))
        total = amount * price
        print(f"{total:,.4f}")


if __name__ == "__main__":
    main()