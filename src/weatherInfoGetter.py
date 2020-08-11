import logging
import os
import requests
from weatherInfo import WeatherInfo
from PySide2.QtGui import QPixmap
from PIL.ImageQt import ImageQt



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/weather_info_getter.log")
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d:%(levelname)s: %(message)s"))
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)



class WeatherInfoGetter:

    API_KEY = os.environ.get("WeatherAppKey")
    
    @classmethod
    def getCurrentWeatherByCityNameFromApi(cls, cityName):
        payload = {"q": cityName, "units": "metric", "appid": cls.API_KEY}
        url = "https://api.openweathermap.org/data/2.5/weather"
        request = requests.get(url, params=payload)
        if request.status_code != 200 or request.json()["cod"] != 200:
            logger.error(f"Could not connect to {url}")
            raise ConnectionError(f"Could not connect to {url}")
        logger.info(f"Successfully connected to {url}")
        return request.json()

    @classmethod
    def getCurrentWeatherByCoordsFromApi(cls, latitude, longitude):
        payload = {"lat": latitude, "lon": longitude, "units": "metric", "appid": cls.API_KEY}
        url = "https://api.openweathermap.org/data/2.5/weather"
        request = requests.get(url, params=payload)
        if request.status_code != 200 or request.json()["cod"] != 200:
            logger.error(f"Could not connect to {url}")
            raise ConnectionError(f"Could not connect to {url}")
        logger.info(f"Successfully connected to {url}")
        return request.json()

    @classmethod
    def parseJsonFromCurrentWeather(cls, jsonDict):
        weatherInfoObject = WeatherInfo(
            cityName=jsonDict["name"],
            countryName=jsonDict["sys"]["country"] if "country" in jsonDict["sys"] else None,
            coords=(jsonDict["coord"]["lat"], jsonDict["coord"]["lon"]),
            shortWeatherDescription=jsonDict["weather"][0]["main"],
            longWeatherDescription=jsonDict["weather"][0]["description"],
            actualTemperatureInCelcius=jsonDict["main"]["temp"],
            feelsLikeTemperatureInCeclius=jsonDict["main"]["feels_like"],
            humidityPercent=jsonDict["main"]["humidity"],
            rainInMmForLast3Hours=jsonDict["rain"]["3h"] if "rain" in jsonDict and "3h" in jsonDict["rain"] else 0,
            windSpeedMph=jsonDict["wind"]["speed"],
            windDirectionDegrees=jsonDict["wind"]["deg"],
            cloudinessPercent=jsonDict["clouds"]["all"],
            weatherIconIDCode=jsonDict["weather"][0]["icon"],
            weatherIconImage=cls.getIconByteImageForCorrespondingWeather(jsonDict["weather"][0]["icon"]),
            timeInfoWasRecorded=jsonDict["dt"]
        )

        logger.info("Successfully created WeatherInfo object")
        return weatherInfoObject

    @classmethod
    def get5Day3HourForecastByCityNameFromApi(cls, cityName):
        payload = {"q": cityName, "units": "metric", "appid": cls.API_KEY}
        url = "https://api.openweathermap.org/data/2.5/forecast"
        request = requests.get(url, params=payload)
        if request.status_code != 200 or request.json()["cod"] != 200:
            logger.error(f"Could not connect to {url}")
            raise ConnectionError(f"Could not connect to {url}")
        logger.info(f"Successfully connected to {url}")
        return request.json()

    @classmethod
    def get5Day3HourForecastByCoordsFromApi(cls, latitude, longitude):
        payload = {"lat": latitude, "lon": longitude, "units": "metric", "appid": cls.API_KEY}
        url = "https://api.openweathermap.org/data/2.5/forecast"
        request = requests.get(url, params=payload)
        if request.status_code != 200 or request.json()["cod"] != 200:
            logger.error(f"Could not connect to {url}")
            raise ConnectionError(f"Could not connect to {url}")
        logger.info(f"Successfully connected to {url}")
        return request.json()

    @classmethod
    def parseJsonFrom5Day3HourForecast(cls, jsonDict):
        weatherInfoList = list()

        for i in range(len(jsonDict["list"])):
            weather = WeatherInfo(
                cityName=jsonDict["city"]["name"],
                countryName=jsonDict["city"]["country"] if "country" in jsonDict["city"] else None,
                coords=(jsonDict["city"]["coord"]["lat"], jsonDict["city"]["coord"]["lon"]),
                shortWeatherDescription=jsonDict["list"][i]["weather"][0]["main"],
                longWeatherDescription=jsonDict["list"][i]["weather"][0]["description"],
                actualTemperatureInCelcius=jsonDict["list"][i]["main"]["temp"],
                feelsLikeTemperatureInCeclius=jsonDict["list"][i]["main"]["feels_like"],
                humidityPercent=jsonDict["list"][i]["main"]["humidity"],
                rainInMmForLast3Hours=jsonDict["list"][i]["rain"]["3h"] if "rain" in jsonDict["list"][i] and "3h" in jsonDict["list"][i]["rain"] else 0,
                windSpeedMph=jsonDict["list"][i]["wind"]["speed"],
                windDirectionDegrees=jsonDict["list"][i]["wind"]["deg"],
                cloudinessPercent=jsonDict["list"][i]["clouds"]["all"],
                weatherIconIDCode=jsonDict["list"][i]["weather"][0]["icon"],
                weatherIconImage=cls.getIconByteImageForCorrespondingWeather(jsonDict["list"][i]["weather"][0]["icon"]),
                timeInfoWasRecorded=jsonDict["list"][i]["dt"]
            )
            weatherInfoList.append(weather)

        logger.info("Successfully created list of WeatherInfo objects")
        return weatherInfoList

    @staticmethod
    def getIconByteImageForCorrespondingWeather(iconCode):
        url = f"http://openweathermap.org/img/wn/{iconCode}@2x.png"
        request = requests.get(url)
        if request.status_code != 200:
            logger.error(f"Could not get image from {url}")
            raise ConnectionError(f"Could not connect to {url}")
        logger.info(f"Successfully retrieved image from {url}")
        return request.content