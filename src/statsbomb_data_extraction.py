import requests
from bs4 import BeautifulSoup
import json
import re

class Game:
    """Game object whose only attribute is event-level JSON file (from Statsbomb's github)"""
    
    def __init__(self, json_file):
        self.json_file = json.loads(json_file)


def fetch_matches_for_season(github_season_url):
    """
    Function which take a url from Statsbomb's github for a specific season and returns a dictionary maping game ID's to the game's 
    event level JSON data.
    
    Arguments:
    
    github_season_url - (String) URL from Statsbomb's github. Format is:
                        https://github.com/statsbomb/open-data/blob/master/data/matches/{league_ID}/{season_ID}.json
    """
    req = requests.get(github_season_url).text
    soup = BeautifulSoup(req, "lxml") 
    table = soup.find('table')
    
    game_nums = []
    for td in table.find_all('td'):
        if "match_id" in td.text:
            game_num = re.findall(r'[0-9]+', td.text)[0]
            game_nums.append(game_num)
            
    json_files = []
    base_url_string = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/"
    game_num_dict = {
        game_num  : Game(requests.get(base_url_string + game_num + ".json").text)
        for game_num in game_nums
    }
 
    return game_num_dict


def fetch_all_seasons_for_league(competition_id):
    """
    Function which takes a competition_id, as specified by Statsbomb, and returns a dictionary where each season maps to 
    another dictionary containing all games in that season.
    
    Arguments:
    
    season_id - (int) competition_id as specified by Statsbomb 
                      See here: https://github.com/statsbomb/open-data/blob/master/data/competitions.json
    
    """
    #Get webpage html for competitions.json
    req = requests.get("https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json").text
    #Convert webpage to json format
    competitions_statsbomb = json.loads(req)

    all_seasons_id = {}
    for comps in competitions_statsbomb:
        if comps['competition_id'] == competition_id:
            season_id = comps['season_id']
            season_name = comps['season_name']
        
            all_seasons_id[season_name] = season_id
    
    league_all_games_by_seasons = {}
    
    for keys, values in all_seasons_id.items():
        season_url = "https://github.com/statsbomb/open-data/blob/master/data/matches/{}/{}.json".format(competition_id, values)
        print("Getting season {}...".format(keys))
        season = fetch_matches_for_season(season_url)
        league_all_games_by_seasons[keys] = season
    
    print("Done")
    
    return league_all_games_by_seasons
