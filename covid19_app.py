from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import sys 
from covid19 import get_data,get_columns
MainUI, _ = loadUiType('covid19_d.ui')

class MainApp(QMainWindow, MainUI):
    def __init__(self):
        super(MainApp, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.data,self.total,self.death,self.active_c,self.recovred,self.closed_c = get_data()
        self.columns = get_columns()
        self.columns = self.columns[1:]
        self.tableWidget.setColumnCount(len(self.columns))
        self.tableWidget.setRowCount(len(self.data))
        self.init_table()
        self.init_label()
        
    def init_table(self):
        for i in range(0,len(self.columns)) :
            item = QtWidgets.QTableWidgetItem(self.columns[i])
            self.tableWidget.setHorizontalHeaderItem(i, item)
            
        for i in range(0,len(self.data)) :
            for a in range(0,len(self.columns)) :
                self.tableWidget.setItem(i,a, QTableWidgetItem(self.data[i][a]))
                
    def init_label(self):
        self.label.setText(f"Total cases : {self.total}")
        self.label_2.setText(f"death : {self.death}")
        self.label_3.setText(f"Recovered : {self.recovred}")
        self.label_4.setText(f"Active Cases : {self.active_c}")
        self.label_5.setText(f"Closed Cases : {self.closed_c}")

def main():
    app = QApplication(sys.argv)
    windows = MainApp()
    windows.show()
    app.exec_()


if __name__ == '__main__':
    main()
