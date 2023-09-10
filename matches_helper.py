from datetime import datetime

import requests


def getIfTimeIsRunningUp(matchToken):
    uri = 'https://api.football-data.org/v4/competitions/SA/'
    headers = {
        'User-Agent': 'python-requests/2.31.0',
         'Accept-Encoding': 'gzip, deflate',
         'Accept': '*/*',
         'Connection': 'keep-alive',
        'X-Auth-Token': matchToken}

    response = requests.get(uri, headers=headers)
    print(response)
    serieA = response.json()
    currentMatchday = serieA['currentSeason']['currentMatchday']
    uri2 = 'https://api.football-data.org/v4/competitions/SA/matches?matchday=' + str(currentMatchday)

    response2 = requests.get(uri2, headers=headers)
    prossimaGiornata = response2.json()
    dayToStart = prossimaGiornata['resultSet']['first']
    # Convert the date string to a datetime object
    date_object = datetime.strptime(dayToStart, "%Y-%m-%d")

    # Get the current date
    current_date = datetime.now()

    # Calculate the difference in days
    days_difference = (date_object - current_date).days
    print("Days difference: " + str(days_difference))
    return days_difference > 2
