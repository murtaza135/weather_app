from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from worker import Worker
import logging
import json



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/view.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s: %(message)s", "%H:%M:%S"))
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)



class MainWindow(QtWidgets.QMainWindow):

    CITY_NAMES_JSON_FILE = "../config/city_names.json"
    
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.initMainWindow()
        self.initUI()
        # self.model.obtainCurrentAndNext5DaysWeatherInfoByCityName("Edinburgh")
        self.showWidgetsIfInfoAvailableElseHide()
        self.threadpool = QtCore.QThreadPool()

    def initMainWindow(self):
        self.setGeometry(200,200,1300,750)
        self.setMinimumWidth(1300)
        self.setMinimumHeight(750)
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QtGui.QIcon("../images/icon.ico"))
        self.setStyleSheet("background-color: #016bac")

    def initUI(self):
        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setHorizontalSpacing(7)
        self.mainLayout.setVerticalSpacing(25)
        self.mainLayout.setContentsMargins(25, 18, 25, 18)
        # self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)

        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        # self.cityNames = self.getCityNamesFromJson()
        # self.cityNamesCompleter = QtWidgets.QCompleter(self.cityNames)
        # self.cityNamesCompleter.setCaseSensitivity(Qt.CaseInsensitive)

        self.searchBox = QtWidgets.QLineEdit()
        self.searchBox.setStyleSheet("color: white;" "font-size: 24px;" "padding-left: 5px")
        # self.searchBox.setCompleter(self.cityNamesCompleter)
        self.searchBox.returnPressed.connect(self.getWeatherInfoAndDisplay)
        self.mainLayout.addWidget(self.searchBox, 0, 0, 1, 4)

        self.searchButton = QtWidgets.QPushButton(text="Search")
        self.searchButton.setStyleSheet("background-color: #004c82;" "color: white;" "font-size: 24px;")
        self.searchButton.setMaximumHeight(33)
        self.searchButton.clicked.connect(self.getWeatherInfoAndDisplay)
        self.mainLayout.addWidget(self.searchButton, 0, 4, 1, 1)
        
        self.currentWeatherInfo = CurrentWeatherInfoDisplay(self.model)
        self.mainLayout.addWidget(self.currentWeatherInfo, 1, 0, 1, 2)

        self.next5DaysWeatherInfo = Next5DaysWeatherInfoDisplay(self.model)
        self.mainLayout.addWidget(self.next5DaysWeatherInfo, 1, 2, 1, 3)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacer, 2, 0)

    def getWeatherInfoAndDisplay(self):
        cityName = self.searchBox.text().strip()
        if cityName != "":
            worker = Worker(self.model.obtainCurrentAndNext5DaysWeatherInfoByCityName, cityName)
            worker.signals.started.connect(self.disableSearchAbility)
            worker.signals.error.connect(self.showErrorMessageBox)
            worker.signals.finished.connect(self.showWidgetsIfInfoAvailableElseHide)
            self.threadpool.start(worker)

    def disableSearchAbility(self):
        self.searchBox.blockSignals(True)
        self.searchButton.setEnabled(False)

    def enableSearchAbility(self):
        self.searchBox.blockSignals(False)
        self.searchButton.setEnabled(True)

    def showWidgetsIfInfoAvailableElseHide(self):
        self.enableSearchAbility()
        if self.model.currentWeatherInfo is not None:
            self.updateTextAndImagesOnAllWidgets()
            self.showAllWidgets()
        else:
            self.hideAllWidgetsExceptSearchOptions()

    def updateTextAndImagesOnAllWidgets(self):
        self.currentWeatherInfo.updateTextAndImagesOnAllWidgets()
        self.next5DaysWeatherInfo.updateTextAndImagesOnAllWidgets()

    def showAllWidgets(self):
        self.currentWeatherInfo.show()
        self.next5DaysWeatherInfo.show()
    
    def hideAllWidgetsExceptSearchOptions(self):
        self.currentWeatherInfo.hide()
        self.next5DaysWeatherInfo.hide()

    def showErrorMessageBox(self, errorInfo):
        QtWidgets.QMessageBox.warning(self, "Warning", "Could not retrieve weather information")

    def getCityNamesFromJson(self):
        with open(type(self).CITY_NAMES_JSON_FILE, "r", encoding="utf-8") as f:
            cityNames = json.load(f)
        return cityNames

