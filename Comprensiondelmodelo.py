from vpython import *
from time import *
import numpy as np
import math
import serial
ad=serial.Serial('com5',115200)
sleep(1)

scene.range=5
toRad=2*np.pi/360
toDeg=1/toRad
scene.forward=vector(-1,-1,-1)
scene.width=600
scene.height=1000

xarrow=arrow(length=4,shaftwidth=0.1,color=color.red,axis=vector(1,0,0))
yarrow=arrow(length=2,shaftwidth=0.1,color=color.green,axis=vector(0,1,0))
zarrow=arrow(length=3,shaftwidth=0.1,color=color.blue,axis=vector(0,0,1))
frontarrow=arrow(length=4,shaftwidth=0.1,color=color.purple,axis=vector(1,0,0))
uparrow=arrow(length=3,shaftwidth=0.1,color=color.magenta,axis=vector(0,1,0))
sidearrow=arrow(length=2.5,shaftwidth=0.1,color=color.orange,axis=vector(0,0,1))
bBoard=box(length=1.7,width=1.1,height=.2,opacity=0.8,pos=vector(0,0+2.9,0))
arduino=box(length=.8,width=.5,height=.1,opacity=1.0,pos=vector(-.44,.15+2.9,0),color=color.blue)
bno055=box(length=0.3,width=0.2,height=0.03,opacity=1.0,pos=vector(.68,.115+2.9,0),color=color.orange)

sCRD=box(pos=vector(1.15,0+2.9,1.15),length=.2,height=6,width=0.2)
sCLD=box(pos=vector(-1.15,0+2.9,1.15),length=.2,height=6,width=0.2)
sCRS=box(pos=vector(1.15,0+2.9,-1.15),length=.2,height=6,width=0.2)
sCLS=box(pos=vector(-1.15,0+2.9,-1.15),length=.2,height=6,width=0.2)

sBI=box(pos=vector(0,-2.9+2.9,1.15),length=2.5,height=.2,width=0.2)
sBS=box(pos=vector(0,-2.9+2.9,-1.15),length=2.5,height=.2,width=0.2)
sBL=box(pos=vector(-1.15,-2.9+2.9,0),length=0.2,height=.2,width=2.5)
sBR=box(pos=vector(1.15,-2.9+2.9,0),length=0.2,height=.2,width=2.5)

sTI=box(pos=vector(0,2.9+2.9,1.15),length=2.5,height=.2,width=0.2)
sTS=box(pos=vector(0,2.9+2.9,-1.15),length=2.5,height=.2,width=0.2)
sTL=box(pos=vector(-1.15,2.9+2.9,0),length=0.2,height=.2,width=2.5)
sTR=box(pos=vector(1.15,2.9+2.9,0),length=0.2,height=.2,width=2.5)

placaEle=box(length=2.5,width=2.5,height=.05,opacity=0.2,pos=vector(0,-.1,0))

ruedaF=sphere(pos=vector(0,-3.6+2.9,1.2),radius=0.5,color=color.red)
ruedaTL=sphere(pos=vector(-1.2,-3.6+2.9,-1.2),radius=0.5,color=color.blue)
ruedaTR=sphere(pos=vector(1.2,-3.6+2.9,-1.2),radius=0.5,color=color.yellow)

pelota=sphere(pos=vector(0,-2.7/2,0),radius=2.7/2)
pelotaidea=sphere(pos=vector(0,-2.7/2,0),radius=2.7/2,opacity=0.5)


myObj=compound([bBoard,arduino,bno055,sCRD,sCLD,sCRS,sCLS,sBI,sBS,sBL,sBR,sTI,sTS,sTL,sTR,placaEle,ruedaF,ruedaTL,ruedaTR,pelota])
while (True):
    while (ad.inWaiting()==0):
        pass
    dataPacket=ad.readline()
    dataPacket=str(dataPacket,'utf-8')
    splitPacket=dataPacket.split(",")
    q0=float(splitPacket[0])
    q1=float(splitPacket[1])
    q2=float(splitPacket[2])
    q3=float(splitPacket[3])

    roll=-atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2))
    pitch=asin(2*(q0*q2-q3*q1))
    yaw=-atan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3))-np.pi/2

    rate(50)
    k=vector(cos(yaw)*cos(pitch),sin(pitch),sin(yaw)*cos(pitch))
    y=vector(0,1,0)
    s=cross(k,y)
    v=cross(s,k)
    vrot=v*cos(roll)+cross(k,v)*sin(roll)

    frontarrow.axis=k
    sidearrow.axis=cross(k,vrot)
    uparrow.axis=vrot
    myObj.axis=k
    myObj.up=vrot
    frontarrow.length=4
    sidearrow.length=4
    uparrow.length=3