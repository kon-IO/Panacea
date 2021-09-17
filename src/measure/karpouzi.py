# Anoixe mou ligo to karpouzi -- Gerasimos 2021

# Importing Libraries
from os import read, write
import serial
import time
from subprocess import call
import I2C_LCD_driver

# SETUP
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)
mylcd = I2C_LCD_driver.lcd()

heartFileOut = open("heartValues.txt", "w")
SPO2FileOut = open("spo2Values.txt", "w")

heartValueCounter = 0
spoValueCounter = 0

heartArray = []
spoArray = []

mylcd.lcd_clear()
mylcd.lcd_display_string("Started counting...", 2, 1)
mylcd.lcd_display_string("Please wait!", 3, 4)
print("Started Counting...")
print("Please wait!")
finalValues = open("../backend/interface/final_values.html", "w")
finalValues.write("<html><body><p style='color:white;text-align:center;font-size:40px'>Please wait while Panacea measures your vital signs!</p><p style='color:white;text-align:center;font-size:30px'></p><p style='color:white;text-align:center;font-size:30px'></p></body></html>")
finalValues.close()

try:
    while 1:

        # Getting serial message from arduino oxymeter
        serialMessage = arduino.readline().decode('utf-8').rstrip()

        # Variable Intialization
        heartRate="0"
        spo="0"

        # Testing if message is valid
        if serialMessage == "":
            continue

        # Separate values from text into according variables
        values=[int(n) for n in serialMessage.split() if n.isdigit()]

        heartRate  = values[0]
        spo = values[1]

        mylcd.lcd_clear()

        # Initial testing of values
        if int(heartRate) > 60 and int(heartRate) < 127 or int(spo) > 90 and int(spo) < 100:
            # Checking for acceptable values        
            if int(heartRate) > 60 and int(heartRate) < 127:
                heartFileOut.write(str(heartRate) + "\n")
                heartArray.append(heartRate)
                heartValueCounter += 1
                print("Heart Rate found... waiting for more entries!")
            elif int(spo) > 90 and int(spo) < 100:
                SPO2FileOut.write(str(spo) + "\n")
                spoArray.append(spo)
                spoValueCounter += 1
                print("SPO2 found... waiting for more entries!")
            else:
                continue
        # When we have enough values, we calculate the average and display it
        if heartValueCounter > 10:
            heartValueCounter = 10
        if spoValueCounter > 10:
            spoValueCounter = 10
        totalCounter = heartValueCounter + spoValueCounter
        totalCounter = totalCounter * 5
        if totalCounter > 100:
            totalCounter = 100
        mylcd.lcd_display_string(str(totalCounter) + "% there!", 2, 4)
        finalValues = open("../backend/interface/final_values.html", "w")
        finalValues.write("<html><body><p style='color:white;text-align:center;font-size:40px'>" + str(totalCounter) + "% way there!</p><p style='color:white;text-align:center;font-size:30px'></p><p style='color:white;text-align:center;font-size:30px'></p></body></html>")
        finalValues.close()
        if heartValueCounter >= 10 and spoValueCounter >= 10:

            heartValueMean = round(sum(heartArray) / len(heartArray))
            spoValueMean = round(sum(spoArray) / len(spoArray))

            mylcd.lcd_clear()
            mylcd.lcd_display_string("Oxygen: "+ str(spoValueMean)+"%", 2, 1)
            mylcd.lcd_display_string("HeartRate:"+ str(heartValueMean) + "bpm", 3, 1)
            print("Oxygen: "+ str(spoValueMean)+"%")
            print("Heart Rate:"+ str(heartValueMean) + "bpm")
            finalValues = open("../backend/interface/final_values.html", "w")
            finalValues.write("<html><body><p style='color:white;text-align:center;font-size:40px'></p><p style='color:white;text-align:center;font-size:30px'></p>Oxygen: " + str(spoValueMean) + "%<p style='color:white;text-align:center;font-size:30px'>Heart Rate: " + str(heartValueMean) + "BPM</p></body></html>")
            finalValues.close()
            time.sleep(5)

            # Making sure everything is reset before we remeasure
            heartValueCounter = 0
            spoValueCounter = 0
            mylcd.lcd_clear()
            heartArray = [0]
            finalValues = open("../backend/interface/final_values.html", "w")
            finalValues.write("<html><body><p style='color:white;text-align:center;font-size:40px'></p><p style='color:white;text-align:center;font-size:30px'></p>Oxygen: " + str(spoValueMean) + "%<p style='color:white;text-align:center;font-size:30px'>Heart Rate: " + str(heartValueMean) + "BPM</p></body></html>")
            finalValues.close()
            spoArray = [0]
            serialMessage = ""

            break

except KeyboardInterrupt:
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Stopped")
    finalValues = open("../backend/interface/final_values.html", "w")
    finalValues.write("<html><body><p style='color:white;text-align:center;font-size:40px'>Stopped</p><p style='color:white;text-align:center;font-size:30px'></p><p style='color:white;text-align:center;font-size:30px'></p></body></html>")
    finalValues.close()
    time.sleep(4)
    mylcd.lcd_clear
