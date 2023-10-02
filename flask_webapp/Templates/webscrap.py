from bs4 import BeautifulSoup
import requests
import csv

url = "https://news.google.com/rss/search?q=triplemint+real+estate+llc&hl=en-US&gl=US&ceid=US:en"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

if result.status_code == 200:
    doc = BeautifulSoup(result.text, "xml")



    with open("triplemint_news.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Date", "Link"])

        for item in doc.find_all("item"):
            title = item.find("title")
            pub_date = item.find("pubDate")
            link = item.find("link").text
        
            print("Title:", title.string)
            print("Publish Date:", pub_date.string)
            print("Link:", link)
            print()

            writer.writerow([title.string, pub_date.string, link])






