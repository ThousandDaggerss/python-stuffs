import requests


#  Fazer uma API chamar e guardar a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status code:", r.status_code)  # Status code: 200 - a chamada retornou sucesso

#  Guardar a resposta da API em uma variável, igual ao file 'example.json'
resposta_dict = r.json()
print('Total de repositórios:', resposta_dict['total_count'])

#  Explorar informações sobre os repositórios
resp_dicts = resposta_dict['items']
print('Repositórios retornados:', len(resp_dicts))

#  Examinar o primeiro repositório.
# resp_dict = resp_dicts[0]
# print('\nKeys:', len(resp_dict))

#  vamos puxar outros valores pra testar
print("\nInformações recebidas sobre cada repositório da lista:")
for resp_dict in resp_dicts:
    print('\nName:', resp_dict['name'])
    print('Owner:', resp_dict['owner']['login'])
    print('Stars:', resp_dict['stargazers_count'])
    print('Repository:', resp_dict['html_url'])
    print('Description:', resp_dict['description'])

for key in sorted(resp_dict.keys()):
    print(key)

# Processar os resultados.
print(resposta_dict.keys())  # dict_keys(['total_count', 'incomplete_results', 'items'])
