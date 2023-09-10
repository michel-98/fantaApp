import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def invia_email(email_address, password, destinatario, soggetto, message_html, message_text):
    # Crea un oggetto server SMTP (esempio per Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Crea una connessione sicura al server SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Effettua l'accesso al tuo account email
    server.login(email_address, password)

    # Crea un oggetto messaggio
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = destinatario
    message['Subject'] = soggetto

    # Aggiungi il corpo del messaggio in formato HTML e Markdown
    message.attach(MIMEText(message_html, 'html'))
    message.attach(MIMEText(message_text, 'plain'))
    # Invia il messaggio
    server.sendmail(email_address, destinatario, message.as_string())

    # Chiudi la connessione
    server.quit()
