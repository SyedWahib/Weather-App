import os
import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

"""api_key= os.getenv("ApiKeyForWeatherApp")

city_name=input("Enter the name of the city you want to find the weather for: ")

url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

data= requests.get(url)"""

#print(data.status_code)

#print(data.json()['weather'][0]['description'])

#print(data.json())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather Report")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon(r"Assets\Icon.png"))
        self.setStyleSheet("""background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                            stop:0 hsl(231, 79%, 53%), stop:1 hsl(231, 100%, 40%));""")

        self.center()

        self.city_name= QLineEdit(self)
        self.submit_button=QPushButton("Submit", self)
        self.submit_button.setObjectName("submit_button")

        self.initUI()


    def initUI(self):

        self.city_name.setFont(QFont("Inter", 10))
        self.city_name.setGeometry(10, 20, 200, 40)
        self.city_name.setStyleSheet("""
    color: black;
    font-weight: bold;
    background-color: white;
    border: 2px solid hsl(231, 100%, 20%);
    border-radius: 5px;
    padding: 5px;
""")
        self.submit_button.setGeometry(210, 20, 75, 40)
        self.submit_button.setFont(QFont("Helvetica", 7))
        self.submit_button.setStyleSheet("""
            color: black;
            font-weight: bold;
            border: 2px solid #01168c;
            border-radius: 5px;
            padding: 5px;
            background-color: hsl(231, 98%, 56%);""")

    def center(self):
        """This method centers the window on the user's monitor"""

        screen_area= QDesktopWidget().availableGeometry()
        screen_width= screen_area.width()
        screen_height= screen_area.height()

        window_area= self.frameGeometry()

        horizontal_centre= (screen_width-window_area.width()) //2
        vertical_centre= (screen_height-window_area.height()) //2
        self.move(horizontal_centre, vertical_centre)



def main():
    app= QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())




if __name__=="__main__":
    main()
