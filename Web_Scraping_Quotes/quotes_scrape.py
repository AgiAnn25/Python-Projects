import requests
from bs4 import BeautifulSoup
import csv

baseurl = "https://quotes.toscrape.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

file = open("quotes.csv", "w", newline="", encoding="utf-8")

writer = csv.writer(file)

writer.writerow(["Quote", "Author", "Author Link", "Tags"])

page = 1

while True:

    url = f"https://quotes.toscrape.com/page/{page}/"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    if len(quotes) == 0:
        break

    for quote in quotes:

        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        author_link = quote.find("a")["href"]
        full_link = baseurl + author_link

        tags = ", ".join([tag.text for tag in quote.find_all("a", class_="tag")])

        writer.writerow([text, author, full_link, tags])

    page += 1

file.close()

print("quotes.csv file created successfully")