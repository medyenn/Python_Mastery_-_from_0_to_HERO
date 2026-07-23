# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def planespotters():
    airline = input('Enter the name of the airline: ')
    slug = "-".join(airline.title().split())
    url = f"https://www.planespotters.net/airline/{slug}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(url)

        input("Solve the verification if it appears, then press Enter...")

        html = page.content()

        with open("airline.html", "w", encoding="utf-8") as f:
            f.write(html)

        browser.close()
    # info_rows = info_table.find_all("tr")
    # info_data = []

    # for row in info_rows:
    #     cols = row.find_all(["th", "td"])

    #     cols = [c.get_text(strip=True) for c in cols]

    #     info_data.append(cols)

    # stats_rows = stats_table.find_all("tr")
    # stats_data = []

    # for row in stats_rows:
    #     cols = row.find_all(["th", "td"])

    #     cols = [c.get_text(strip=True) for c in cols]

    #     stats_data.append(cols)

    # df = pd.DataFrame(info_data)
    # df = pd.DataFrame(stats_data)
    # print(info_data)
    # print('\n\n\n' + stats_data)


planespotters()
