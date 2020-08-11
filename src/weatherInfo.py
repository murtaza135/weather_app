import logging
from enum import Enum
from validationFunctions import checkIfVarIsType



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/weather_info.log")
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d:%(levelname)s: %(message)s"))
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)



class WeatherInfo:
    
    def __init__(self, cityName, countryName, coords, shortWeatherDescription, longWeatherDescription,
                actualTemperatureInCelcius, feelsLikeTemperatureInCeclius, humidityPercent,
                windSpeedMph, windDirectionDegrees, cloudinessPercent, rainInMmForLast3Hours,
                snowInMmForLast3Hours, weatherIconIDCode, weatherIconImage, timeInfoWasRecorded):
        self.cityName = checkIfVarIsType(cityName, str)
        self.countryName = checkIfVarIsType(countryName, str)
        self.coords = checkIfVarIsType(coords, tuple)
        self.shortWeatherDescription = checkIfVarIsType(shortWeatherDescription, str)
        self.longWeatherDescription = checkIfVarIsType(longWeatherDescription, str)
        self.actualTemperatureInCelcius = checkIfVarIsType(actualTemperatureInCelcius, int)
        self.feelsLikeTemperatureInCeclius = checkIfVarIsType(feelsLikeTemperatureInCeclius, int)
        self.humidityPercent = checkIfVarIsType(humidityPercent, int)
        self.windSpeedMph = checkIfVarIsType(windSpeedMph, int)
        self.windDirectionDegrees = checkIfVarIsType(windDirectionDegrees, int)
        self.cloudinessPercent = checkIfVarIsType(cloudinessPercent, int)
        self.rainInMmForLast3Hours = checkIfVarIsType(rainInMmForLast3Hours, int)
        self.snowInMmForLast3Hours = checkIfVarIsType(snowInMmForLast3Hours, int)
        self.weatherIconIDCode = checkIfVarIsType(weatherIconIDCode, str)
        self.weatherIconImage = weatherIconImage
        self.timeInfoWasRecorded = timeInfoWasRecorded

        logger.info(f"{self.__class__} instantiated")

    def getRainSeverity(self):
        # Values adapted from "https://water.usgs.gov/edu/activity-howmuchrain-metric.html"

        if self.rainInMmForLast3Hours < 0.5 * 3:
            return RainSeverity.low
        elif self.rainInMmForLast3Hours >= 0.5 * 3 and self.rainInMmForLast3Hours < 2 * 3:
            return RainSeverity.slight
        elif self.rainInMmForLast3Hours >= 2 * 3 and self.rainInMmForLast3Hours < 4 * 3:
            return RainSeverity.moderate
        elif self.rainInMmForLast3Hours >= 4 * 3 and self.rainInMmForLast3Hours < 8 * 3:
            return RainSeverity.heavy
        else:
            return RainSeverity.veryHeavy

    def getWindSpeedSeverity(self):
        # Values adapted from "https://en.wikipedia.org/wiki/Beaufort_scale#Modern_scale"
        
        if self.windSpeedMph < 3:
            return WindSpeedSeverity.calm
        elif self.windSpeedMph >= 3 and self.windSpeedMph < 12:
            return WindSpeedSeverity.gentle
        elif self.windSpeedMph >= 12 and self.windSpeedMph < 24:
            return WindSpeedSeverity.moderate
        elif self.windSpeedMph >= 24 and self.windSpeedMph < 38:
            return WindSpeedSeverity.strong
        elif self.windSpeedMph >= 38 and self.windSpeedMph < 54:
            return WindSpeedSeverity.gale
        elif self.windSpeedMph >= 54 and self.windSpeedMph < 72:
            return WindSpeedSeverity.violentGale
        else:
            return WindSpeedSeverity.hurricane

    def getWindSpeedDirectionInNESW(self):
        pass


class RainSeverity(Enum):
    # Values adapted from "https://water.usgs.gov/edu/activity-howmuchrain-metric.html"

    low = 1  # 0-0.5 mm/hr
    slight = 2  # 0.5-2 mm/hr
    moderate = 3  # 2-4 mm/hr
    heavy = 4  # 4-8 mm/hr
    veryHeavy = 5  # 8+ mm/hr


class WindSpeedSeverity(Enum):
    # Values adapted from "https://en.wikipedia.org/wiki/Beaufort_scale#Modern_scale"

    calm = 1  # 0-3 mph
    gentle = 2  # 4-12 mph
    moderate = 3  # 13-24 mph
    strong = 4  # 25-38 mph
    gale = 5  # 39-54 mph
    violentGale = 6  # 55-72 mph
    hurricane = 7  # 73+ mph


class WindDirection(Enum):
    north = 1
    northeast = 2
    east = 3
    southeast = 4
    south = 5
    southwest = 6
    west = 7
    northwest = 8