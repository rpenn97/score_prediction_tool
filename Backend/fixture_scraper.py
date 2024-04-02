from bs4 import BeautifulSoup
import requests
from datetime import datetime,timedelta
import pandas as pd

league_list = ['england','france','germany','italy','spain']

def fixture_list(league_list):

    match_list = []
    day_dictionary = {"Mo":"Mon","Tu":"Tue","We":"Wed","Th":"Thu","Fr":"Fri","Sa":"Sat","Su":"Sun"}
    today = datetime.now().date()
    last_day = today + timedelta(days=6)

    for i in league_list:
        url = f'https://www.soccerstats.com/results.asp?league={i}'
        a = requests.get(url)

        soup = BeautifulSoup(a.text,features="html.parser")
        data = soup.find_all(class_='odd')
        for row in data:
            row = row.text
            if row[0:2] in day_dictionary.keys():
                if "-" not in row:
                    row = row[:-3]
                    row2 = row.split(" ")
                    day_3 = day_dictionary.get(row2[0])
                    row_date = row2[0] + " " + row2[1] + " " + row2[2][0:3]
                    row_date_upd = day_3 + " " + row2[1] + " " + row2[2][0:3]
                    row_date_upd_y = f"{datetime.now().year} {row_date_upd}"
                    date_object = datetime.strptime(row_date_upd_y, "%Y %a %d %b").date()
                    if date_object >= today and date_object <= last_day:
                        row_teams = row.replace(row_date,"")
                        row_teams = ''.join((x for x in row_teams if not x.isdigit()))
                        row_teams = row_teams.replace(":","v")
                        row_teams = row_teams.replace(u'\xa0', u' ')
                        match_list.append(row_teams)
      
    return match_list

match_list = fixture_list(league_list)

def name_converter(match_list):
    match_list_upd = []

    epl_namechange_dict = {"Luton Town":"Luton", "Manchester Utd":"Manchester United", "Newcastle Utd":"Newcastle United", "Nottm Forest":"Nottingham Forest", "Sheffield Utd":"Sheffield United", "West Ham Utd":"West Ham United", "Wolverhampton":"Wolverhampton Wanderers"}
    ligue1_namechange_dict = {"Clermont":"Clermont Foot", "Paris SG":"Paris Saint Germain"}
    bundesliga_namechange_dict = {"FC Augsburg":"Augsburg", "Leverkusen":"Bayer Leverkusen", "Dortmund":"Borussia Dortmund", "Monchengladbach":"Borussia M.Gladbach", "E. Frankfurt":"Eintracht Frankfurt", "FC Koln":"FC Cologne", "Heidenheim":"FC Heidenheim", "FSV Mainz":"Mainz 05", "RB Leipzig":"RasenBallsport Leipzig", "Stuttgart":"VfB Stuttgart"}
    seriea_namechange_dict = {"Inter Milan":"Inter", "AS Roma":"Roma", "Hellas Verona":"Verona"}
    laliga_namechange_dict = {"Athletic Bilbao":"Athletic Club", "FC Barcelona":"Barcelona", "Sevilla FC":"Sevilla"}
    soccerstats_to_understat_names_dict = epl_namechange_dict | ligue1_namechange_dict | bundesliga_namechange_dict | seriea_namechange_dict | laliga_namechange_dict

    for item in match_list:
        temp_list = []
        item = item.split(" v ")
        home_team = item[0]
        away_team = item[1]
        if home_team in soccerstats_to_understat_names_dict.keys():
            home_team_upd = soccerstats_to_understat_names_dict.get(home_team)
            temp_list.append(home_team_upd)
        else:
            temp_list.append(home_team)
        if away_team in soccerstats_to_understat_names_dict.keys():
            away_team_upd = soccerstats_to_understat_names_dict.get(away_team)
            temp_list.append(away_team_upd)
        else:
            temp_list.append(away_team)
        match_list_upd.append(f"{temp_list[0]} v {temp_list[1]}")

    return match_list_upd

match_list_updated = name_converter(match_list)

df = pd.DataFrame({'matches': match_list_updated})
df.to_csv('Backend/fixtures.txt',mode='wb',index=False)
