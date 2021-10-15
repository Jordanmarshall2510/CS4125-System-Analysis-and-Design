#Coded by Jakub Pazej - 18260179
import yaml

class battery:
    battery_size=0 #values read and set in init
    battery_value=0

    def __init__(self):
        with open('config.yaml', 'r') as f:
            config = yaml.load(f, Loader = yaml.FullLoader)
        self.battery_size=config['distribution']['battery_size']
        self.battery_value=config['distribution']['battery_value']

    def getValue(self):
        return self.battery_value

    def getSize(self):
        return self.battery_size

    def setValue(self, value):
        self.battery_value = value

    def setSize(self, value):
        self.battery_size = value
        if (self.battery_value > self.battery_size): self.battery_value = self.battery_size

    def input(self, value, unit):
        if (unit.lower() == 'watt' or 'watts'):
                self.battery_value += value/1000000000
                if (self.battery_value > self.battery_size): self.battery_value = self.battery_size
        elif (unit.lower() == 'kilowatt' or 'kilowatts' or 'kw'):
                self.battery_value += value/1000000
                if (self.battery_value > self.battery_size): self.battery_value = self.battery_size
        elif (unit.lower() == 'megawatt' or 'megawatts' or 'mw'):
                self.battery_value += value/1000
                if (self.battery_value > self.battery_size): self.battery_value = self.battery_size
        elif (unit.lower() == 'gigawatt' or 'gigawatts' or 'gw'):
                self.battery_value += value
                if (self.battery_value > self.battery_size): self.battery_value = self.battery_size
        else:
            print('wrong unit input!!!')

    def output(self, value, unit):
        if (unit.lower() == 'watt' or 'watts'):
                if (self.battery_value - value/1000000000 < 0):
                    return False
                else:
                    self.battery_value -= value/1000000000
                    return True
        elif (unit.lower() == 'kilowatt' or 'kilowatts' or 'kw'):
                if (self.battery_value - value/1000000 < 0):
                    return False
                else:
                    self.battery_value -= value/1000000
                    return True
        elif (unit.lower() == 'megawatt' or 'megawatts' or 'mw'):
                if (self.battery_value - value/1000 < 0):
                    return False
                else:
                    self.battery_value -= value/1000
                    return True
        elif (unit.lower() == 'gigawatt' or 'gigawatts' or 'gw'):
                if (self.battery_value - value < 0):
                    return False
                else:
                    self.battery_value -= value
                    return True
        else:
            print('wrong unit input!!!')