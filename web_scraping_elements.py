import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozzila/5.0'}

#  Busca o código html da página que quer analisar
pagina = requests.get('https://fundamentus.com.br/fii_imoveis.php', headers=headers)

#  Instancie o BeautifulSoup, passando o html no construtor e parser
soup = BeautifulSoup(pagina.text, 'html.parser')

#  ctrl+shift+i => atalho pra modo desenvolvedor no opera/chrome
#  Ache o dado que quer na página para isso (nesse exemplo queremos a tabela em tbody elemento tr)
dados = soup.find("table", {"id": "tabelaFiiImoveis"}).find('tbody').find_all('tr')

#  vamos fazer um loop for pra puxar todos dados "td" stockados na variável dados e printar um a um
for fundo in dados:
    dados_fundo = fundo.find_all("td")
    print(
        f"[{dados_fundo[0].text}]\n"
        f"\tImóvel: {dados_fundo[1].text}\n"
        f"\tEndereço: {dados_fundo[2].text}\n"
        f"\tOutros: {dados_fundo[3].text}\n"
    )
