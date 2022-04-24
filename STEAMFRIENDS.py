import requests 

BASE_URL_FRIENDLIST ="http://api.steampowered.com/ISteamUser/GetFriendList/v0001/"
API_KEY = input ("ENTER STEAM API KEY: ")
STEAMID = input ("ENTER STEAMID: ")
BASE_URL_CONVERT ="http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"

def getfriendslist():
    relationship = "all"
    request_url = f"{BASE_URL_FRIENDLIST}?key={API_KEY}&steamid={STEAMID}&relationship={relationship}&format=json"
    response = requests.get(request_url)
    data = response.json()
    friendslist = data['friendslist']['friends']
    arroffriends = []
    for item in friendslist: 
        steamidlist = (item['steamid']) 
        arroffriends.append(steamidlist) 
    return arroffriends 

def convert_steamid_toname(getfriendslist):
    request_url = f"{BASE_URL_CONVERT}?key={API_KEY}&steamids={getfriendslist}&format=json"
    response = requests.get(request_url)
    data = response.json()
    data2 = data['response']['players']
    for personanames in data2: 
        personaname = (personanames['personaname']) 
        print(personaname) 

convert_steamid_toname(getfriendslist())
