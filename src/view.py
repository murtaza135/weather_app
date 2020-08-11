from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/view.log")
file_handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d:%(levelname)s: %(message)s"))
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)



class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.initMainWindow()
        self.initUI()

    def initMainWindow(self):
        self.setGeometry(200,200,1250,750)
        self.setMinimumWidth(250)
        self.setMinimumHeight(250)
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QtGui.QIcon("../images/icon.ico"))
        self.setStyleSheet("background-color: #016bac")

    def initUI(self):
        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setHorizontalSpacing(7)
        self.mainLayout.setVerticalSpacing(25)
        self.mainLayout.setContentsMargins(25, 18, 25, 18)
        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.searchBox = QtWidgets.QLineEdit()
        self.searchBox.setStyleSheet("color: white;" "font-size: 24px;" "padding-left: 5px")
        self.mainLayout.addWidget(self.searchBox, 0, 0, 1, 4)

        self.searchButton = QtWidgets.QPushButton(text="Search")
        self.searchButton.setStyleSheet("background-color: #004c82;" "color: white;" "font-size: 24px;")
        self.searchButton.setMaximumHeight(33)
        self.mainLayout.addWidget(self.searchButton, 0, 4, 1, 1)

        layoutLeft = QtWidgets.QVBoxLayout()
        layoutLeft.setSpacing(0)
        self.mainLayout.addLayout(layoutLeft, 1, 0, 1, 2)

        locationTimeLayout = QtWidgets.QVBoxLayout()
        locationTimeLayout.setSpacing(0)
        layoutLeft.addLayout(locationTimeLayout)

        self.locationLabel = QtWidgets.QLabel()
        self.locationLabel.setStyleSheet("color: white;" "font-size: 32px;" "padding-left: 0px")
        # self.locationLabel.setText("Location (0.00, 1.00)")
        locationTimeLayout.addWidget(self.locationLabel)

        self.timeLabel = QtWidgets.QLabel()
        self.timeLabel.setStyleSheet("color: white; font-size: 16px; padding-left: 0px")
        # self.timeLabel.setText("3 hours ago")
        locationTimeLayout.addWidget(self.timeLabel)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        locationTimeLayout.addItem(spacer)

        pictureTempDescriptionLayout = QtWidgets.QGridLayout()
        pictureTempDescriptionLayout.setHorizontalSpacing(0)
        pictureTempDescriptionLayout.setVerticalSpacing(0)
        layoutLeft.addLayout(pictureTempDescriptionLayout)

        self.weatherPicture = QtWidgets.QLabel()
        # weatherPixmap = QtGui.QPixmap("../images/test1.png")
        # weatherPixmap = weatherPixmap.scaled(175, 175, QtCore.Qt.KeepAspectRatio)
        # self.weatherPicture.setPixmap(weatherPixmap)
        self.weatherPicture.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        pictureTempDescriptionLayout.addWidget(self.weatherPicture, 0, 0)

        self.actualTemperatureLabel = QtWidgets.QLabel()
        # self.actualTemperatureLabel.setText("13°C")
        self.actualTemperatureLabel.setStyleSheet("color: white; font-size: 40px; padding-left: 5px")
        pictureTempDescriptionLayout.addWidget(self.actualTemperatureLabel, 0, 1)

        self.longDescriptionLabel = QtWidgets.QLabel()
        # self.longDescriptionLabel.setText("Long Description of weather, this is a test text")
        self.longDescriptionLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.longDescriptionLabel.setWordWrap(True)
        pictureTempDescriptionLayout.addWidget(self.longDescriptionLabel, 1, 0, 1, 2)

        spacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        layoutLeft.addItem(spacer)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        layoutLeft.addWidget(line)

        spacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        layoutLeft.addItem(spacer)

        remainingWeatherInfoLayout = QtWidgets.QGridLayout()
        remainingWeatherInfoLayout.setSpacing(15)
        layoutLeft.addLayout(remainingWeatherInfoLayout)

        self.feelsLikeTemeperatureLabel = QtWidgets.QLabel()
        self.feelsLikeTemeperatureLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        # self.feelsLikeTemeperatureLabel.setText("Feels Like: 13°C")
        remainingWeatherInfoLayout.addWidget(self.feelsLikeTemeperatureLabel)

        self.humidityPercent = QtWidgets.QLabel()
        self.humidityPercent.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        # self.humidityPercent.setText("Humidity: 50%")
        remainingWeatherInfoLayout.addWidget(self.humidityPercent)

        self.windSpeedMphAndDirection = QtWidgets.QLabel()
        self.windSpeedMphAndDirection.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        # self.windSpeedMphAndDirection.setText("Wind Speed: 10mph NW")
        remainingWeatherInfoLayout.addWidget(self.windSpeedMphAndDirection)

        self.cloudinessPercent = QtWidgets.QLabel()
        self.cloudinessPercent.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        # self.cloudinessPercent.setText("Cloudiness: 20%")
        remainingWeatherInfoLayout.addWidget(self.cloudinessPercent)

        self.rainInMmForLast3Hours = QtWidgets.QLabel()
        self.rainInMmForLast3Hours.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        # self.rainInMmForLast3Hours.setText("Rain: Very High")
        remainingWeatherInfoLayout.addWidget(self.rainInMmForLast3Hours)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        layoutLeft.addItem(spacer)

        layoutRight = QtWidgets.QHBoxLayout()
        layoutRight.setSpacing(0)
        self.mainLayout.addLayout(layoutRight, 1, 2, 1, 3)

        spacer = QtWidgets.QSpacerItem(25, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        layoutRight.addItem(spacer)

        self.leftArrowPicture = QtWidgets.QLabel()
        leftArrowPixmap = QtGui.QPixmap("../images/back.png")
        leftArrowPixmap = leftArrowPixmap.scaled(25, 25, QtCore.Qt.KeepAspectRatio)
        self.leftArrowPicture.setPixmap(leftArrowPixmap)
        self.leftArrowPicture.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        layoutRight.addWidget(self.leftArrowPicture)
        self.leftArrowPicture.hide()

        self.specifiedHourWeatherInfoWidgets = [SpecifiedHourWeatherInfo() for _ in range(8)]
        for widget in self.specifiedHourWeatherInfoWidgets:
            layoutRight.addWidget(widget)

        self.rightArrowPicture = QtWidgets.QLabel()
        rightArrowPixmap = QtGui.QPixmap("../images/next.png")
        rightArrowPixmap = rightArrowPixmap.scaled(25, 25, QtCore.Qt.KeepAspectRatio)
        self.rightArrowPicture.setPixmap(rightArrowPixmap)
        self.rightArrowPicture.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        layoutRight.addWidget(self.rightArrowPicture)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacer, 2, 0)


