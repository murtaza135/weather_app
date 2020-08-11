import logging
from enum import Enum
from validationFunctions import checkIfVarIsType, checkVarAgainstMultipleTypes
from datetime import datetime, timedelta



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/weather_info.log")
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d:%(levelname)s: %(message)s"))
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)



class WeatherInfo:
    
    def __init__(self, cityName, coords, shortWeatherDescription, longWeatherDescription,
                actualTemperatureInCelcius, feelsLikeTemperatureInCeclius, humidityPercent,
                windSpeedMph, windDirectionDegrees, cloudinessPercent, weatherIconIDCode,
                weatherIconImage, timeInfoWasRecorded, countryName=None, rainInMmForLast3Hours=0):
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
        checkVarAgainstMultipleTypes(actualTemperatureInCelcius, float, int)
        self.actualTemperatureInCelcius = actualTemperatureInCelcius
        checkVarAgainstMultipleTypes(feelsLikeTemperatureInCeclius, float, int)
        self.feelsLikeTemperatureInCeclius = feelsLikeTemperatureInCeclius
        checkIfVarIsType(humidityPercent, int)
        self.humidityPercent = humidityPercent
        checkVarAgainstMultipleTypes(rainInMmForLast3Hours, float, int)
        self.rainInMmForLast3Hours = rainInMmForLast3Hours
        checkVarAgainstMultipleTypes(windSpeedMph, float, int)
        self.windSpeedMph = windSpeedMph
        checkIfVarIsType(windDirectionDegrees, int)
        self.windDirectionDegrees = windDirectionDegrees
        checkIfVarIsType(cloudinessPercent, int)
        self.cloudinessPercent = cloudinessPercent
        checkIfVarIsType(weatherIconIDCode, str)
        self.weatherIconIDCode = weatherIconIDCode
        checkIfVarIsType(weatherIconImage, bytes)
        self.weatherIconImage = weatherIconImage
        checkIfVarIsType(timeInfoWasRecorded, int)
        self.timeInfoWasRecorded = datetime.fromtimestamp(timeInfoWasRecorded)
        logger.info(f"{self.__class__}: {self.cityName}, {self.timeInfoWasRecorded} - instantiated")

    def getTimeInfoWasRecorded(self):
        return self.timeInfoWasRecorded.strftime("%H:%M")

    def getRainSeverity(self):
        # Values adapted from "https://water.usgs.gov/edu/activity-howmuchrain-metric.html"

        if self.rainInMmForLast3Hours == 0:
            return "N/A"
        elif self.rainInMmForLast3Hours > 0 and self.rainInMmForLast3Hours < 0.5 * 3:
            return "Slight"
        elif self.rainInMmForLast3Hours >= 0.5 * 3 and self.rainInMmForLast3Hours < 4 * 3:
            return "Moderate"
        elif self.rainInMmForLast3Hours >= 4 * 3 and self.rainInMmForLast3Hours < 8 * 3:
            return "Heavy"
        else:
            return "Very Heavy"

    def getWindSpeedSeverity(self):
        # Values adapted from "https://en.wikipedia.org/wiki/Beaufort_scale#Modern_scale"

        if self.windSpeedMph < 3:
            return "Calm"
        elif self.windSpeedMph >= 3 and self.windSpeedMph < 12:
            return "Gentle"
        elif self.windSpeedMph >= 12 and self.windSpeedMph < 24:
            return "Moderate"
        elif self.windSpeedMph >= 24 and self.windSpeedMph < 38:
            return "Strong"
        elif self.windSpeedMph >= 38 and self.windSpeedMph < 54:
            return "Gale"
        elif self.windSpeedMph >= 54 and self.windSpeedMph < 72:
            return "Violent Gale"
        else:
            return "Hurricane"

    def getWindSpeedDirectionInNESW(self):
        if self.windDirectionDegrees < 22.5 or self.windDirectionDegrees >= 337.5:
            return "North"
        elif self.windDirectionDegrees >= 22.5 and self.windDirectionDegrees < 67.5:
            return "Northeast"
        elif self.windDirectionDegrees >= 67.5 and self.windDirectionDegrees < 112.5:
            return "East"
        elif self.windDirectionDegrees >= 112.5 and self.windDirectionDegrees < 157.5:
            return "Southeast"
        elif self.windDirectionDegrees >= 157.5 and self.windDirectionDegrees < 202.5:
            return "South"
        elif self.windDirectionDegrees >= 202.5 and self.windDirectionDegrees < 247.5:
            return "Southwest"
        elif self.windDirectionDegrees >= 247.5 and self.windDirectionDegrees < 292.5:
            return "West"
        else:
            return "Northwest"


class RainSeverity(Enum):
    # Values adapted from "https://water.usgs.gov/edu/activity-howmuchrain-metric.html"

    low = 1  # 0-0.1 mm/hr
    slight = 2  # 0.1-0.5 mm/hr
    moderate = 3  # 0.5-4 mm/hr
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