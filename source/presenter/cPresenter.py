from model.wrapper.Wrapper import Wrapper
from presenter.IPresenter import IPresenter

class ComparasionPresenter(IPresenter):

    def __init__(self, cView, model:Wrapper):
        self.cView = cView
        self.model = model

    def onStartButtonClick(self):
        #для выбранной левой системы
        leftSystem = self.cView.leftComboBox.currentText()
        videoPath = self.model.resultDictionary.get(leftSystem+"_videoPath") 
        self.cView.runVideo(videoPath,self.cView.leftMediaplayer)
        self.cView.displayText(self.model.parseFrameCount(leftSystem) + self.model.parseTime(leftSystem), self.cView.textBoxForLeftResults)
        shortLeftVideoName = self.model.getShortFileName(videoPath)
        self.cView.displayText(shortLeftVideoName, self.cView.textBoxLeftVideoName)
        self.cView.runVideo(videoPath, self.cView.leftMediaplayer)

        
        #для выбранной правой системы
        rightSystem = self.cView.rightComboBox.currentText()
        videoPath = self.model.resultDictionary.get(rightSystem+"_videoPath")
        self.cView.runVideo(videoPath, self.cView.rightMediaplayer)
        self.cView.displayText(self.model.parseFrameCount(leftSystem) + self.model.parseTime(rightSystem), self.cView.textBoxForRightResults)
        shortRightVideoName = self.model.getShortFileName(videoPath)
        self.cView.displayText(shortRightVideoName, self.cView.textBoxRightVideoName)

  