class CurrentWeatherInfoDisplay(QtWidgets.QWidget):
    
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.initUI()

    def initUI(self):
        # self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setSpacing(0)


        locationTimeLayout = QtWidgets.QVBoxLayout()
        locationTimeLayout.setSpacing(0)
        self.mainLayout.addLayout(locationTimeLayout)

        self.locationLabel = QtWidgets.QLabel()
        self.locationLabel.setStyleSheet("color: white;" "font-size: 32px;" "padding-left: 0px")
        locationTimeLayout.addWidget(self.locationLabel)

        self.timeLabel = QtWidgets.QLabel()
        self.timeLabel.setStyleSheet("color: white; font-size: 16px; padding-left: 0px")
        locationTimeLayout.addWidget(self.timeLabel)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        locationTimeLayout.addItem(spacer)


        pictureTempDescriptionLayout = QtWidgets.QGridLayout()
        pictureTempDescriptionLayout.setHorizontalSpacing(0)
        pictureTempDescriptionLayout.setVerticalSpacing(0)
        self.mainLayout.addLayout(pictureTempDescriptionLayout)

        self.weatherPicture = QtWidgets.QLabel()
        self.weatherPicture.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        pictureTempDescriptionLayout.addWidget(self.weatherPicture, 0, 0)

        self.actualTemperatureLabel = QtWidgets.QLabel()
        self.actualTemperatureLabel.setStyleSheet("color: white; font-size: 40px; padding-left: 5px")
        pictureTempDescriptionLayout.addWidget(self.actualTemperatureLabel, 0, 1)

        self.longDescriptionLabel = QtWidgets.QLabel()
        self.longDescriptionLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.longDescriptionLabel.setWordWrap(True)
        pictureTempDescriptionLayout.addWidget(self.longDescriptionLabel, 1, 0, 1, 2)


        spacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addItem(spacer)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mainLayout.addWidget(line)

        spacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addItem(spacer)


        remainingWeatherInfoLayout = QtWidgets.QGridLayout()
        remainingWeatherInfoLayout.setSpacing(15)
        self.mainLayout.addLayout(remainingWeatherInfoLayout)

        self.feelsLikeTemeperatureLabel = QtWidgets.QLabel()
        self.feelsLikeTemeperatureLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        remainingWeatherInfoLayout.addWidget(self.feelsLikeTemeperatureLabel)

        self.humidityPercentLabel = QtWidgets.QLabel()
        self.humidityPercentLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        remainingWeatherInfoLayout.addWidget(self.humidityPercentLabel)

        self.windSpeedMphLabel = QtWidgets.QLabel()
        self.windSpeedMphLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        remainingWeatherInfoLayout.addWidget(self.windSpeedMphLabel)

        self.cloudinessPercentLabel = QtWidgets.QLabel()
        self.cloudinessPercentLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        remainingWeatherInfoLayout.addWidget(self.cloudinessPercentLabel)

        self.rainInMmForLast3HoursLabel = QtWidgets.QLabel()
        self.rainInMmForLast3HoursLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        remainingWeatherInfoLayout.addWidget(self.rainInMmForLast3HoursLabel)


        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacer)

    def updateTextAndImagesOnAllWidgets(self):
        currentWeatherInfo = self.model.currentWeatherInfo
        if currentWeatherInfo is not None:
            self.locationLabel.setText(f"{currentWeatherInfo.cityName} {currentWeatherInfo.coords}")
            self.timeLabel.setText(f"Updated {currentWeatherInfo.getTimeInfoWasRecorded()}")
            self.actualTemperatureLabel.setText("{:.0f}°C".format(currentWeatherInfo.actualTemperatureInCelcius))
            self.longDescriptionLabel.setText(f"{currentWeatherInfo.longWeatherDescription}")
            self.feelsLikeTemeperatureLabel.setText("Feels Like: {:.0f}°C".format(currentWeatherInfo.feelsLikeTemperatureInCeclius))
            self.humidityPercentLabel.setText(f"Humidity: {currentWeatherInfo.humidityPercent}%")
            self.windSpeedMphLabel.setText(f"Wind: {currentWeatherInfo.windSpeedMph}mph {currentWeatherInfo.getWindSpeedDirectionInNESW()} ({currentWeatherInfo.getWindSpeedSeverity()})")
            self.cloudinessPercentLabel.setText(f"Cloudiness: {currentWeatherInfo.cloudinessPercent}%")
            self.rainInMmForLast3HoursLabel.setText(f"Rain: {currentWeatherInfo.getRainSeverity()}")

            weatherPixmap = QtGui.QPixmap()
            weatherPixmap.loadFromData(currentWeatherInfo.weatherIconImage)
            weatherPixmap = weatherPixmap.scaled(175, 175, QtCore.Qt.KeepAspectRatio)
            self.weatherPicture.setPixmap(weatherPixmap)


