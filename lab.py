import gui
import sys
import requests  #用於發送REST API
from requests.auth import HTTPBasicAuth
import json  #解析json
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *

Ui_MainWindow = gui.Ui_Dialog
params = {}
auth = {'admin', 'admin'}
url = 'http://140.116.247.69:8282/~/mn-cse/mn-name/Air_Conditioner'

fan_speed_status = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.binding_ui()
        self.set_fan_movie

    def get_status_(self):
        global fan_speed_status
        r = requests.post(url,
                          auth=HTTPBasicAuth('admin', 'admin'),
                          params={'op': 'get_state'})
        temp = r.text.split(',')[1]
        fan_speed_status = int(r.text.split(',')[2])
        self.lcdNumber.display(temp)
        self.set_fan_movie(fan_speed_status)
        print("fan_speed_stauts = ", fan_speed_status)

    def set_fan_movie(self, fan_speed_status_):
        movie = QMovie('./source (1).gif')
        movie.setCacheMode(QMovie.CacheAll)
        movie.setScaledSize(self.movie_screen.size())
        self.movie_screen.setMovie(movie)
        print("set_fan_movie status = ", fan_speed_status_)
        if (fan_speed_status_ == 1):
            print("Change Speed 30")
            movie.setSpeed(30)
        elif (fan_speed_status_ == 2):
            print("Change Speed 150")
            movie.setSpeed(150)
        else:
            print("Change Speed 500")
            movie.setSpeed(500)
        movie.start()

    def binding_ui(self):
        #設置GIF
        self.fan_minus.clicked.connect(self.set_fan_minus)
        self.fan_plus.clicked.connect(self.set_fan_plus)
        self.tmp_minus.clicked.connect(self.set_tmp_minus)
        self.tmp_plus.clicked.connect(self.set_tmp_plus)
        self.get_status.clicked.connect(self.get_status_)

    def set_tmp_minus(self):
        my_params = {'op': 'set_temp', 'value': 'minus'}
        r = requests.post(url,
                          params=my_params,
                          auth=HTTPBasicAuth('admin', 'admin'))

    def set_tmp_plus(self):
        my_params = {'op': 'set_temp', 'value': 'plus'}
        r = requests.post(url,
                          params=my_params,
                          auth=HTTPBasicAuth('admin', 'admin'))

    def set_fan_minus(self):
        my_params = {'op': 'set_fan', 'value': 'minus'}
        r = requests.post(url,
                          params=my_params,
                          auth=HTTPBasicAuth('admin', 'admin'))

        if (r.status_code == 200):
            global fan_speed_status
            fan_speed_status -= 1
            self.set_fan_movie(fan_speed_status)  #0代表減速
            print("Response 200")
        else:
            print("Bad Request")

    def set_fan_plus(self):
        my_params = {'op': 'set_fan', 'value': 'plus'}
        r = requests.post(url,
                          params=my_params,
                          auth=HTTPBasicAuth('admin', 'admin'))

        if (r.status_code == 200):
            global fan_speed_status
            fan_speed_status += 1
            self.set_fan_movie(fan_speed_status)  #1代表加速
            print("Response 200")
        else:
            print('Bad Request')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())