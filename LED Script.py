#Nabil Youssef
# first code to test LEDs

from gpiozero import LED
from time import sleep
# Blue LED on GPIO 4
Blue_LED = LED(4)
# Green LEDs on GPIO 17, 27, 22
Green_LED1 = LED(17)
Green_LED2 = LED(27)
Green_LED3 = LED(22)
# Red LEDs on GPIO 5, 16, 21
Red_LED1 = LED(5)
Red_LED2 = LED(16)
Red_LED3 = LED(21)
# two blue are always on
Blue_LED.on() 
# ON OFF LEDs
while True:
  #set the led ON for one second
  Green_LED1.on()
  Green_LED2.on()
  Green_LED3.on()
  sleep(1)
  Red_LED1.on()
  Red_LED2.on()
  Red_LED3.on()
  sleep(1)
  Green_LED1.off()
  Green_LED2.off()
  Green_LED3.off()
  sleep(1)
  Red_LED1.off()
  Red_LED2.off()
  Red_LED3.off()
  sleep(1) 