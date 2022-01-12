import serial
ser = serial.Serial('COM7', baudrate = 115200, timeout=1)
my_file = open("otus.txt", "w")
while 1:
    arduinoData = ser.readline()
    my_file.write(arduinoData.decode("utf-8"))
    print(arduinoData)
    
