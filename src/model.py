from weatherInfoGetter import WeatherInfoGetter
import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/model.log")
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d:%(levelname)s: %(message)s"))
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)



class Model:

    def __init__(self):
        currentWeatherInfo = None
        next5DaysOfWeatherInfo = list()

    def getCurrentAndNext5DaysWeatherInfoByCityName(self, cityName):
        pass

    def getCurrentAndNext5DaysWeatherInfoByCoords(self, latitude, longitude):
        pass