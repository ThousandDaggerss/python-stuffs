import requests
import config
import time

#  Código desenvolvido por @Lord Kark#0755 at discord https://discord.gg/wSXezk64
def create_sala_w2g(url):
    payload = {'Accept': 'application/json', 'Content-tyoe': 'application/json'}
    payload2 = {'w2g_api_key': config.API_KEY_W2G, 'share': url, 'bg_color': '#00ff00', 'bg_opacity': '50'}

    r = requests.post('https://w2g.tv/rooms/create.json', headers=payload, json=payload2)   

    r = r.json()
    stream_key = r['streamkey']
    time.sleep(1)
    
    return f'https://w2g.tv/rooms/{stream_key}'

print(create_sala_w2g('https://w2g.tv/j6z6zjw86q6n0x3sf9'))
