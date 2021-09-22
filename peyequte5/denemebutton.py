# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:17:10 2021

@author: durdu
"""



from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout,QTableWidgetItem
import sys
from Ui_tabloqt import Ui_MainWindow
import pandas as pd

class myApp(QtWidgets.QMainWindow):
    def __init__(self):                     
        super(myApp, self).__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        
        
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        
        
        self.ui.pushButton.clicked.connect(lambda _, xl_path="trendyol_telefon.xlsx", 
                                sheet_name=worksheet_name: self.loadExcelData(xl_path, sheet_name))
        
        
        
        
        
        self.ui.pushButton_2.clicked.connect(lambda _,
        xl_path= excel_file_path, sheet_name=worksheet_name: self.loadExcelData(xl_path, sheet_name))
        
        
        
        self.ui.pushButton_3.clicked.connect(lambda _, xl_path="trendyol_esofman.xlsx",
                            sheet_name=worksheet_name: self.loadExcelData(xl_path, sheet_name))
        
        self.ui.pushButton_4.clicked.connect(lambda _, xl_path="ayakkabi.xlsx",
                            sheet_name=worksheet_name: self.loadExcelData(xl_path, sheet_name))


    def loadExcelData(self, excel_file_dir, worksheet_name):
        
        
        df = pd.read_excel(excel_file_dir, worksheet_name)
        if df.size == 0:
            
            
            return

        df.fillna('', inplace=True)
        self.ui.tableWidget.setRowCount(df.shape[0])
        self.ui.tableWidget.setColumnCount(df.shape[1])
        self.ui.tableWidget.setHorizontalHeaderLabels(df.columns)

        # pandas dizi nesnesini dönderiyor
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = "{:.2f}".format(value)
                tableItem = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row[0], col_index, tableItem)

        self.ui.tableWidget.setColumnWidth(10, 10)# 2, 300   
        
        
    
     

    
excel_file_path = 'trendyol_tablet.xlsx'
worksheet_name = 'Sheet1'



def app():
  
    app = QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())




app()






        
