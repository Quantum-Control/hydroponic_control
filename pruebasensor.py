import RPi.GPIO as GPIO
import Adafruit_DHT
import anvil.server
import requests, json 

api_key = "8e09338ad9fb1dafbb7f24a6c5e0f273"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = ("tuxtla")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()


sen = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN)
GPIO.setup(8, GPIO.OUT)

anvil.server.connect("73OMHQFKYIE7PSBIYTVCV4HF-ZXBVDM6OJVWT5RTG")

@anvil.server.callable
def temtux():
    if x["cod"] != "404":
        y = x["main"]
        tuxtem=current_temperature = y["temp"]-273.15
        z = x["weather"]
        weather_description = z[0]["description"]
    else: 
        print(" City Not Found ")
    return tuxtem

@anvil.server.callable
def humtux():
    if x["cod"] != "404":
        y = x["main"]
        tuxhum=current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
    else: 
        print(" City Not Found ")
    return tuxhum

@anvil.server.callable
def pretux():
    if x["cod"] != "404":
        y = x["main"]
        current_pressure = y["pressure"]
        z = x["weather"]
        weather_description = z[0]["description"]
    else: 
        print(" City Not Found ")
    return current_pressure

@anvil.server.callable
def weatux():
    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]
        tuxwea=weather_description = z[0]["description"]
    else: 
        print(" City Not Found ")
    return tuxwea

@anvil.server.callable
def temp():
    humedad, temperatura = Adafruit_DHT.read_retry(sen, 10)
    return temperatura

@anvil.server.callable
def hum2():
    humedad, temperatura = Adafruit_DHT.read_retry(sen, 10)
    return humedad

@anvil.server.callable
def hum1():
    i=0
    while i== 0:
        if GPIO.input(10) == GPIO.HIGH:
            GPIO.output(8, True)
            resul="El nivel de humedad es nulo"
            i=i+1
        else:
            GPIO.output(8, False)
            resul="El nivel de humedad es optimo"
            i=i+1
    return resul
        
        
anvil.server.wait_forever()