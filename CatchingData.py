import serial
import time
arduinoData=serial.Serial('com3',115200)
time.sleep(1)
while (1==1):
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket, 'utf-8')
    splitPacket=dataPacket.split(',')
    Caccl=float(splitPacket[0])
    Cgyr=float(splitPacket[1])
    Cmag=float(splitPacket[2])
    Csys=float(splitPacket[3])
    Pitch=float(splitPacket[4])
    Roll=float(splitPacket[5])
    Yaw=float(splitPacket[6])
    print("Caccl=",Caccl," Cgyr=",Cgyr," Cmag=",Cmag," Csys=",Csys," Pitch=",Pitch,"Roll",Roll, "Yaw",Yaw)
