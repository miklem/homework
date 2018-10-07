from PySide.QtCore import *
from PySide.QtGui import *
import math
import calculator_uis as ui


class calcClass(QMainWindow, ui.Ui_calc_ManWindow):
    temp_A = None
    temp_B = None
    operation = None
    result = False
    clearDigit = False

    opfirst = ["1/", "sqrt>"]

    def __init__(self):
        super(calcClass, self).__init__()
        self.setupUi(self)
        self.history_lb.setText("")

        # connect numbers
        self.b1_btn.clicked.connect(lambda: self.addNumber(str(1)))
        self.b2_btn.clicked.connect(lambda: self.addNumber(str(2)))
        self.b3_btn.clicked.connect(lambda: self.addNumber(str(3)))
        self.b4_btn.clicked.connect(lambda: self.addNumber(str(4)))
        self.b5_btn.clicked.connect(lambda: self.addNumber(str(5)))
        self.b6_btn.clicked.connect(lambda: self.addNumber(str(6)))
        self.b7_btn.clicked.connect(lambda: self.addNumber(str(7)))
        self.b8_btn.clicked.connect(lambda: self.addNumber(str(8)))
        self.b9_btn.clicked.connect(lambda: self.addNumber(str(9)))
        self.b0_btn.clicked.connect(lambda: self.addNumber(str(0)))
        self.dot_btn.clicked.connect(lambda: self.addNumber("."))

        # connect operations
        self.plus_btn.clicked.connect(lambda: self.addOperator("+"))
        self.minus_btn.clicked.connect(lambda: self.addOperator("-"))
        self.mul_btn.clicked.connect(lambda: self.addOperator("x"))
        self.div_btn.clicked.connect(lambda: self.addOperator("/"))
        self.pow_btn.clicked.connect(lambda: self.addOperator("^"))
        self.divx_btn.clicked.connect(lambda: self.addOperator("1/"))
        self.sqrt_btn.clicked.connect(lambda: self.addOperator("sqrt>"))
        self.percent_btn.clicked.connect(lambda: self.addOperator("%"))
        self.neg_btn.clicked.connect(lambda: self.addOperator("+-"))
        self.result_btn.clicked.connect(lambda: self.addOperator("="))
        self.clear_btn.clicked.connect(self.clear)

    def clear(self):
        self.temp_A = None
        self.temp_B = None
        self.operation = None
        self.result = False
        self.clearDigit = False
        self.history_lb.setText("")
        self.digit_le.setText("")

    def addNumber(self, character):
        if self.clearDigit:
            self.digit_le.setText("")
            self.clearDigit = False
        temp = self.digit_le.text() + character
        self.digit_le.setText(temp)

    def addOperator(self, operator):
        if self.digit_le.text() != "":
            if self.temp_A is None:
                self.temp_A = float(self.digit_le.text())
            else:
                self.temp_B = float(self.digit_le.text())
        else:
            self.temp_A = self.result
        self.addHistory(self.checkOrder(operator))

        if self.operation == "+":
            self.doSum()
        elif self.operation == "-":
            self.doSubstract()
        elif self.operation == "x":
            self.doMul()
        elif self.operation == "/":
            self.doDiv()
        elif self.operation == "^":
            self.doPow()
        elif self.operation == "sqrt>":
            self.doSqrt()
        elif self.operation == "1/":
            self.doDivx()
        elif self.operation == "+-":
            self.doNeg()
        elif self.operation == "%":
            self.doPercent()

        if operator == "=":

            self.addHistory(str(self.temp_A) + " | ")
            self.digit_le.setText("")
            self.result = self.temp_A
            self.temp_A, self.temp_B = None, None

        self.operation = operator
        self.clearDigit = True

    # decorates operational functions for proper trimming and output
    def outputTrimDecorator(func):
        def wrapper(self):
            result = func(self)
            self.temp_A = self.trim(result)
            self.digit_le.setText(str(self.temp_A))
        return wrapper

    # operations itself
    @outputTrimDecorator
    def doSum(self):
        self.temp_A = self.temp_A + self.temp_B
        return self.temp_A

    @outputTrimDecorator
    def doSubstract(self):
        return self.temp_A - self.temp_B

    @outputTrimDecorator
    def doMul(self):
        return self.temp_A * self.temp_B

    @outputTrimDecorator
    def doDiv(self):
        return self.temp_A / self.temp_B

    @outputTrimDecorator
    def doPow(self):
        self.temp_A = math.pow(self.temp_A, self.temp_B)
        return self.convertFromString(str(self.temp_A))

    @outputTrimDecorator
    def doSqrt(self):
        return math.sqrt(self.temp_A)

    @outputTrimDecorator
    def doDivx(self):
        return (1 / self.temp_A)

    @outputTrimDecorator
    def doNeg(self):
        return self.temp_A * -1

    @outputTrimDecorator
    def doPercent(self):
        return (self.temp_A * self.temp_B) / 100

    def checkOrder(self, operator):
        if operator not in self.opfirst:
            return self.digit_le.text() + operator
        else:
            return operator + self.digit_le.text() + ">>{0}".format(operator)

    def addHistory(self, history):
        self.history_lb.setText(self.history_lb.text() + history)

    def trim(self, value):
        try:
            temp = str(value)
            a, b = temp.split('.')
            if b == "0":
                return int(a)
            else:
                return float(temp)
        except:
            print "error in trim() func"

    def convertFromString(self, convFrom=""):
        if convFrom != "":
            if "." not in convFrom:
                return int(convFrom)

            else:
                a, b = convFrom.split('.')
                if b == "0":
                    return int(a)
                else:
                    return float(convFrom)
        else:
            return "None"


if __name__ == '__main__':
    app = QApplication([])
    w = calcClass()
    w.show()
    app.exec_()
