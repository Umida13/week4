# from cgitb import html
# from itertools import product


# import requests
# import json
# from bs4 import BeautifulSoup

# URL = "https://www.kivano.kg/noutbuki"    #->можем исп любую ссылку на этом сайте

# def get_html(url: str) -> str:
#     """
#     Возаращает html response
#     """
#     html = requests.get(url=url).text
#     return html

# def get_data(html:str):
#     soup = BeautifulSoup(html, "lxml")
#     data = soup.find("div", class_="list-view")
#     products = data.find_all("div", class_='item')
#     return products

# html = get_html(url=URL)
# data = get_data(html=html)

# def main(data: list):
#     products_list = list()
#     for product in data:
#         tittle = product.find("div", class_="pull-right").find("div", class_="product_text").find("strong").find("a").text
  

    

# main(data=data)





# URL = "https://www.kivano.kg/noutbuki"  
# page = "?page"
# urls = [URL + page + str(i) for i in range(1, 56)]
# with Pool(os.cpu_count()) as p:
#     p.map(fast_pars, urls)
 


















import csv
import requests
from bs4 import BeautifulSoup

URL = "http://kenesh.kg/ru/deputy/list/35"
def get_html(url:str):
    html = requests.get(url=url)
    return html.text

def get_last_page(html):
    soup = BeautifulSoup(html, "lxml")
    pagination = soup.find("div", class_ = "pagination").find_all("a", class_ = "item")[-1].text
    return int(pagination)

def write_to_csv(data:list) -> None:
    """
    запись в csv формат
    """
    with open("data/info.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "info","email","phone", "image"])
        for item in data:
            writer.writerow([item.get("name"), item.get("info"), item.get("email"), item.get("phone"), item.get("image")])


DATA = []
def get_data(html):
    soup=BeautifulSoup(html,"lxml")
    all_deputas = soup.find("div", class_ = "grid-deputs").find_all("div", class_ = "dep-item")
    for deput in all_deputas:
        try:
            name = deput.find("a", class_ = "name").text
            # print(name)
        except:
            name = "-"

        try:
            desc = deput.find("div", class_="info").txt
            # print(desc)
        except:
            desc = "-"


        try:
            email = deput.find("div", class_="buttom-info").find("a", class_="mail").text
            print(email)
        except:
            email = "-"

        try:
            phone =deput.find("div",  class_="bottom-info").find("a",class_="phone-call").text
        #     print(phone)
        except:
            phone = "-"
            try:
                image = deput.find("div", class_="image").find("img").get("src")
                image = "http://kenesh.kg" + image
                print(image)
            except:
                image = "-"
            {"name": name, "info": info, "email"}

html = get_html(url=URL)
get_last_page(html)
print(get_data(html=html))






