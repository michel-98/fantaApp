# Definisci l'URL della richiesta POST
import requests

url = 'https://api.app.fantagoat.it/api/account/login/'

# Definisci gli header della richiesta
headers = {
    'authority': 'api.app.fantagoat.it',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://app.fantagoat.it',
    'referer': 'https://app.fantagoat.it/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}


def getAccessToken(fantaGoatEmail, fantaGoatPassword):
    data = {
        "username": fantaGoatEmail,
        "password": fantaGoatPassword
    }

    # Esegui la richiesta POST con gli header e i dati
    response = requests.post(url, headers=headers, json=data)

    # Verifica se la richiesta ha avuto successo
    if response.status_code == 200:
        # Estrai il JSON di risposta
        response_data = response.json()
        access_token = 'Bearer ' + response_data.get('access_token')
        print(access_token)
        return access_token
    else:
        print(f"Errore nella richiesta: {response.status_code}")
