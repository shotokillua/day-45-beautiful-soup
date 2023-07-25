from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", rel="nofollow")

article_texts = []
article_links = []

for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
# print(article_tag)
print(article_texts)
print(article_links)
# print(int(article_upvotes[0].split()[0]))
num_upvotes = [int(article_upvotes[0].split()[0]) for score in article_upvotes]
print(num_upvotes)


highest_number = max(num_upvotes)
highest_number_index = num_upvotes.index(highest_number)
print(highest_number_index)
print(article_texts[highest_number_index])
print(article_links[highest_number_index])









# # import lxml
#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
#
# # for tag in all_anchor_tags:
# #
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)