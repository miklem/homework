# square = w * h
# circle = pi**2 * r

from PySide.QtCore import *
from PySide.QtGui import *
import computerArea_uis as ui
import math 


class computeAreaClass(QMainWindow, ui.Ui_computerArea):
    def __init__(self):
        super(computeAreaClass, self).__init__()
        self.setupUi(self)
        self.compute()
        self.ci_grpb.setVisible(self.shape_cbb.currentIndex()==1)
        #variables
        self.live = False
        #connects
        self.shape_cbb.currentIndexChanged.connect(self.updateUI)
        self.compute_btn.clicked.connect(self.compute)
        if self.live:
            self.compute_btn.setVisible(0)
            self.sq_height_spb.valueChanged.connect(self.compute)
            self.sq_width_spb.valueChanged.connect(self.compute)
            self.ci_radius_spb.valueChanged.connect(self.compute)


    def updateUI(self):
        self.sq_grpb.setVisible(self.shape_cbb.currentIndex()==0)
        self.ci_grpb.setVisible(self.shape_cbb.currentIndex()==1)
        self.compute()

    def compute(self):
        if self.shape_cbb.currentIndex() == 0:
            self.computeSquare()
        if self.shape_cbb.currentIndex() == 1:
            self.computeCircle()
    
    def computeSquare(self):
        w = self.sq_width_spb.value()
        h = self.sq_height_spb.value()
        self.showResult(w*h)

    def computeCircle(self):
        radius = self.ci_radius_spb.value()
        self.showResult(math.pi*(radius**2))
        
    def showResult(self, val):
        self.result_lbl.setText("Result: %.3f" % val)

if __name__ == '__main__':
    app = QApplication([])
    w = computeAreaClass()
    w.show()
    app.exec_()
