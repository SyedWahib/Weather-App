import os
import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather Report")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon(r"Assets\Icon.png"))
        self.setStyleSheet("""
                            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                            stop:0 hsl(231, 79%, 53%), stop:1 hsl(231, 100%, 40%));
                           """)

        self.center()

        self.city_name= QLineEdit(self)
        self.city_name.setPlaceholderText("Enter the city name for weather details")
        self.submit_button=QPushButton("Submit", self)
        self.submit_button.setObjectName("submit_button")

        self.initUI()


    def initUI(self):

        self.city_name.setFont(QFont("Inter", 10))
        self.city_name.setGeometry(10, 20, 400, 40)
        self.city_name.setStyleSheet("""
                                        color: black;
                                        font-weight: bold;
                                        background-color: white;
                                        border: 2px solid hsl(231, 100%, 20%);
                                        border-radius: 5px;
                                        padding: 5px;
                                    """)
        self.submit_button.setGeometry(410, 20, 75, 40)
        self.submit_button.setFont(QFont("Helvetica", 7))
        self.submit_button.setStyleSheet("""
                                        QPushButton#submit_button{
                                        color: black;
                                        font-weight: bold;
                                        border: 2px solid #01168c;
                                        border-radius: 5px;
                                        padding: 5px;
                                        background-color: hsl(231, 98%, 56%);}
                                                                    
                                        QPushButton#submit_button:hover{background-color: hsl(231, 98%, 76%);}
                                                                    
                                        QPushButton#submit_button:pressed{background-color: white;
                                                                    color: grey;}
                                         """)
        
        self.submit_button.clicked.connect(self.weatherFinder)

    def weatherFinder(self):

        self.city=self.city_name.text()

        api_key= os.getenv("ApiKeyForWeatherApp")
        url=f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}&units=metric"
        data= requests.get(url)
        weather_details= data.json()
        weather_main_temperature= QLabel(f"{weather_details["main"]["temp"]}°c", self)
        weather_main_temperature.setGeometry(10, 160, 400, 40)
        weather_main_temperature.setFont(QFont("Inter", 12))
        weather_main_temperature.setStyleSheet("""
                                        color: white;
                                        font-weight: bold;
                                        background-color: hsl(231, 98%, 40%);
                                        border-radius: 5px;
                                        padding: 5px;
                                        """)

        weather_main_description= QLabel(f"{weather_details["weather"][0]["main"]}", self)
        weather_main_description.setGeometry(10, 80, 400, 40)
        weather_main_description.setFont(QFont("Inter", 12))
        weather_main_description.setStyleSheet("""
                                        color: white;
                                        font-weight: bold;
                                        background-color: hsl(231, 98%, 40%);
                                        border-radius: 5px;
                                        padding: 5px;
                                        """)
        
        weather_main_temperature.show()
        weather_main_description.show()
        
        #print(data.status_code)

        #print(data.json()['weather'][0]['description'])

        #print(data.json())

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
