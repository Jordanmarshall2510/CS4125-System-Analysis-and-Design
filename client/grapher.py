## Where the graphing code will reside
from pandas.core.base import DataError
from traitlets.traitlets import Integer
from client.database import Database
from datetime import datetime
import pandas as pd
import numpy as np
import re
import os,json

class Grapher:
    db = Database()
    def get_session_data(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("client")[0] + "server/config.json"

        with open(path) as json_file:
            conf = json.load(json_file)
            business = conf["session"]["electricity_user"]["businesses"]
            house = conf["session"]["electricity_user"]["houses"]
            infrastructure = conf["session"]["electricity_user"]["infrastructure"]
            vehicles = conf["session"]["electricity_user"]["vehicles"]

            solar = conf["session"]["electricity_generator"]["solar"]
            wind = conf["session"]["electricity_generator"]["wind"]

            time = conf["session"]["time"]

        return business, house, infrastructure, vehicles, solar, wind, time

    def create_df(self,inputs):
        result = []
        for i in inputs:
            result.append(i)
            if i == "Overall Generation":
                value = self.db.select_total_generated_power_history()
                pos = []
                for j in value:
                    num = j[0]
                    pos.append(num)
                result.append(pos)
            elif i == "Overall Usage":
                value = self.db.select_total_used_power_history()
                pos = []
                for j in value:
                    num = j[0]
                    pos.append(num)
                result.append(pos)
            elif i == "Solar" or i == "Wind":
                value = self.db.select_generated_power_history(i)
                pos = []
                for j in value:
                    num = j[0]
                    pos.append(num)
                result.append(pos)
            else:
                value = self.db.select_used_power_history(i)
                pos = []
                for j in value:
                    num = j[0]
                    pos.append(num)
                result.append(pos)
        result_dict = {result[i]: result[i + 1] for i in range(0, len(result), 2)}
        selected_generated, selected_usage, total_generated, total_usage = self.get_statistics(result_dict)
        return pd.DataFrame(result_dict), selected_generated, selected_usage, total_generated, total_usage

    def get_statistics(self,selected_items) :
        selected_generated = []
        selected_usage = []
        total_generated = 0
        total_usage = 0

        if 'House' in selected_items.keys():
            total_usage += sum(selected_items['House'])
            selected_usage.append('House')
        if 'Business' in selected_items:
            total_usage += sum(selected_items['Business'])
            selected_usage.append('Business')
        if 'Infrastructure' in selected_items:
            total_usage += sum(selected_items['Infrastructure'])
            selected_usage.append('Infrastructure')
        if 'Vehicle' in selected_items:
            total_usage += sum(selected_items['Vehicle'])
            selected_usage.append('Vehicle')
        if 'Solar' in selected_items:
            total_generated += sum(selected_items['Solar'])
            selected_generated.append('Solar')
        if 'Wind' in selected_items:
            total_generated += sum(selected_items['Wind'])
            selected_generated.append('Wind')
        if 'Overall Generation' in selected_items:
            total_generated = sum(selected_items['Overall Generation'])
            selected_generated.append('Overall Generation')
        if 'Overall Usage' in selected_items:
            total_usage = sum(selected_items['Overall Usage'])
            selected_usage.append('Overall Usage')
        return selected_generated, selected_usage, total_generated, total_usage
            