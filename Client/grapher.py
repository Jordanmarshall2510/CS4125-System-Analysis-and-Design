## Where the graphing code will reside
from pandas.core.base import DataError
from traitlets.traitlets import Integer
from database import Database
from datetime import datetime
import pandas as pd
import numpy as np
import re

class Grapher:
    db = Database()
    selected_items = {}

    def createDF(self,inputs):
        result = []
        for i in inputs:
            result.append(i)
            if i == "Overall Generation":
                value = self.db.selectTotalGeneratedPowerHistory()
                pos = []
                for j in value:
                    num = j[0]
                    pos.append(num)
                result.append(pos)
            elif i == "Overall Usage":
                value = self.db.selectTotalUsedPowerHistory()
                pos = []
                for j in value:
                    num = j[0]
                    pos.append(num)
                result.append(pos)
            elif i == "Solar" or i == "Wind":
                value = self.db.selectGeneratedPowerHistory(i)
                pos = []
                for j in value:
                    num = j[0]
                    pos.append(num)
                result.append(pos)
            else:
                value = self.db.selectUsedPowerHistory(i)
                pos = []
                for j in value:
                    num = j[0]
                    pos.append(num)
                result.append(pos)
        result_dict = {result[i]: result[i + 1] for i in range(0, len(result), 2)}
        total_generated, total_usage = self.getStatistics(result_dict)
        return pd.DataFrame(result_dict),total_generated, total_usage

    def getStatistics(self,selected_items) :
        total_generated = 0
        total_usage = 0
        if 'House' in selected_items.keys():
            print('working!')
            total_generated += sum(selected_items['House'])
        if 'Business' in selected_items:
            total_generated += sum(selected_items['Business'])
        if 'Infrastructure' in selected_items:
            total_generated += sum(selected_items['Infrastructure'])
        if 'Vehicle' in selected_items:
            total_generated += sum(selected_items['Vehicle'])
        if 'Solar' in selected_items:
            total_usage += sum(selected_items['Solar'])
        if 'Wind' in selected_items:
            total_usage += sum(selected_items['Wind'])
        if 'Overall Generation' in selected_items:
            total_generated = sum(selected_items['Overall Generation'])
        if 'Overall Usage' in selected_items:
            total_usage = sum(selected_items['Overall Usage'])
        return total_generated, total_usage
            