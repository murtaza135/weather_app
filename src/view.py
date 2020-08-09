from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.initMainWindow()
        self.initUI()

    def initMainWindow(self):
        self.setGeometry(200,200,750,750)
        # self.setMinimumWidth(250)
        # self.setMinimumHeight(250)
        self.setWindowTitle("Weather App")
        # self.setWindowIcon(QtGui.QIcon(""))
        # palette = self.palette()
        # palette.setColor(QtGui.QPalette.Background, QtGui.QColor(Qt.cyan))
        # self.setPalette(palette)
        # self.setAutoFillBackground(True)

    def initUI(self):
        # palette = QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.Background, QtGui.QColor(Qt.darkRed))


        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setSpacing(0)
        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.searchBox = QtWidgets.QLineEdit()
        self.searchBox.setStyleSheet("background-color: lightgreen")
        self.searchBox.setFixedHeight(25)
        print(self.searchBox.sizePolicy())
        print(self.searchBox.sizeHint())
        self.mainLayout.addWidget(self.searchBox, 0, 0, 1, 4, alignment=Qt.AlignTop)

        self.searchButton = QtWidgets.QPushButton(text="Search")
        self.searchButton.setStyleSheet("background-color: lightgreen")
        self.searchButton.setFixedHeight(25)
        self.mainLayout.addWidget(self.searchButton, 0, 5, alignment=Qt.AlignTop)

        layoutLeft = QtWidgets.QVBoxLayout()
        layoutLeft.setSpacing(0)
        self.mainLayout.addLayout(layoutLeft, 1, 0, 1, 2, alignment=Qt.AlignTop)

        self.locationTimeFrame = QtWidgets.QFrame()
        self.locationTimeFrame.setFixedHeight(45)
        layoutLeft.addWidget(self.locationTimeFrame, alignment=Qt.AlignTop)

        locationTimeLayout = QtWidgets.QVBoxLayout(self.locationTimeFrame)
        locationTimeLayout.setSpacing(0)

        self.locationLabel = QtWidgets.QLabel()
        self.locationLabel.setStyleSheet("background-color: lightgreen")
        self.locationLabel.setText("Location (0.00, 1.00)")
        self.locationLabel.setFixedHeight(15)
        locationTimeLayout.addWidget(self.locationLabel, alignment=Qt.AlignTop)

        self.timeLabel = QtWidgets.QLabel()
        self.timeLabel.setStyleSheet("background-color: lightgreen")
        self.timeLabel.setText("Time")
        self.timeLabel.setFixedHeight(15)
        locationTimeLayout.addWidget(self.timeLabel, alignment=Qt.AlignTop)

        self.weatherPicture = QtWidgets.QLabel()
        self.weatherPicture.setStyleSheet("background-color: lightgreen")
        self.weatherPicture.setPixmap(QtGui.QPixmap("../images/test1.png"))
        self.weatherPicture.setFixedHeight(60)
        layoutLeft.addWidget(self.weatherPicture, alignment=Qt.AlignTop)

        self.longDescriptionLabel = QtWidgets.QLabel()
        self.longDescriptionLabel.setStyleSheet("background-color: lightgreen")
        self.longDescriptionLabel.setText("Long Description of weather, this is a test text aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah")
        self.longDescriptionLabel.setFixedHeight(30)
        self.longDescriptionLabel.setWordWrap(True)
        layoutLeft.addWidget(self.longDescriptionLabel, alignment=Qt.AlignTop)

        # actualTempInCelcius
        # humidityPercent
        # windSpeedMph + windDirectionDegrees
        # cloudinessPercent
        # rainInMmForLast3Hours

        self.remainingWeatherInfoFrame = QtWidgets.QFrame()
        self.remainingWeatherInfoFrame.setFixedHeight(100)
        layoutLeft.addWidget(self.remainingWeatherInfoFrame, alignment=Qt.AlignTop)

        remainingWeatherInfoLayout = QtWidgets.QGridLayout(self.remainingWeatherInfoFrame)
        layoutLeft.setSpacing(0)

        self.actualTempInCelcius = QtWidgets.QLabel()
        self.actualTempInCelcius.setStyleSheet("background-color: lightgreen")
        self.actualTempInCelcius.setText("actualTempInCelcius")
        self.actualTempInCelcius.setFixedHeight(15)
        remainingWeatherInfoLayout.addWidget(self.actualTempInCelcius, alignment=Qt.AlignTop)

        self.humidityPercent = QtWidgets.QLabel()
        self.humidityPercent.setStyleSheet("background-color: lightgreen")
        self.humidityPercent.setText("humidityPercent")
        self.humidityPercent.setFixedHeight(15)
        remainingWeatherInfoLayout.addWidget(self.humidityPercent, alignment=Qt.AlignTop)

        self.windSpeedMphAndDirection = QtWidgets.QLabel()
        self.windSpeedMphAndDirection.setStyleSheet("background-color: lightgreen")
        self.windSpeedMphAndDirection.setText("windSpeedMphAndDirection")
        self.windSpeedMphAndDirection.setFixedHeight(15)
        remainingWeatherInfoLayout.addWidget(self.windSpeedMphAndDirection, alignment=Qt.AlignTop)

        self.cloudinessPercent = QtWidgets.QLabel()
        self.cloudinessPercent.setStyleSheet("background-color: lightgreen")
        self.cloudinessPercent.setText("cloudinessPercent")
        self.cloudinessPercent.setFixedHeight(15)
        remainingWeatherInfoLayout.addWidget(self.cloudinessPercent, alignment=Qt.AlignTop)

        self.rainInMmForLast3Hours = QtWidgets.QLabel()
        self.rainInMmForLast3Hours.setStyleSheet("background-color: lightgreen")
        self.rainInMmForLast3Hours.setText("rainInMmForLast3Hours")
        self.rainInMmForLast3Hours.setFixedHeight(15)
        remainingWeatherInfoLayout.addWidget(self.rainInMmForLast3Hours, alignment=Qt.AlignTop)