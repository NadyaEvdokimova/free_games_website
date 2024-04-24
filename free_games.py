import requests

URL = "https://gamerpower.com/api/giveaways"


class FreeGames:
    def __init__(self, platform, sort):
        self.parameters = {
            "platform": platform,
            'type': "game",
            'sort-by': sort
        }
        self.response = requests.get(url=URL, params=self.parameters)
        self.data = self.response.json()
