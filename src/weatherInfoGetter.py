import logging
from weatherInfo import WeatherInfo



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/weather_info_getter.log")
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d:%(levelname)s: %(message)s"))
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)



class WeatherInfoGetter:
    
    @staticmethod
    def getCurrentWeatherByCityNameFromApi(cityName):
        return dict()

    @staticmethod
    def getCurrentWeatherByCoordsFromApi(latitude, longitude):
        return dict()

    @staticmethod
    def parseJsonFromCurrentWeather(dict):
        return WeatherInfo

    @staticmethod
    def get5Day3HourForecastByCityNameFromApi(cityName):
        return dict()

    @staticmethod
    def get5Day3HourForecastByCoordsFromApi(latitude, longitude):
        return dict()

    @staticmethod
    def parseJsonFrom5Day3HourForecast(dict):
        return list() # of WeatherInfo

    @staticmethod
    def getIconForCorrespondingWeather(iconCode):
        return # image