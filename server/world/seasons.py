# Coded by [Add yourself here if you did any meaningful work on this class]
import json
import os


class Seasons:
    """Static Seasons class made to calculate and manage seasons in the simulation"""
    season = ''  # Summer, Autumn, Winter, Spring, Dry, Wet, Desert Summer, Polar Winter

    @staticmethod
    def init():
        path = os.path.dirname(os.path.realpath(__file__)).split("world")[
            0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)
            Seasons.season = conf['world']['weather']['season']

    @staticmethod
    def get_season():
        return Seasons.season

    @staticmethod
    def set_season(string):
        if (string.lower() == 'summer' or 'autumn' or 'winter' or 'spring' or 'dry' or 'wet' or 'desert_summer' or 'polar_winter'):
            Seasons.season = string.lower()

    @staticmethod
    def get_season_change(date):

        if 3 <= int(date.strftime("%m")) <= 6:  # spring
            if 3 == int(date.strftime("%m")) and int(date.strftime("%d")) < 20:
                return 'winter'
            elif 6 == int(date.strftime("%m")) and int(date.strftime("%d")) > 20:
                return 'summer'
            else:
                return 'spring'
        elif 6 <= int(date.strftime("%m")) <= 9:  # summer
            if 9 == int(date.strftime("%m")) and int(date.strftime("%d")) > 21:
                return 'autumn'
            else:
                return 'summer'
        elif 9 <= int(date.strftime("%m")) <= 12:  # autumn
            if 12 == int(date.strftime("%m")) and int(date.strftime("%d")) > 20:
                return 'winter'
            else:
                return 'autumn'
        else:  # winter
            return 'winter'

    @staticmethod
    def update_season(date):
        Seasons.set_season(Seasons.get_season_change(date))
