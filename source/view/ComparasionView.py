from PyQt5.QtWidgets import QGridLayout,QComboBox, QPushButton,QLabel, QWidget, QErrorMessage, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import  QtCore
from presenter.cPresenter import ComparasionPresenter
from PyQt5.QtCore import Qt
from view.IView import IView

class ComparasionView(IView):
    BUTTON_COLOR = "white"
    FRAME_COLOR = "#bababa"
    START = "Старт"
    WARNING_START = "Данное действие выполнить невозможно, дождитесь окончания сегментации системы на главной вкладке"
    WARNING = "Пердупреждение"

    def __init__(self, model):
        self.segmentationStarted = False
        self.leftComboBox = QComboBox()
        self.rightComboBox = QComboBox()
        self.leftComboBox.activated[str].connect(self.onSelectedLeftComboBox)
        self.leftComboBox.activated[str].connect(self.onSelectedRightComboBox)

        self.startButton = QPushButton(self.START)
        self.startButton.clicked.connect(self.startButtonClicked)
        self.startButton.setStyleSheet("background:"+self.BUTTON_COLOR)

        self.leftMediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.leftVideoWidget = QVideoWidget()        
        self.leftVideoWidget.setMaximumWidth(880)
        self.leftVideoWidget.setMaximumHeight(320)

        self.leftVideoWidget.setStyleSheet("background:"+self.FRAME_COLOR)
        self.leftMediaplayerWidget = QWidget() 

        self.textBoxLeftVideoName = QLabel("")
        self.textBoxLeftVideoName.setAlignment(QtCore.Qt.AlignHCenter)

        layout = QGridLayout()
        layout.addWidget(self.leftVideoWidget,0,0,6,6)
        layout.addWidget(self.textBoxLeftVideoName,6,0,1,6,Qt.AlignmentFlag.AlignCenter)
        self.leftMediaplayerWidget.setLayout(layout)
        self.leftMediaplayer.setVideoOutput(self.leftVideoWidget)

        self.rightMediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.rightVideoWidget = QVideoWidget()
        self.rightVideoWidget.setMaximumWidth(880)
        self.rightVideoWidget.setMaximumHeight(320)
        self.rightVideoWidget.setStyleSheet("background:"+self.FRAME_COLOR)
        self.rightMediaplayerWidget = QWidget()

        self.textBoxRightVideoName = QLabel("")
        self.textBoxRightVideoName.setAlignment(QtCore.Qt.AlignHCenter)

        layout = QGridLayout()
        layout.addWidget(self.rightVideoWidget,0,0,6,6)
        layout.addWidget(self.textBoxRightVideoName,6,0,1,6,Qt.AlignmentFlag.AlignCenter)
        self.rightMediaplayerWidget.setLayout(layout)
        self.rightMediaplayer.setVideoOutput(self.rightVideoWidget)

        self.textBoxForLeftResults = QLabel("")
        self.textBoxForLeftResults.setAlignment(QtCore.Qt.AlignHCenter)

        self.textBoxForRightResults = QLabel("")
        self.textBoxForRightResults.setAlignment(QtCore.Qt.AlignHCenter)

        self.cPresenter =  ComparasionPresenter(self,model)

    def runDefaultState(self):
        self.leftComboBox.clear()
        self.rightComboBox.clear()
        self.textBoxLeftVideoName.setText("")
        self.textBoxRightVideoName.setText("")
        self.textBoxForLeftResults.setText("")
        self.textBoxForRightResults.setText("")
        self.segmentationStarted = False
    
    def onSelectedLeftComboBox(self):
        self.leftSystemName = self.leftComboBox.currentText()

    def onSelectedRightComboBox(self):
        self.rightSystemName = self.rightComboBox.currentText()

    def startButtonClicked(self):
        if(not self.segmentationStarted):   
            self.cPresenter.onStartButtonClick()
        else:
            warningMessage = QMessageBox()
            warningMessage.setWindowTitle(self.WARNING)
            warningMessage.setText(self.WARNING_START)
            warningMessage.setIcon(QMessageBox.Warning)
            warningMessage.setStandardButtons(QMessageBox.Close)
            warningMessage.exec_()
        
