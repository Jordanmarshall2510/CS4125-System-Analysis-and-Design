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
        return pd.DataFrame(result_dict)
            