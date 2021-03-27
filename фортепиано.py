import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5 import QtCore, QtMultimedia


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('фортепиано.ui', self)

        self.do_1.clicked.connect(self.f1)
        self.re.clicked.connect(self.f2)
        self.mi.clicked.connect(self.f3)
        self.fa.clicked.connect(self.f4)
        self.sol.clicked.connect(self.f5)
        self.lya.clicked.connect(self.f6)
        self.si.clicked.connect(self.f7)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)

        self.player = QtMultimedia.QMediaPlayer()

        self.player.setMedia(content)

    def sound1(self):
        self.load_mp3('1.mp3')
        self.player.play()

    def sound2(self):
        self.load_mp3('2.mp3')
        self.player.play()

    def sound3(self):
        self.load_mp3('3.mp3')
        self.player.play()

    def sound4(self):
        self.load_mp3('4.mp3')
        self.player.play()

    def sound5(self):
        self.load_mp3('5.mp3')
        self.player.play()

    def sound6(self):
        self.load_mp3('6.mp3')
        self.player.play()

    def sound7(self):
        self.load_mp3('7.mp3')
        self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
