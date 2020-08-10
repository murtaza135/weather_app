from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.initMainWindow()
        self.initUI()

    def initMainWindow(self):
        self.setGeometry(200,200,1250,750)
        # self.setMinimumWidth(250)
        # self.setMinimumHeight(250)
        self.setWindowTitle("Weather App")
        # self.setWindowIcon(QtGui.QIcon(""))
        # self.setStyleSheet("background: url(../images/taylor-van-riper-yQorCngxzwI-unsplash.jpg) 0 0 0 0 stretch stretch")
        self.setStyleSheet("background-color: #016bac")
        self.setAutoFillBackground(True)

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
        self.searchButton.setStyleSheet("color: white;" "font-size: 24px;")
        self.mainLayout.addWidget(self.searchButton, 0, 5)

        layoutLeft = QtWidgets.QVBoxLayout()
        layoutLeft.setSpacing(0)
        self.mainLayout.addLayout(layoutLeft, 1, 0, 1, 2)

        locationTimeLayout = QtWidgets.QVBoxLayout()
        locationTimeLayout.setSpacing(0)
        layoutLeft.addLayout(locationTimeLayout)

        self.locationLabel = QtWidgets.QLabel()
        self.locationLabel.setStyleSheet("color: white;" "font-size: 32px;" "padding-left: 0px")
        self.locationLabel.setText("Location (0.00, 1.00)")
        locationTimeLayout.addWidget(self.locationLabel)

        self.timeLabel = QtWidgets.QLabel()
        self.timeLabel.setStyleSheet("color: white; font-size: 16px; padding-left: 0px")
        self.timeLabel.setText("3 hours ago")
        locationTimeLayout.addWidget(self.timeLabel)

        pictureTempDescriptionLayout = QtWidgets.QGridLayout()
        pictureTempDescriptionLayout.setHorizontalSpacing(0)
        pictureTempDescriptionLayout.setVerticalSpacing(8)
        layoutLeft.addLayout(pictureTempDescriptionLayout)

        self.weatherPicture = QtWidgets.QLabel()
        self.weatherPicture.setPixmap(QtGui.QPixmap("../images/test1.png"))
        self.weatherPicture.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        pictureTempDescriptionLayout.addWidget(self.weatherPicture, 0, 0)

        self.actualTemperatureLabel = QtWidgets.QLabel()
        self.actualTemperatureLabel.setText("13°C")
        self.actualTemperatureLabel.setStyleSheet("color: white; font-size: 32px")
        pictureTempDescriptionLayout.addWidget(self.actualTemperatureLabel, 0, 1)

        self.longDescriptionLabel = QtWidgets.QLabel()
        self.longDescriptionLabel.setText("Long Description of weather, this is a test text")
        self.longDescriptionLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.longDescriptionLabel.setWordWrap(True)
        pictureTempDescriptionLayout.addWidget(self.longDescriptionLabel, 1, 0, 1, 2)

        spacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        layoutLeft.addItem(spacer)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setStyleSheet("color: white")
        layoutLeft.addWidget(line)

        spacer = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        layoutLeft.addItem(spacer)

        remainingWeatherInfoLayout = QtWidgets.QGridLayout()
        remainingWeatherInfoLayout.setSpacing(15)
        layoutLeft.addLayout(remainingWeatherInfoLayout)

        self.feelsLikeTemeperatureLabel = QtWidgets.QLabel()
        self.feelsLikeTemeperatureLabel.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.feelsLikeTemeperatureLabel.setText("Feels Like: 13°C")
        remainingWeatherInfoLayout.addWidget(self.feelsLikeTemeperatureLabel)

        self.humidityPercent = QtWidgets.QLabel()
        self.humidityPercent.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.humidityPercent.setText("Humidity: 50%")
        remainingWeatherInfoLayout.addWidget(self.humidityPercent)

        self.windSpeedMphAndDirection = QtWidgets.QLabel()
        self.windSpeedMphAndDirection.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.windSpeedMphAndDirection.setText("Wind Speed: 10mph NW")
        remainingWeatherInfoLayout.addWidget(self.windSpeedMphAndDirection)

        self.cloudinessPercent = QtWidgets.QLabel()
        self.cloudinessPercent.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.cloudinessPercent.setText("Cloudiness: 20%")
        remainingWeatherInfoLayout.addWidget(self.cloudinessPercent)

        self.rainInMmForLast3Hours = QtWidgets.QLabel()
        self.rainInMmForLast3Hours.setStyleSheet("color: white; font-size: 20px; padding-left: 0px")
        self.rainInMmForLast3Hours.setText("Rain: Very High")
        remainingWeatherInfoLayout.addWidget(self.rainInMmForLast3Hours)

        spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacer, 2, 0)