class Next5DaysWeatherInfoDisplay(QtWidgets.QWidget):

    NUM_WEATHER_INFO_TO_DISPLAY = 8
    
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.initUI()


    def initUI(self):
        # self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.mainLayout = QtWidgets.QHBoxLayout(self)
        self.mainLayout.setSpacing(0)

        spacer = QtWidgets.QSpacerItem(25, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addItem(spacer)

        self.specifiedHourWeatherInfoWidgets = [SpecifiedHourWeatherInfo(self.model) for _ in range(type(self).NUM_WEATHER_INFO_TO_DISPLAY)]
        for widget in self.specifiedHourWeatherInfoWidgets:
            self.mainLayout.addWidget(widget)

    def updateTextAndImagesOnAllWidgets(self):
        next5DaysOfWeatherInfo = self.model.next5DaysOfWeatherInfo
        if type(next5DaysOfWeatherInfo) == list and len(next5DaysOfWeatherInfo) > 0:
            for index, widget in enumerate(self.specifiedHourWeatherInfoWidgets):
                widget.updateTextAndImagesOnAllWidgets(index)


class SpecifiedHourWeatherInfo(QtWidgets.QFrame):

    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.initUI()

    def initUI(self):
        self.mainLayout = QtWidgets.QGridLayout(self)
        self.mainLayout.setHorizontalSpacing(5)
        self.mainLayout.setVerticalSpacing(50)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.VLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addWidget(line, 0, 0, 6, 1)

        self.timeLabel = QtWidgets.QLabel()
        self.timeLabel.setStyleSheet("color: white; font-size: 22px; padding-left: 7px; font-weight: bold")
        self.timeLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.timeLabel, 0, 1)

        self.weatherIconLabel = QtWidgets.QLabel()
        self.weatherIconLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.weatherIconLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.weatherIconLabel, 1, 1)

        self.temperatureLabel = QtWidgets.QLabel()
        self.temperatureLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 12px")
        self.temperatureLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.temperatureLabel, 2, 1)

        cloudinessLayout = QtWidgets.QVBoxLayout()
        cloudinessLayout.setSpacing(0)
        self.mainLayout.addLayout(cloudinessLayout, 3, 1)

        self.cloudinessIconLabel = QtWidgets.QLabel()
        cloudinessIconPixmap = QtGui.QPixmap("../images/cloudiness.png")
        cloudinessIconPixmap = cloudinessIconPixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.cloudinessIconLabel.setPixmap(cloudinessIconPixmap)
        self.cloudinessIconLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 12px")
        self.cloudinessIconLabel.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        cloudinessLayout.addWidget(self.cloudinessIconLabel)

        self.cloudinessLabel = QtWidgets.QLabel()
        self.cloudinessLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 14px")
        self.cloudinessLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        cloudinessLayout.addWidget(self.cloudinessLabel)

        rainLayout = QtWidgets.QVBoxLayout()
        rainLayout.setSpacing(0)
        self.mainLayout.addLayout(rainLayout, 4, 1)

        self.rainIconLabel = QtWidgets.QLabel()
        rainIconPixmap = QtGui.QPixmap("../images/rain.png")
        rainIconPixmap = rainIconPixmap.scaled(60, 60, QtCore.Qt.KeepAspectRatio)
        self.rainIconLabel.setPixmap(rainIconPixmap)
        self.rainIconLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 9px")
        self.rainIconLabel.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        rainLayout.addWidget(self.rainIconLabel)

        self.rainLabel = QtWidgets.QLabel()
        self.rainLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 13px")
        self.rainLabel.setWordWrap(True)
        self.rainLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        rainLayout.addWidget(self.rainLabel)

        windSpeedLayout = QtWidgets.QVBoxLayout()
        windSpeedLayout.setSpacing(0)
        self.mainLayout.addLayout(windSpeedLayout, 5, 1)

        self.windSpeedIconLabel = QtWidgets.QLabel()
        windSpeedIconPixmap = QtGui.QPixmap("../images/wind.png")
        windSpeedIconPixmap = windSpeedIconPixmap.scaled(35, 35, QtCore.Qt.KeepAspectRatio)
        self.windSpeedIconLabel.setPixmap(windSpeedIconPixmap)
        self.windSpeedIconLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 24px")
        self.windSpeedIconLabel.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        windSpeedLayout.addWidget(self.windSpeedIconLabel)

        self.windSpeedLabel = QtWidgets.QLabel()
        self.windSpeedLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 10px")
        self.windSpeedLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        windSpeedLayout.addWidget(self.windSpeedLabel)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacer, 6, 0)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addItem(spacer, 0, 2, 7, 1)

    def updateTextAndImagesOnAllWidgets(self, index):
        next5DaysOfWeatherInfo = self.model.next5DaysOfWeatherInfo
        if type(next5DaysOfWeatherInfo) == list and len(next5DaysOfWeatherInfo) > 0:
            self.timeLabel.setText(f"{next5DaysOfWeatherInfo[index].getTimeInfoWasRecorded()}")
            self.temperatureLabel.setText("{:.0f}°C".format(next5DaysOfWeatherInfo[index].actualTemperatureInCelcius))
            self.cloudinessLabel.setText(f"{next5DaysOfWeatherInfo[index].cloudinessPercent}%")
            self.rainLabel.setText(f"{next5DaysOfWeatherInfo[index].getRainSeverity()}")
            self.windSpeedLabel.setText(f"{next5DaysOfWeatherInfo[index].getWindSpeedSeverity()}")

            weatherIconPixmax = QtGui.QPixmap()
            weatherIconPixmax.loadFromData(next5DaysOfWeatherInfo[index].weatherIconImage)
            weatherIconPixmax = weatherIconPixmax.scaled(75, 75, QtCore.Qt.KeepAspectRatio)
            self.weatherIconLabel.setPixmap(weatherIconPixmax)