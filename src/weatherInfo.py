import logging
from enum import Enum
from validationFunctions import checkIfVarIsType
from datetime import datetime



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/weather_info.log")
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d:%(levelname)s: %(message)s"))
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)



class WeatherInfo:
    
    def __init__(self, cityName, coords, shortWeatherDescription, longWeatherDescription,
                actualTemperatureInCelcius, feelsLikeTemperatureInCeclius, humidityPercent,
                windSpeedMph, windDirectionDegrees, cloudinessPercent, rainInMmForLast3Hours,
                snowInMmForLast3Hours, weatherIconIDCode, weatherIconImage, timeInfoWasRecorded,
                countryName=None, timezoneDelta=0):
        checkIfVarIsType(cityName, str)
        self.cityName = cityName
        checkIfVarIsType(countryName, str) if countryName is not None else None
        self.countryName = countryName
        checkIfVarIsType(coords, tuple)
        self.coords = coords
        checkIfVarIsType(shortWeatherDescription, str)
        self.shortWeatherDescription = shortWeatherDescription
        checkIfVarIsType(longWeatherDescription, str)
        self.longWeatherDescription = longWeatherDescription
        checkIfVarIsType(actualTemperatureInCelcius, int)
        self.actualTemperatureInCelcius = actualTemperatureInCelcius
        checkIfVarIsType(feelsLikeTemperatureInCeclius, int)
        self.feelsLikeTemperatureInCeclius = feelsLikeTemperatureInCeclius
        checkIfVarIsType(humidityPercent, int)
        self.humidityPercent = humidityPercent
        checkIfVarIsType(windSpeedMph, int)
        self.windSpeedMph = windSpeedMph
        checkIfVarIsType(windDirectionDegrees, int)
        self.windDirectionDegrees = windDirectionDegrees
        checkIfVarIsType(cloudinessPercent, int)
        self.cloudinessPercent = cloudinessPercent
        checkIfVarIsType(weatherIconIDCode, str)
        self.weatherIconIDCode = weatherIconIDCode
        checkIfVarIsType(weatherIconImage, bytes)
        self.weatherIconImage = weatherIconImage
        checkIfVarIsType(timezoneDelta, int)
        checkIfVarIsType(timeInfoWasRecorded, int)
        self.timeInfoWasRecorded = datetime.fromtimestamp(timeInfoWasRecorded)

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
        if self.windDirectionDegrees < 22.5 or self.windDirectionDegrees >= 337.5:
            return WindDirection.north
        elif self.windDirectionDegrees >= 22.5 and self.windDirectionDegrees < 67.5:
            return WindDirection.northeast
        elif self.windDirectionDegrees >= 67.5 and self.windDirectionDegrees < 112.5:
            return WindDirection.east
        elif self.windDirectionDegrees >= 112.5 and self.windDirectionDegrees < 157.5:
            return WindDirection.southeast
        elif self.windDirectionDegrees >= 157.5 and self.windDirectionDegrees < 202.5:
            return WindDirection.south
        elif self.windDirectionDegrees >= 202.5 and self.windDirectionDegrees < 247.5:
            return WindDirection.southwest
        elif self.windDirectionDegrees >= 247.5 and self.windDirectionDegrees < 292.5:
            return WindDirection.west
        else:
            return WindDirection.northwest


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