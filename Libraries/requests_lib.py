import requests

url = "https://b2484492.smushcdn.com/2484492/wp-content/uploads/2025/03/pedro-lastra-Nyvq2juw4_o-unsplash-2560x1574.jpg?lossy=1&strip=1&webp=1"
res = requests.get(url)

if res.ok:
    with open("test.jpg", "wb") as f:
        f.write(res.content)
    print("Saved successfully")
    print(res.headers.get("Content-Type"))
    print(len(res.content))
else:
    print("Failed:", res.status_code)
    print(res.headers.get("Content-Type"))

print("=======          =======")

parameters = {'page': 2, 'count': 25}
key = requests.get('https://httpbin.org/get', parameters)
print(key.text)

print("=======          =======")

print("Exact URL: ", key.url)

print("=======          =======")

params2 = {"Name": 'Mohamed', "Age": 22}
key = requests.post('https://httpbin.org/post', data=params2)
print(key.text)

print("=======          =======")

key_dict = key.json()
print(key_dict["form"])