class SpecifiedHourWeatherInfo(QtWidgets.QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        # self.timeText = timeText
        # self.weatherIconPath = weatherIconPath
        # self.temperatureText = temperatureText
        # self.cloudinessIconPath = cloudinessIconPath
        # self.cloudinessText = cloudinessText
        # self.rainIconPath = rainIconPath
        # self.rainText = rainText
        # self.windSpeedIconPath = windSpeedIconPath
        # self.windSpeedText = windSpeedText

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
        # self.timeLabel.setText("13:00")
        self.timeLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.timeLabel, 0, 1)

        self.weatherIconLabel = QtWidgets.QLabel()
        # weatherIconPixmax = QtGui.QPixmap("../images/test1.png")
        # weatherIconPixmax = weatherIconPixmax.scaled(75, 75, QtCore.Qt.KeepAspectRatio)
        # self.weatherIconLabel.setPixmap(weatherIconPixmax)
        self.weatherIconLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.weatherIconLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.weatherIconLabel, 1, 1)

        self.temperatureLabel = QtWidgets.QLabel()
        self.temperatureLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 12px")
        # self.temperatureLabel.setText("16°C")
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
        # self.cloudinessLabel.setText("23%")
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
        self.rainLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 7px")
        # self.rainLabel.setText("Heavy")
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
        self.windSpeedLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 6px")
        # self.windSpeedLabel.setText("20mph")
        self.windSpeedLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        windSpeedLayout.addWidget(self.windSpeedLabel)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacer, 6, 0)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addItem(spacer, 0, 2, 7, 1)