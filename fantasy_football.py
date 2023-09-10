def get_players_by_role(squadra):
    players = squadra['players']

    # Crea un dizionario per conteggiare il numero di giocatori per ruolo
    role_count = {}

    # Crea un dizionario per i giocatori titolari divisi per ruolo
    titolari_per_ruolo = {}

    for player in players:
        ruolo = player['position']
        titolare = player['selection'] == 'F'

        # Aggiungi il ruolo al dizionario dei conteggi
        if ruolo not in role_count:
            role_count[ruolo] = 0

        if titolare:
            # Aggiungi il giocatore ai titolari per il suo ruolo
            if ruolo not in titolari_per_ruolo:
                titolari_per_ruolo[ruolo] = []

            titolari_per_ruolo[ruolo].append(player)
            # Aggiorna il conteggio per quel ruolo
            role_count[ruolo] += 1

    modulo = squadra.get('module', None)  # Ottieni il modulo se presente, altrimenti None

    return modulo, titolari_per_ruolo, role_count
