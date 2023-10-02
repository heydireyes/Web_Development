from flask import Blueprint, render_template
from bs4 import BeautifulSoup
import requests
from datetime import datetime


auth = Blueprint("auth", __name__)

@auth.route('/sense')
def sense(): 
        url = "https://news.google.com/rss/search?q=%22Sense+Finance%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                doc = BeautifulSoup(result.text, "xml")

                news_data = []

                for item in doc.find_all("item"):
                        title = item.find("title")
                        pub_date_string = item.find("pubDate").string
                        pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date=pub_date.strftime("%B %d, %Y")
                        link = item.find("link").text
                        source= item.find("source").string
                
                        print("Title:", title.string)
                        print("Posted on:", formatted_date)
                        print("Link:", link)
                        print()
               
                        if "City of Mentor, Ohio" not in source and pub_date.year >= 2021:    
                                data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                                }
                                news_data.append(data)
                        
                        

                sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                return render_template("sense.html", data=sorted_news_data)

@auth.route('/prenav')
def prenav(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("prenav.html", data=sorted_news_data)
        

@auth.route('/brewbotz')
def brewbotz(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("brewbotz.html", data=sorted_news_data)

@auth.route('/tablelist')
def tablelist(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("tablelist.html", data=sorted_news_data)

@auth.route('/hint')
def hint(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("hint.html", data=sorted_news_data)

@auth.route('/naytev')
def naytev(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("naytev.html", data=sorted_news_data)

@auth.route('/mdinsider')
def mdinsider(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("mdinsider.html", data=sorted_news_data)

@auth.route('/wevorce')
def wevorce(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("wevorce.html", data=sorted_news_data)

@auth.route('/mudwtr')
def mudwtr(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("mudwtr.html", data=sorted_news_data)

@auth.route('/locusbiosciences')
def locusbiosciences(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("locusbiosciences.html", data=sorted_news_data)         

@auth.route('/velocitymobile')
def velocitymobile(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("velocitymobile.html", data=sorted_news_data)
        
@auth.route('/loomai')
def loomai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("loomai.html", data=sorted_news_data)
        
@auth.route('/lively')
def lively(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("lively.html", data=sorted_news_data)

@auth.route('/triller')
def triller(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("triller.html", data=sorted_news_data)
        
@auth.route('/orphidia')
def orphidia(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("orphidia.html", data=sorted_news_data)

@auth.route('/an2therapeutics')
def an2therapeutics(): 
        url = "https://news.google.com/rss/search?q=%22an2+therapeutics%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                doc = BeautifulSoup(result.text, "xml")

                news_data = []

                for item in doc.find_all("item"):
                        title = item.find("title")
                        pub_date_string = item.find("pubDate").string
                        pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date=pub_date.strftime("%B %d, %Y")
                        link = item.find("link").text
                        source= item.find("source").string
                
                        print("Title:", title.string)
                        print("Posted on:", formatted_date)
                        print("Link:", link)
                        print()
               
                        if "Simply Wall St" not in source:    
                                data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                                }
                                news_data.append(data)
                        
                        

                sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                return render_template("an2therapeutics.html", data=sorted_news_data)
        
@auth.route('/chai')
def chai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("chai.html", data=sorted_news_data)
        
@auth.route('/seated')
def seated(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("seated.html", data=sorted_news_data)
        
@auth.route('/phoenixmoleculardesigns')
def phoenixmoleculardesigns(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("phoenixmoleculardesigns.html", data=sorted_news_data)
        
@auth.route('/humanlongevity')
def humanlongevity(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("humanlongevity.html", data=sorted_news_data)
        
@auth.route('/ionpath')
def ionpath(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ionpath.html", data=sorted_news_data)
        
@auth.route('/umbra')
def umbra(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("umbra.html", data=sorted_news_data)
        
@auth.route('/akadeumlifesciences')
def akadeumlifesciences(): 
        url = "https://news.google.com/rss/search?q=akadeum+life+sciences&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                doc = BeautifulSoup(result.text, "xml")

                news_data = []
                count= 0

                for item in doc.find_all("item"):
                        title = item.find("title")
                        pub_date_string = item.find("pubDate").string
                        pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date=pub_date.strftime("%B %d, %Y")
                        link = item.find("link").text
                        source= item.find("source").string
                        
                
                        print("Title:", title.string)
                        print("Posted on:", formatted_date)
                        print("Link:", link)
                        print()
               
                        if "DBusiness" not in source:    
                                data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                                }
                                news_data.append(data)
                                count += 1
                        
                if count == 0:
                        print("No news articles published at this time.")

                sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                return render_template("akadeumlifesciences.html", data=sorted_news_data)
        
@auth.route('/mycroftai')
def mycroftai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("mycroftai.html", data=sorted_news_data)
        
@auth.route('/molekule')
def molekule(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("molekule.html", data=sorted_news_data)
        

@auth.route('/pipefy')
def pipefy(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("pipefy.html", data=sorted_news_data)

@auth.route('/zeotap')
def zeotap(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("zeotap.html", data=sorted_news_data)
        
@auth.route('/wavebl')
def wavebl(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("wavebl.html", data=sorted_news_data)
        
@auth.route('/adarzabiosystems')
def adarzabiosystems(): 
        url = "https://news.google.com/rss/search?q=adarza+biosystems&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("adarzabiosystems.html", data=sorted_news_data)


@auth.route('/anymod')
def anymod(): 
        url = "https://news.google.com/rss/search?q=%22anymod%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("anymod.html", data=sorted_news_data)
        
@auth.route('/aanikabiosciences')
def aanikabiosciences(): 
        url = "https://news.google.com/rss/search?q=aanika+biosciences&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("aanikabiosciences.html", data=sorted_news_data)
        
@auth.route('/aavrani')
def aavrani(): 
        url = "https://news.google.com/rss/search?q=aavrani&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("aavrani.html", data=sorted_news_data)
        

@auth.route('/acquicent')
def acquicent(): 
        url = "https://news.google.com/rss/search?q=acquicent&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("acquicent.html", data=sorted_news_data)
        

@auth.route('/advancedmicrobubbles')
def advancedmicrobubbles(): 
        url = "https://news.google.com/rss/search?q=%22advanced+microbubbles%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                doc = BeautifulSoup(result.text, "xml")

                news_data = []
                count= 0

                for item in doc.find_all("item"):
                        title = item.find("title")
                        pub_date_string = item.find("pubDate").string
                        pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date=pub_date.strftime("%B %d, %Y")
                        link = item.find("link").text
                        source= item.find("source").string
                        
                
                        print("Title:", title.string)
                        print("Posted on:", formatted_date)
                        print("Link:", link)
                        print()
               
                        if "ASCO Journals" not in source and "Cancer Discovery" not in source:    
                                data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                                }
                                news_data.append(data)
                                count += 1
                        
                if count == 0:
                        print("No news articles published at this time.")

                sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                return render_template("advancedmicrobubbles.html", data=sorted_news_data)        

def aetherbiomachines2(): 
    url = "https://news.google.com/rss/search?q=aether&hl=en-US&gl=US&ceid=US:en"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    if result.status_code == 200:
        doc = BeautifulSoup(result.text, "xml")

        news_data = []
        article_count = 0  

        for item in doc.find_all("item"):
            if article_count >= 3:
                break  

            title = item.find("title")
            pub_date_string = item.find("pubDate").string
            pub_date = datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
            formatted_date = pub_date.strftime("%B %d, %Y")
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
            article_count += 1

        return news_data

@auth.route('/aetherbiomachines')
def aetherbiomachines(): 
    url = "https://news.google.com/rss/search?q=%22aether+bio%22&hl=en-US&gl=US&ceid=US:en"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    if result.status_code == 200:
        doc = BeautifulSoup(result.text, "xml")

        news_data = []

        for item in doc.find_all("item"):
            title = item.find("title")
            pub_date_string = item.find("pubDate").string
            pub_date = datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
            formatted_date = pub_date.strftime("%B %d, %Y")
            link = item.find("link").text

            data = {
                "Title": title.string,
                "Date": formatted_date,
                "Link": link
            }
            news_data.append(data)
        
     
        additional_news_data = aetherbiomachines2()
        
       
        combined_news_data = news_data
        combined_news_data.extend(additional_news_data)
        
       
        sorted_news_data = sorted(combined_news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)
        
        return render_template("aetherbiomachines.html", data=sorted_news_data)

@auth.route('/aetherdiamonds')
def aetherdiamonds(): 
        url = "https://news.google.com/rss/search?q=%22akash+systems%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("aetherdiamonds.html", data=sorted_news_data)


@auth.route('/akashsystems')
def akashsystems(): 
        url = "https://news.google.com/rss/search?q=%22akash+systems%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("akashsystems.html", data=sorted_news_data)
        

@auth.route('/altopharmacy')
def altopharmacy(): 
        url = "https://news.google.com/rss/search?q=%22alto+pharmacy%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("altopharmacy.html", data=sorted_news_data)
        

@auth.route('/altoira')
def altoira(): 
        url = "https://news.google.com/rss/search?q=%22alto+ira%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("altoira.html", data=sorted_news_data)
        

@auth.route('/americangenetechnologies')
def americangenetechnologies():
        url = "https://news.google.com/rss/search?q=%22american+gene+technologies%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                doc = BeautifulSoup(result.text, "xml")

                news_data = []

                for item in doc.find_all("item"):
                        title = item.find("title")
                        pub_date_string = item.find("pubDate").string
                        pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date=pub_date.strftime("%B %d, %Y")
                        link = item.find("link").text
                        source= item.find("source").string
                
                        print("Title:", title.string)
                        print("Posted on:", formatted_date)
                        print("Link:", link)
                        print()
               
                        if "FierceBiotech" not in source and "Scrip" not in source:          
                                data = {
                                                        "Title": title.string,
                                                        "Date": formatted_date,
                                                        "Link": link
                                                        }
                                news_data.append(data)
                        
                        

                sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                return render_template("americangenetechnologies.html", data=sorted_news_data)
        

@auth.route('/angellist')
def angellist(): 
        url = "https://news.google.com/rss/search?q=angellist&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("angellist.html", data=sorted_news_data)


@auth.route('/angellistsyndicate')
def angellistsyndicate(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("angellistsyndicate.html", data=sorted_news_data)


@auth.route('/anthropic')
def anthropic(): 
        url = "https://news.google.com/rss/search?q=anthropic&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("anthropic.html", data=sorted_news_data)
        

@auth.route('/interlock')
def interlock(): 
        url = "https://news.google.com/rss/search?q=%22interlock%22%20%22decentralized%20security%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("interlock.html", data=sorted_news_data)
        

@auth.route('/appbind')
def appbind(): 
        url = "https://news.google.com/rss/search?q=%22AppBind%22%20%22subscriptions%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("appbind.html", data=sorted_news_data)
        

@auth.route('/artie')
def artie(): 
        url = "https://news.google.com/rss/search?q=%22artie%22%20%22mobile%20gaming%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                        doc = BeautifulSoup(result.text, "xml")

                        news_data = []

                        for item in doc.find_all("item"):
                                title = item.find("title")
                                pub_date_string = item.find("pubDate").string
                                pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                                formatted_date=pub_date.strftime("%B %d, %Y")
                                link = item.find("link").text
                                source= item.find("source").text
                                
                        
                                print("Title:", title.string)
                                print("Posted on:", formatted_date)
                                print("Link:", link)
                                print("Source:", source)
                                print()
                
        
                                excluded_sources = ["The Indian Express", " Casino.org News", "Digital Trends", "CNET", "That Hashtag Show", "VegasSlotsOnline"]

                                if source not in excluded_sources and "Tony 'The Ant' Hitman Nicholas Calabrese Dies Aged 80 - Casino.Org News" not in title:
                                        data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                        }
                                        news_data.append(data)
        
                                        
                        sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                        return render_template("artie.html", data=sorted_news_data)


@auth.route('/ashwellness')
def ashwellness(): 
        url = "https://news.google.com/rss/search?q=%22Ash+Wellness%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ashwellness.html", data=sorted_news_data)
        

@auth.route('/ashvatthatherapeutics')
def ashvatthatherapeutics(): 
        url = "https://news.google.com/rss/search?q=%22ashvattha+therapeutics%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ashvatthatherapeutics.html", data=sorted_news_data)
        

@auth.route('/astranisspacetechnologies')
def astranisspacetechnologies(): 
        url = "https://news.google.com/rss/search?q=%22astranis%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("astranisspacetechnologies.html", data=sorted_news_data)
        

@auth.route('/attivare')
def attivare(): 
        url = "https://news.google.com/rss/search?q=attivare+therapeutics&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                doc = BeautifulSoup(result.text, "xml")

                news_data = []

                for item in doc.find_all("item"):
                        title = item.find("title")
                        pub_date_string = item.find("pubDate").string
                        pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date=pub_date.strftime("%B %d, %Y")
                        link = item.find("link").text
                        source= item.find("source").string
                
                        print("Title:", title.string)
                        print("Posted on:", formatted_date)
                        print("Link:", link)
                        print()
               
                        if "World Health Organization" not in source and "We Make Future" not in source:    
                                data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                                }
                                news_data.append(data)
                        
                        

                sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                return render_template("attivare.html", data=sorted_news_data)
        

@auth.route('/audigent')
def audigent(): 
        url = "https://news.google.com/rss/search?q=%22audigent%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                doc = BeautifulSoup(result.text, "xml")

                news_data = []

                for item in doc.find_all("item"):
                        title = item.find("title")
                        pub_date_string = item.find("pubDate").string
                        pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date=pub_date.strftime("%B %d, %Y")
                        link = item.find("link").text
                        source= item.find("source").string
                
                        print("Title:", title.string)
                        print("Posted on:", formatted_date)
                        print("Link:", link)
                        print()
               
                        if "RMF24" not in source and "RMF FM" not in source:    
                                data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                                }
                                news_data.append(data)
                        
                        

                sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                return render_template("audigent.html", data=sorted_news_data)
        

@auth.route('/axiomspace')
def axiomspace(): 
        url = "https://news.google.com/rss/search?q=%22axiom+space%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("axiomspace.html", data=sorted_news_data)
        

@auth.route('/betr')
def betr(): 
        url = "https://news.google.com/rss/search?q=%22betr%22%20%22betting%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("betr.html", data=sorted_news_data)
        

@auth.route('/better')
def better(): 
        url = "https://news.google.com/rss/search?q=%22better+holdco%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                        doc = BeautifulSoup(result.text, "xml")

                        news_data = []

                        for item in doc.find_all("item"):
                                title = item.find("title")
                                pub_date_string = item.find("pubDate").string
                                pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                                formatted_date=pub_date.strftime("%B %d, %Y")
                                link = item.find("link").text
                                source= item.find("source").text
                                
                        
                                print("Title:", title.string)
                                print("Posted on:", formatted_date)
                                print("Link:", link)
                                print("Source:", source)
                                print()
                
        
                                excluded_sources = ["POLITICO", "Sullivan & Cromwell LLP", "Live Mint"]

                                if source not in excluded_sources:
                                        data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                        }
                                        news_data.append(data)
        
                                        
                        sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                        return render_template("better.html", data=sorted_news_data)
        

@auth.route('/bitvore')
def bitvore(): 
        url = "https://news.google.com/rss/search?q=%22bitvore%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                        doc = BeautifulSoup(result.text, "xml")

                        news_data = []

                        for item in doc.find_all("item"):
                                title = item.find("title")
                                pub_date_string = item.find("pubDate").string
                                pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                                formatted_date=pub_date.strftime("%B %d, %Y")
                                link = item.find("link").text
                                source= item.find("source").text
                                
                        
                                print("Title:", title.string)
                                print("Posted on:", formatted_date)
                                print("Link:", link)
                                print("Source:", source)
                                print()
                
        
                                excluded_sources = ["NEWS.am", "FactSet"]

                                if source not in excluded_sources:
                                        data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                        }
                                        news_data.append(data)
        
                                        
                        sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                        return render_template("bitvore.html", data=sorted_news_data)
        

@auth.route('/blacksharkai')
def blacksharkai(): 
        url = "https://news.google.com/rss/search?q=%22blackshark.ai%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                doc = BeautifulSoup(result.text, "xml")

                news_data = []

                for item in doc.find_all("item"):
                        title = item.find("title")
                        pub_date_string = item.find("pubDate").string
                        pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date=pub_date.strftime("%B %d, %Y")
                        link = item.find("link").text
                        source= item.find("source").string
                
                        print("Title:", title.string)
                        print("Posted on:", formatted_date)
                        print("Link:", link)
                        print()
               
                        if "Asia Pacific Defence Reporter" not in source:    
                                data = {
                                                "Title": title.string,
                                                "Date": formatted_date,
                                                "Link": link
                                                }
                                news_data.append(data)
                        
                        

                sorted_news_data = sorted(news_data, key=lambda x: datetime.strptime(x["Date"], "%B %d, %Y"), reverse=True)   
                return render_template("blacksharkai.html", data=sorted_news_data)
        

@auth.route('/blingfinancial')
def blingfinancial(): 
        url = "https://news.google.com/rss/search?q=%22bling+financial%22&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
                doc = BeautifulSoup(result.text, "xml")

                news_data = []

                for item in doc.find_all("item"):
                        title = item.find("title")
                        pub_date_string = item.find("pubDate").string
                        pub_date= datetime.strptime(pub_date_string, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date=pub_date.strftime("%B %d, %Y")
                        link = item.find("link").text
                        source= item.find("source").string
                
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
                return render_template("blingfinancial.html", data=sorted_news_data)
                
        

@auth.route('/blueberrypediatrics')
def blueberrypediatrics(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("blueberrypediatrics.html", data=sorted_news_data)
        

@auth.route('/branch')
def branch(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("branch.html", data=sorted_news_data)
        

@auth.route('/brex')
def brex(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("brex.html", data=sorted_news_data)
        

@auth.route('/brilliantsmarthome')
def brilliantsmarthome(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("brilliantsmarthome.html", data=sorted_news_data)
        

@auth.route('/briohr')
def briohr(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("briohr.html", data=sorted_news_data)


@auth.route('/carbonhealth')
def carbonhealth(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("carbonhealth.html", data=sorted_news_data)
        

@auth.route('/cerebrassystems')
def cerebrassystems(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("cerebrassystems.html", data=sorted_news_data)
        

@auth.route('/coeliuscapitalrollingfund')
def coeliuscapitalrollingfund(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("coeliuscapitalrollingfund.html", data=sorted_news_data)
        

@auth.route('/cognitivespace')
def cognitivespace(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("cognitivespace.html", data=sorted_news_data)
        

@auth.route('/corelight')
def corelight(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("corelight.html", data=sorted_news_data)
        

@auth.route('/cubii')
def cubii(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("cubii.html", data=sorted_news_data)
        

@auth.route('/dmatrix')
def dmatrix(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("dmatrix.html", data=sorted_news_data)
        

@auth.route('/dapi')
def dapi(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("dapi.html", data=sorted_news_data)
        

@auth.route('/darklang')
def darklang(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("darklang.html", data=sorted_news_data)
        

@auth.route('/deice')
def deice(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("deice.html", data=sorted_news_data)
        

@auth.route('/dnablock')
def dnablock(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("dnablock.html", data=sorted_news_data)
        

@auth.route('/dnovobio')
def dnovobio(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("dnovobio.html", data=sorted_news_data)
        

@auth.route('/doorvest')
def doorvest(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("doorvest.html", data=sorted_news_data)
        

@auth.route('/droplette')
def droplette(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("droplette.html", data=sorted_news_data)
        

@auth.route('/eigentherapeutics')
def eigentherapeutics(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("eigentherapeutics.html", data=sorted_news_data)
        

@auth.route('/emberfund')
def emberfund(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("emberfund.html", data=sorted_news_data)
        

@auth.route('/epicgames')
def epicgames(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("epicgames.html", data=sorted_news_data)
        

@auth.route('/epinoma')
def epinoma(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("epinoma.html", data=sorted_news_data)
        

@auth.route('/eve')
def eve(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("eve.html", data=sorted_news_data)
        

@auth.route('/falcomm')
def falcomm(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("falcomm.html", data=sorted_news_data)
        

@auth.route('/feeltherapeutics')
def feeltherapeutics(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("feeltherapeutics.html", data=sorted_news_data)
        

@auth.route('/finlessfoods')
def finlessfoods(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("finlessfoods.html", data=sorted_news_data)
        

@auth.route('/firefliesai')
def firefliesai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("firefliesai.html", data=sorted_news_data)
        

@auth.route('/forta')
def forta(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("forta.html", data=sorted_news_data)
        

@auth.route('/fretello')
def fretello(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("fretello.html", data=sorted_news_data)
        

@auth.route('/friz')
def friz(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("friz.html", data=sorted_news_data)
        

@auth.route('/frostmethanelabs')
def frostmethanelabs(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("frostmethanelabs.html", data=sorted_news_data)


@auth.route('/gauge')
def gauge(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("gauge.html", data=sorted_news_data)
        

@auth.route('/genies')
def genies(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("genies.html", data=sorted_news_data)
        

@auth.route('/gist')
def gist(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("gist.html", data=sorted_news_data)
        

@auth.route('/glyde')
def glyde(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("glyde.html", data=sorted_news_data)
        

@auth.route('/gocarsubscription')
def gocarsubscription(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("gocarsubscription.html", data=sorted_news_data)
        

@auth.route('/gpuaudio')
def gpuaudio(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("gpuaudio.html", data=sorted_news_data)


@auth.route('/h3xtechnologies')
def h3xtechnologies(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("h3xtechnologies.html", data=sorted_news_data)
        

@auth.route('/helicityspace')
def helicityspace(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("helicityspace.html", data=sorted_news_data)
        

@auth.route('/here')
def here(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("here.html", data=sorted_news_data)
        

@auth.route('/hypersonix')
def hhypersonix(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("hypersonix.html", data=sorted_news_data)
        

@auth.route('/ingeltherapeutics')
def ingeltherapeutics(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ingeltherapeutics.html", data=sorted_news_data)
        

@auth.route('/insomabio')
def insomabio(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("insomabio.html", data=sorted_news_data)
        

@auth.route('/inspectify')
def inspectify(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("inspectify.html", data=sorted_news_data)
        

@auth.route('/ipinovyxbio')
def iipinovyxbio(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ipinovyxbio.html", data=sorted_news_data)


@auth.route('/kalendarai')
def kalendarai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("kalendarai.html", data=sorted_news_data)
        

@auth.route('/kasheesh')
def kasheesh(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("kasheesh.html", data=sorted_news_data)
        

@auth.route('/kernalbiologics')
def kernalbiologics(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("kernalbiologics.html", data=sorted_news_data)
        

@auth.route('/keys')
def keys(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("keys.html", data=sorted_news_data)
        

@auth.route('/koniku')
def koniku(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("koniku.html", data=sorted_news_data)


@auth.route('/lendtable')
def lendtable(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("lendtable.html", data=sorted_news_data)
        

@auth.route('/level')
def level(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("level.html", data=sorted_news_data)
        

@auth.route('/ligandal')
def ligandal(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ligandal.html", data=sorted_news_data)
        

@auth.route('/loop')
def loop(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("loop.html", data=sorted_news_data)


@auth.route('/lvl')
def lvl(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("lvl.html", data=sorted_news_data)
        

@auth.route('/metadata')
def metadata(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("metadata.html", data=sorted_news_data)
        

@auth.route('/mgrana')
def mmgrana(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("mgrana.html", data=sorted_news_data)
        

@auth.route('/miles')
def miles(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("miles.html", data=sorted_news_data)
        

@auth.route('/modularit')
def modularit(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("modularit.html", data=sorted_news_data)
        

@auth.route('/mozart')
def mozart(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("mozart.html", data=sorted_news_data)
        

@auth.route('/mycars')
def mycars(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("mycars.html", data=sorted_news_data)
        

@auth.route('/mythicalgames')
def mythicalgames(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("mythicalgames.html", data=sorted_news_data)
        

@auth.route('/nanonets')
def nanonets(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("nanonets.html", data=sorted_news_data)
        

@auth.route('/noah')
def noah(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("noah.html", data=sorted_news_data)
        

@auth.route('/nopsec')
def nopsec(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("nopsec.html", data=sorted_news_data)
        

@auth.route('/nourishtechnology')
def nourishtechnology(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("nourishtechnology.html", data=sorted_news_data)
        

@auth.route('/numetric')
def numetric(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("numetric.html", data=sorted_news_data)
        

@auth.route('/nutrisense')
def nutrisense(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("nutrisense.html", data=sorted_news_data)


@auth.route('/obviouslyai')
def obviouslyai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("obviouslyai.html", data=sorted_news_data)


@auth.route('/ocient')
def ocient(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ocient.html", data=sorted_news_data)
        

@auth.route('/omaze')
def omaze(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("omaze.html", data=sorted_news_data)
        

@auth.route('/oneroof')
def oneroof(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("oneroof.html", data=sorted_news_data)
        

@auth.route('/onrampinvest')
def onrampinvest(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("onrampinvest.html", data=sorted_news_data)
        

@auth.route('/openprise')
def openprise(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("openprise.html", data=sorted_news_data)
        

@auth.route('/ople')
def ople(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ople.html", data=sorted_news_data)
        

@auth.route('/orbitfab')
def orbitfab(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("orbitfab.html", data=sorted_news_data)       
        

@auth.route('/otisai')
def otisai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("otisai.html", data=sorted_news_data)       
        

@auth.route('/ottertune')
def ottertune(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ottertune.html", data=sorted_news_data)       


@auth.route('/pacaso')
def pacaso(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("pacaso.html", data=sorted_news_data)       


@auth.route('/paga')
def paga(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("paga.html", data=sorted_news_data)       
        

@auth.route('/peopleai')
def peopleai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("peopleai.html", data=sorted_news_data)       


@auth.route('/plantiq')
def plantiq(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("plantiq.html", data=sorted_news_data)       
        

@auth.route('/promakhostherapeutics')
def promakhostherapeutics(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("promakhostherapeutics.html", data=sorted_news_data)  



@auth.route('/radishhealth')
def radishhealth(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("radishhealth.html", data=sorted_news_data)       
        

@auth.route('/rainneuromophics')
def rainneuromophics(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("rainneuromophics.html", data=sorted_news_data)       
        

@auth.route('/rationalvaccines')
def rationalvaccines(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("rationalvaccines.html", data=sorted_news_data)       
        

@auth.route('/raydiant')
def raydiant(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("raydiant.html", data=sorted_news_data)       
        

@auth.route('/resonadolabs')
def resonadolabs(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("resonadolabs.html", data=sorted_news_data)       
        

@auth.route('/ringmd')
def ringmd(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ringmd.html", data=sorted_news_data)       
        

@auth.route('/rnav8bio')
def rnav8bio(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("rnav8bio.html", data=sorted_news_data)       


@auth.route('/row64')
def row64(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("row64.html", data=sorted_news_data)     
        

@auth.route('/sendhub')
def sendhub(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("sendhub.html", data=sorted_news_data)     
        

@auth.route('/shapesxr')
def shapesxr(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("shapesxr.html", data=sorted_news_data) 


@auth.route('/shiplyst')
def shiplyst(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("shiplyst.html", data=sorted_news_data)     
        

@auth.route('/snack')
def snack(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("snack.html", data=sorted_news_data)     
        

@auth.route('/songclip')
def songclip(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("songclip.html", data=sorted_news_data)     
        
@auth.route('/sourse')
def sourse(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("sourse.html", data=sorted_news_data)     


@auth.route('/sparkneuro')
def sparkneuro(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("sparkneuro.html", data=sorted_news_data)
        

@auth.route('/stormx')
def stormx(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("stormx.html", data=sorted_news_data)

    
@auth.route('/studio')
def studio(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("studio.html", data=sorted_news_data)
        

@auth.route('/superplastic')
def superplastic(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("superplastic.html", data=sorted_news_data)


@auth.route('/superworld')
def superworld(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("superworld.html", data=sorted_news_data)
        

@auth.route('/ten63therapeutics')
def ten63therapeutics(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("ten63therapeutics.html", data=sorted_news_data)


@auth.route('/tenzrhealth')
def tenzrhealth(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("tenzrhealth.html", data=sorted_news_data)
        

@auth.route('/testai')
def testai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("testai.html", data=sorted_news_data)
        

@auth.route('/threatquotient')
def threatquotient(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("threatquotient.html", data=sorted_news_data)


@auth.route('/treau')
def treau(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("treau.html", data=sorted_news_data)
        

@auth.route('/triplemint')
def triplemint(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("triplemint.html", data=sorted_news_data)


@auth.route('/umake')
def umake(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("umake.html", data=sorted_news_data)
        

@auth.route('/unspun')
def unspun(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("unspun.html", data=sorted_news_data)


@auth.route('/urbanstems')
def urbanstems(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("urbanstems.html", data=sorted_news_data)
        

@auth.route('/varobank')
def varobank(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("varobank.html", data=sorted_news_data)
        

@auth.route('/venostent')
def venostent(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("venostent.html", data=sorted_news_data)
        

@auth.route('/venusaerospace')
def venusaerospace(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("venusaerospace.html", data=sorted_news_data)


@auth.route('/waev')
def waev(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("waev.html", data=sorted_news_data)
        

@auth.route('/wallarooai')
def wallarooai(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("wallarooai.html", data=sorted_news_data)
        
@auth.route('/workorder')
def workorder(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("workorder.html", data=sorted_news_data)


@auth.route('/yumi')
def yumi(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("yumi.html", data=sorted_news_data)


@auth.route('/yummy')
def yummy(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("yummy.html", data=sorted_news_data)
        

@auth.route('/zainar')
def zainar(): 
        url = "https://news.google.com/rss/search?q=Prenav+Inc&hl=en-US&gl=US&ceid=US:en"

        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        if result.status_code == 200:
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
                        return render_template("zainar.html", data=sorted_news_data)
        


        

        






        
        
        
        



        
        




        
        
        





        

   
        


    
        

   
        


        

        





        

   
        


    
        

   
        

