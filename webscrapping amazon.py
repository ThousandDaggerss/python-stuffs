import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Veirdo-Mens-Cotton-T-shirt-G4_BSR_BLACK_L_Black_Large/dp/B01MSTXWBS/ref=bbp_bb_d33a38_st_pbyk_w_0?psc=1&smid=APT08BGG6TKYO'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id= "productTitle").get_text()
features = soup.find("div", {"id": "feature-bullets"}).find('ul').find_all('li')
availability = soup.find(id="availability").get_text()

print('-' * 40)
print(title.strip())
print('-' * 40)
print(availability.strip())
print('-' * 40)
print("Instruções:")
for dado in features:
    dados_fundo = dado.find_all("span")
    print(
        f"{dados_fundo[0].text}"
    )
print('-' * 40)
