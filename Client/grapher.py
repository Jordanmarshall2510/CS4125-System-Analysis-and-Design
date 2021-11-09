## Where the graphing code will reside
from pandas.core.base import DataError
from database import Database
from datetime import datetime
import pandas as pd
class Grapher:
    db = Database()
    def createDF(self,inputs):
        result = []
        for i in inputs:
            result.append(i)
            if i == "Overall":
                result.append(self.db.selectPowerHistory(i))
            elif i != "Solar" or "Wind":
                result.append(self.db.selectPowerHistory(i))
            else:
                result.append(self.db.selectPowerHistory(i))
        result_dict = {result[i]: result[i + 1] for i in range(0, len(result), 2)}
        return pd.DataFrame(result_dict)
            