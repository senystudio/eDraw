import sys
import utils
from DBCon import DBCon
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWinExtras import QtWin  # !!!


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        myappid = 'senn1x.PyDraw.Drawing.1'
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
        # setting title
        self.setWindowTitle("eDraw")
        self.setCursor(QCursor(Qt.CrossCursor))
        self.setFixedSize(1280, 720)
        self.setWindowIcon(QIcon('web.ico'))
        self.image = QImage(self.size(), QImage.Format_RGB32)

        self.image.fill(Qt.white)


        self.drawing = False
        self.brushSize = 3
        self.brushColor = Qt.black
        self._clear_size = 20



        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        mainMenu.setCursor(QCursor(Qt.PointingHandCursor))

        fileMenu = mainMenu.addMenu("Файл")

        kistMenu = mainMenu.addMenu("Кисть")
        kistMode = kistMenu.addMenu("Режим")

        kistXuy = QAction("Кисть", self)
        kistMode.addAction(kistXuy)
        kistXuy.triggered.connect(self.blackColor)

        kistPizda = QAction("Ластик", self)
        kistMode.addAction(kistPizda)
        kistPizda.triggered.connect(self.whiteColor)

        b_size = kistMenu.addMenu("Размер")


        b_color = kistMenu.addMenu("Цвет")

        pal_col = QAction("Палитра цветов...", self)
        b_color.addAction(pal_col)
        pal_col.triggered.connect(self.colKist)

        bckgrnd = mainMenu.addMenu("Заливка фона")

        saveAction = QAction("Сохранить как...", self)
        saveAction.setShortcut("Ctrl + S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction("Очистить холст", self)
        clearAction.setShortcut("Ctrl + C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        pal_bknd = QAction("Палитра цветов...", self)
        bckgrnd.addAction(pal_bknd)
        pal_bknd.triggered.connect(self.run)


        pix_3 = QAction("3px", self)
        b_size.addAction(pix_3)
        pix_3.triggered.connect(self.Pixel_3)

        # similarly repeating above steps for different sizes
        pix_6 = QAction("6px", self)
        b_size.addAction(pix_6)
        pix_6.triggered.connect(self.Pixel_6)

        pix_9 = QAction("9px", self)
        b_size.addAction(pix_9)
        pix_9.triggered.connect(self.Pixel_9)

        pix_12 = QAction("12px", self)
        b_size.addAction(pix_12)
        pix_12.triggered.connect(self.Pixel_12)

        pix_16 = QAction("16px", self)
        b_size.addAction(pix_16)
        pix_16.triggered.connect(self.Pixel_16)

        pix_20 = QAction("20px", self)
        b_size.addAction(pix_20)
        pix_20.triggered.connect(self.Pixel_20)

        # black = QAction("Черный", self)
        # # adding this action to the brush colors
        # kistXuy.addAction(black)
        # # adding methods to the black
        # black.triggered.connect(self.kist)
        black = QAction("Черный", self)
        b_color.addAction(black)
        black.triggered.connect(self.blackColor)

        white = QAction("Белый", self)
        b_color.addAction(white)
        white.triggered.connect(self.whiteColor)

        green = QAction("Зеленый", self)
        b_color.addAction(green)
        green.triggered.connect(self.greenColor)

        yellow = QAction("Желтый", self)
        b_color.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)

        red = QAction("Красный", self)
        b_color.addAction(red)
        red.triggered.connect(self.redColor)

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):

        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)

            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))


            painter.drawLine(self.lastPoint, event.pos())

            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)

        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)
        DBCon().add_record(filePath)


    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    # def lastik(self):
    #     self.erase()
    # methods for changing pixel sizes
    def Pixel_3(self):
        self.brushSize = 3

    def Pixel_6(self):
        self.brushSize = 6

    def Pixel_9(self):
        self.brushSize = 9

    def Pixel_12(self):
        self.brushSize = 12

    def Pixel_16(self):
        self.brushSize = 16

    def Pixel_20(self):
        self.brushSize = 20



    def run(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.image.fill(color)


    def colKist(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.brushColor = color

    # def lastik(self):
    #     self.brushColor = Qt.transparent




    def blackColor(self):
        self.brushColor = Qt.black

    def whiteColor(self):
        self.brushColor = Qt.white

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow

    def redColor(self):
        self.brushColor = Qt.red



if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    window.setWindowIcon(QIcon('web.ico'))
    window.show()
    sys.exit(App.exec())
