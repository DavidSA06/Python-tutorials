from datetime import datetime
import pytz

def time_zone(city):
    city_timezone = pytz.timezone("America/" + city)
    city_date = datetime.now(city_timezone)
    print( city + ": ", city_date.strftime("%d/%m/%Y, %H:%M:%S"))

#bogota_timezone = pytz.timezone("America/Bogota")
#bogota_date = datetime.now(bogota_timezone)
#print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

def run():
    time_zone("Bogota")
    time_zone("Mexico_City")
    time_zone("Caracas")

if __name__ == '__main__':
    run()