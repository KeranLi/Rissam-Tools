# -*- coding: utf-8 -*-
# @Author  : Keran Li

from PyQt5 import QtWidgets, QtCore
from ui.plane_plorized_dock import Ui_MainWindow
from PyQt5.QtGui import QPixmap

class PlanePlorizedDockWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, mainwindow):
        super(PlanePlorizedDockWidget, self).__init__()
        self.mainwindow = mainwindow
        self.setupUi(self)
        self.setWindowTitle("Plane and Plorized Images")

    def set_images(self, plane_image_path, plorized_image_path):
        # 获取dock的高度
        dock_height = self.height()
        print('This height of the dock is {}'.format(dock_height))

        # 加载图像
        plane_pixmap = QPixmap(plane_image_path)
        plorized_pixmap = QPixmap(plorized_image_path)

        # 计算缩放比例
        scale_ratio = dock_height / max(plane_pixmap.height(), plorized_pixmap.height())
        print('This scale ratio is {}'.format(scale_ratio))

        # 使用缩放比例来调整图像的大小
        plane_pixmap = plane_pixmap.scaled(plane_pixmap.width() * scale_ratio, plane_pixmap.height() * scale_ratio)
        plorized_pixmap = plorized_pixmap.scaled(plorized_pixmap.width() * scale_ratio, plorized_pixmap.height() * scale_ratio)

        # 设置QLabel的Pixmap
        self.imageLabel1.setPixmap(plane_pixmap)
        self.imageLabel2.setPixmap(plorized_pixmap)

        # 将QLabel的内容居中对齐
        self.imageLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel2.setAlignment(QtCore.Qt.AlignCenter)

        # 将QLabel的内容缩放以填充整个QLabel
        self.imageLabel1.setScaledContents(True)
        self.imageLabel2.setScaledContents(True)

