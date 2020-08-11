from weatherInfoGetter import WeatherInfoGetter
import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/model.log")
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d:%(levelname)s: %(message)s"))
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)



class Model:

    def __init__(self):
        self.currentWeatherInfo = None
        self.next5DaysOfWeatherInfo = list()

    def getCurrentAndNext5DaysWeatherInfoByCityName(self, cityName):
        try:
            currentWeather = WeatherInfoGetter.getCurrentWeatherByCityNameFromApi(cityName)
            self.currentWeatherInfo = WeatherInfoGetter.parseJsonFromCurrentWeather(currentWeather)
            next5DaysWeather = WeatherInfoGetter.get5Day3HourForecastByCityNameFromApi(cityName)
            self.next5DaysOfWeatherInfo = WeatherInfoGetter.parseJsonFrom5Day3HourForecast(next5DaysWeather)
        except (ConnectionError, TypeError, KeyError) as e:
            logger.error(e)

    def getCurrentAndNext5DaysWeatherInfoByCoords(self, latitude, longitude):
        try:
            currentWeather = WeatherInfoGetter.getCurrentWeatherByCoordsFromApi(latitude, longitude)
            self.currentWeatherInfo = WeatherInfoGetter.parseJsonFromCurrentWeather(currentWeather)
            next5DaysWeather = WeatherInfoGetter.get5Day3HourForecastByCoordsFromApi(latitude, longitude)
            self.next5DaysOfWeatherInfo = WeatherInfoGetter.parseJsonFrom5Day3HourForecast(next5DaysWeather)
        except (ConnectionError, TypeError, KeyError) as e:
            logger.error(e)