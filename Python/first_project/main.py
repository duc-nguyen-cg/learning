from demo.weather_controller import WeatherController
    
def main():
    controller = WeatherController.getInstance()
    controller.run()


if (__name__ == "__main__"):
    main()  
