import json
import requests

API_BASE_URL = "https://fantasy.premierleague.com/drf/"

class ClassicLeague(object):
    """
    A class representing a classic league in the Fantasy Premier League.
    """
    def __init__(self, league_id):
        self.id = league_id
        self._information = self._information()
        self._league = self._information["league"]

        self.new_entries = self._information["new_entries"]

        self.name = self._league["name"]
        self.created = self._league["created"]
        self.started = self._league["start_event"]

        self.standings = self._information["standings"]["results"]

    @property
    def type(self):
        """Return what kind of league is is, which can be ..."""
        return self._league["league_type"]

    def _information(self):
        return requests.get("{}leagues-classic-standings/{}".format(
            API_BASE_URL, self.id)).json()
        
if __name__ == '__main__':
    print(json.dumps(ClassicLeague(743038).standings))