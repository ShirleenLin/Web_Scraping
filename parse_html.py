import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import numpy as np


response = requests.get("https://www.ctvnews.ca/business/homeowners-brace-for-mortgage-payment-shock-amid-higher-for-longer-rate-outlook-1.6585658")
soup = BeautifulSoup(response.content)
# full_text = ' '.join([p.text for p in soup.find_all('p')])  - if you want to print the whole article
interest_rates_sentences ="\n".join([p.text for p in soup.find_all('p') if 'interest rates' in p.text.lower()])
print("Sentences Containing 'Interest Rates'\n",interest_rates_sentences)
sentiment = [TextBlob(p.text).sentiment.polarity for p in soup.find_all('p') if 'interest rates' in p.text.lower()]
print("Sentiment Score of each sentence",sentiment)
print("【Positive Sentiment】",np.where(np.array(sentiment) >0,1,0).sum(),"VS 【Negative Sentiment】",np.where(np.array(sentiment)<0,1,0).sum())
print("【Overall Sentiment:】", "Positive" if TextBlob(interest_rates_sentences).sentiment.polarity>0 else "Negative")



# first_header = soup.find("script")
# # print(first_header)
# paragraph = soup.find_all("p" , attrs= {"id" : "paragraph-id"})
# print(paragraph)
# print("p.paragraph-id",soup.find("p#paragraph-id"))
# print("p.paragraph-id",soup.find_all("p#paragraph-id"))
# print("p.paragraph-id",soup.select("p#paragraph-id"))
# # headers = soup.find_all("h2")
# # print(headers)
# # first_header = soup.find_all(["h1" , "h2"])
# # first_header
# print("p\n", soup.select("p"))
# print("div p\n", soup.select("div p"))
# print("div > p\n", soup.select("div > p"))
# print("body > p\n", soup.select("body > p"))
# print("h2 ~ p\n", soup.select("h2 ~ p"))
# print("body > * > p\n", soup.select("body > * > p"))
# print("p#paragraph-id b\n", soup.select("p#paragraph-id b"))
# print("p#paragraph-id\n", soup.select("p#paragraph-id")) # - cuz this is id; if it's class: soup.select("ul.socials")
# print("div[align=middle]\n", soup.select("div[align=middle]"))
# print(soup.find_all("p" , attrs= {"id" : "paragraph-id"}))
# print(soup.find_all("p"))
