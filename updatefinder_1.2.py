import time
import os
import re
import sys
from PyQt5.QtWidgets import (QWidget, QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication, QPushButton, QLineEdit)

# Define source folder

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

# Button and field Source Directory
        self.btn1 = QPushButton('Source Directory', self)
        self.btn1.move(20, 20)
        self.btn1.clicked.connect(self.getSourcePath)
        self.source_folder = ''

        self.source_dir_txt = QLineEdit(self)
        self.source_dir_txt.move(130, 22)
        self.source_dir_txt.setGeometry(130, 22, 500, 25)

# Button and field Result Directory
        self.btn2 = QPushButton('Results Directory', self)
        self.btn2.move(20, 60)
        self.btn2.clicked.connect(self.getResultPath)
        self.dstdir = ''

        self.result_dir_txt = QLineEdit(self)
        self.result_dir_txt.move(130, 22)
        self.result_dir_txt.setGeometry(130, 62, 500, 25)

# Period

        self.start_year = QLineEdit(self)
        self.start_year.move(130, 22)
        self.start_year.setGeometry(130, 102, 500, 25)

        self.start_month = QLineEdit(self)
        self.start_month.move(130, 22)
        self.start_month.setGeometry(130, 62, 500, 25)


        self.end_year = QLineEdit(self)
        self.end_year.move(130, 22)
        self.end_year.setGeometry(130, 62, 500, 25)

        self.end_month = QLineEdit(self)
        self.end_month.move(130, 22)
        self.end_month.setGeometry(130, 62, 500, 25)


# Button Run
        self.btn3 = QPushButton('Run', self)
        self.btn3.move(20, 100)
        self.btn3.clicked.connect(self.runButton)

        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.getSourcePath)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 750, 300)
        self.setWindowTitle('Update Finder 2.0')
        self.show()


    def getSourcePath(self):
        fname = QFileDialog.getExistingDirectory(self, 'Open file', '')
        self.source_dir_txt.setText(str(fname))
        self.source_folder = str(fname)

    def getResultPath(self):
        fname = QFileDialog.getExistingDirectory(self, 'Open file', '')
        self.result_dir_txt.setText(str(fname))

'''
    def runButton(self):


start_year = int(input("Enter period start Year (yyyy): "))
start_month = int(input("Enter period start Month (m): "))
print("=================================================================================")
print("WARNING: Dates from End Period month and older will not be included to te results")
print("=================================================================================")
end_year = int(input("Enter period end Year (yyyy): "))
end_month = int(input("Enter period end Month (m): "))

start_time_tuple = (start_year, start_month, 1, 0, 0, 0, 0, 0, 0)
start_timestamp = time.mktime(start_time_tuple)

end_time_tuple = (end_year, end_month, 1, 0, 0, 0, 0, 0, 0)
end_timestamp = time.mktime(end_time_tuple)

# Create a set which includes updated directories
updated_folders = set()

# Find all directories with updates and put them to the set
for top, dirs, files in os.walk(source_folder):
    for nm in files:
        if ((end_timestamp > os.path.getmtime(os.path.join(top, nm)) > start_timestamp) or (end_timestamp > os.path.getmtime(top) > start_timestamp)) and not re.match(r"(.+)nfo$", nm):
            if ((os.path.dirname(top)).replace("\\", '/') in updated_folders) or ((os.path.dirname(os.path.dirname(top))).replace("\\", '/') in updated_folders) or ((os.path.dirname(os.path.dirname(os.path.dirname(top)))).replace("\\", '/') in updated_folders):
                break
            else:
                for i in updated_folders:
                    if top == os.path.dirname(i) or top == os.path.dirname(os.path.dirname(i)) or top == os.path.dirname(os.path.dirname(os.path.dirname(i))):
                        updated_folders.remove(i)
                    else:
                        break
                updated_folders.add(top.replace("\\", '/'))


# Delete advertisement from directories with updates
for i in updated_folders:
    if os.path.exists(i + "/www.SamLab.ws.url"):
        os.remove(i + "/www.SamLab.ws.url")
        print(i + "/www.SamLab.ws.url " + " Advertisement is found and DELETED!")

# Create a folder for RAR archives
if not os.path.exists(dstdir):
    os.mkdir(dstdir)

print(str(len(updated_folders)) + " archives with updated data will be created...")

# Create RAR archives
k = 0
for i in updated_folders:
    k += 1
    source = str(i)
    rar_name = source[(len(source_folder)+1):].replace("/", "_")
    dst = dstdir + os.sep + rar_name + '.rar'
    rar = rar_path + "/WinRAR.exe u -as -dh -ep1 {0} {1}".format(dst, source)
    if os.system(rar)==0:
        print(str(k) + " from " + str(len(updated_folders)) + " RAR is created in " + str(dst))
    else:
        print('RAR creating is FAILED')

print ("PROCESS FINISHED")

'''

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())