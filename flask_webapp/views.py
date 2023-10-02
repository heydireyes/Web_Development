from flask import Blueprint, render_template
from bs4 import BeautifulSoup
import requests
from datetime import datetime

views = Blueprint("views", __name__)

@views.route("/")
def home(): 
    url = "https://news.google.com/rss/search?q=triplemint+real+estate+llc&hl=en-US&gl=US&ceid=US:en"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "xml")

  

    news_data = []

    for item in doc.find_all("item"):
                title = item.find("title")
                pub_date_string = item.find("pubDate").string
                pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                formatted_date=pub_date.strftime("%B %d, %Y")
                link = item.find("link").text
          
            
                print("Title:", title.string)
                print("Posted on:", formatted_date)
                print("Link:", link)
                print()

                data = {
                        "Title": title.string,
                        "Date": formatted_date,
                        "Link": link
                        }
                news_data.append(data)

    sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
    return render_template("home.html", data=sorted_news_data)

        
