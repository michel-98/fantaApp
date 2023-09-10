import requests
from html2text import html2text

import email_helper
import fantasy_football
import login_helper


def fetch_squadre_and_send_emails(email_address, password, fantaGoatPassword, sergio, antonello):
    # Definisci l'URL della richiesta GET
    url = 'https://api.app.fantagoat.it/api/v1/zona/userprofile/77604/team/'
    bearer = login_helper.getAccessToken(email_address, fantaGoatPassword)
    # Definisci gli headers della richiesta
    headers = {
        'authority': 'api.app.fantagoat.it',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': bearer,
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

    # Esegui la richiesta GET con gli header
    response = requests.get(url, headers=headers)

    # Verifica se la richiesta ha avuto successo
    if response.status_code == 200:
        # Estrai il JSON di risposta
        data = response.json()
        squadre = data['results']
        for squadra in squadre:
            modulo, titolari_per_ruolo, role_count = fantasy_football.get_players_by_role(squadra)
            destinatario = antonello if squadra['name'] == 'FC Braciollona' else sergio
            if modulo is not None:
                message_html = f"<html><body>"
                message_html += f"<h2>Modulo della squadra {squadra['name']}:</h2>"
                ruoli_italiani = {
                    "Forward": "Attaccanti",
                    "Midfielder": "Centrocampisti",
                    "Defender": "Difensori",
                    "Goalkeeper": "Portiere"
                }
                for ruolo, giocatori in titolari_per_ruolo.items():
                    nome_ruolo_italiano = ruoli_italiani.get(ruolo, ruolo)
                    message_html += f"<h3>{nome_ruolo_italiano.capitalize()} titolari:</h3>"
                    message_html += "<ul>"
                    for giocatore in giocatori:
                        message_html += f"<li>{giocatore['firstname']} {giocatore['lastname']}</li>"
                    message_html += "</ul>"

                message_html += "</body></html>"
                # Converte il corpo del messaggio in formato Markdown
                message_text = html2text(message_html)
                email_helper.invia_email(email_address, password, destinatario, f"Squadra {squadra['name']}",
                                         message_html, message_text)

                print(f"Email inviata a {destinatario} per la squadra {squadra['name']}")
            else:
                print(f"Squadra '{squadra['name']}' non trovata nel JSON.")
    else:
        print(f"Errore nella richiesta: {response.status_code}")
