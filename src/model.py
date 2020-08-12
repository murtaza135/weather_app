from weatherInfoGetter import WeatherInfoGetter
import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/model.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s: %(message)s", "%H:%M:%S"))
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)

file_handler_debug = logging.FileHandler("../logs/model_debug.log")
file_handler_debug.setFormatter(logging.Formatter("%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s: %(message)s", "%H:%M:%S"))
file_handler_debug.setLevel(logging.DEBUG)
logger.addHandler(file_handler_debug)



class Model:

    def __init__(self):
        self.currentWeatherInfo = None
        self.next5DaysOfWeatherInfo = list()

    def obtainCurrentAndNext5DaysWeatherInfoByCityName(self, cityName):
        try:
            logger.info("Retrieving weather information from api")
            currentWeather = WeatherInfoGetter.getCurrentWeatherByCityNameFromApi(cityName)
            self.currentWeatherInfo = WeatherInfoGetter.parseJsonFromCurrentWeather(currentWeather)
            next5DaysWeather = WeatherInfoGetter.get5Day3HourForecastByCityNameFromApi(cityName)
            self.next5DaysOfWeatherInfo = WeatherInfoGetter.parseJsonFrom5Day3HourForecast(next5DaysWeather)
            logger.info("Retrieved weather information from api")
        except (ConnectionError, TypeError, KeyError) as e:
            logger.warning(e)
            raise

    def obtainCurrentAndNext5DaysWeatherInfoByCoords(self, latitude, longitude):
        try:
            logger.info("Retrieving weather information from api")
            currentWeather = WeatherInfoGetter.getCurrentWeatherByCoordsFromApi(latitude, longitude)
            self.currentWeatherInfo = WeatherInfoGetter.parseJsonFromCurrentWeather(currentWeather)
            next5DaysWeather = WeatherInfoGetter.get5Day3HourForecastByCoordsFromApi(latitude, longitude)
            self.next5DaysOfWeatherInfo = WeatherInfoGetter.parseJsonFrom5Day3HourForecast(next5DaysWeather)
            logger.info("Retrieved weather information from api")
        except (ConnectionError, TypeError, KeyError) as e:
            logger.warning(e)
            raise

    def clear(self):
        self.currentWeatherInfo = None
        self.next5DaysOfWeatherInfo = list()