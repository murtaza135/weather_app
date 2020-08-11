import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/weather_info_getter.log")
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d:%(levelname)s: %(message)s"))
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)



class WeatherInfoGetter:
    pass