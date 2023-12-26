
import xml.etree.ElementTree as ET

class TemperatureConverter():
    def convert_c2f(self, num):
        self.number = round(((9/5 * num) + 32), 1)
        return self.number

temp_convert = TemperatureConverter()

class ForecastXmlParser():
    def parse(self):
        tree = ET.parse('forecast.xml')
        root = tree.getroot()
        for item in root.findall('item'):
            cels = item.get('temperature_in_celsius')
            far = temp_convert.convert_c2f(cels)
            day = item.get('day')
            print(f'{day}: {cels} Celsius, {far} Fahrenheit')

forecast = ForecastXmlParser()
forecast.parse()