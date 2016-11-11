import RPi.GPIO as GPIO

import time

import os

import datetime


GPIO.setmode(GPIO.BOARD)

GPIO.cleanup()

GPIO.setup(29, GPIO.OUT)

GPIO.setup(31, GPIO.OUT)

GPIO.setup(33, GPIO.OUT)

GPIO.setup(35, GPIO.OUT)

GPIO.setup(36, GPIO.IN)

GPIO.setup(37, GPIO.OUT)

GPIO.setup(38, GPIO.OUT)

GPIO.setup(40, GPIO.OUT)

f = open('/mnt/raw/wind', 'w')
f.write('OK')
f.close()

f = open('/mnt/raw/pos', 'w')
f.write('1')
f.close()

i=1
t2=24

def info():
    f = open('/mnt/raw/wind')
    com = f.read()
    f.close()
    return com

def ans():
    f = open('/mnt/raw/wind', 'w')
    f.write('OK')
    f.close()
    print ("OK")

def rob():
    c = info()
    if c=="10":
        GPIO.output(37, 1)
        print ("close1")
        time.sleep(3)
        GPIO.output(37, 0)
        ans()
    elif c=="11":
        GPIO.output(35, 1)
        print ("open1")
        time.sleep(2)
        GPIO.output(35, 0)
        ans()
    elif c=="12":
        GPIO.output(37, 1)
        print ("close1")
        time.sleep(3)
        GPIO.output(37, 0)
        ans()
    elif c=="13":
        GPIO.output(35, 1)
        print ("open1")
        time.sleep(1)
        GPIO.output(35, 0)
        ans()
    elif c=="20":
        GPIO.output(33, 1)
        print ("close2")
        time.sleep(3)
        GPIO.output(33, 0)
        ans()
    elif c=="21":
        GPIO.output(31, 1)
        print ("open2")
        time.sleep(3)
        GPIO.output(31, 0)
        ans()
    elif c=="22":
        GPIO.output(33, 1)
        print ("close2")
        time.sleep(1)
        GPIO.output(33, 0)
        ans()
    elif c=="23":
        GPIO.output(31, 1)
        print ("open2")
        time.sleep(1)
        GPIO.output(31, 0)
        ans()
    elif c=="30":
        global i
        i=0
        ans()
        f = open('/mnt/raw/pos', 'w')
        f.write('0')
        f.close()
        print('30')
        global i
        i=0
        ans()
    elif c=="31":
        f = open('/mnt/raw/pos', 'w')
        f.write('1')
        f.close()
        print('31')
        global i
        i=1
        ans()
        



#def tep():
while True:

 rob()
 if i==1:

#  if os.path.isdir("/sys/bus/w1/devices/28-011563e6feff"):  

  # tfile=open("/sys/bus/w1/devices/28-011563e6feff/w1_slave")

  # ttext=tfile.read()

  # tfile.close()

  # temp=ttext.split("\n")[1].split(" ")[9]

   # t=float(temp[2:])/1000

    #print t

 # else:

#    print ('File not found')
 #   t==t2

  if os.path.isdir("/sys/bus/w1/devices/28-011563e8d2ff"):


    tfile2=open("/sys/bus/w1/devices/28-011563e8d2ff/w1_slave")
 
    ttext2=tfile2.read()
 
    tfile2.close()
 
    temp2=ttext2.split("\n")[1].split(" ")[9]
 
    t2=float(temp2[2:])/1000

 #   print t2

  else:

    print ('File not found')
    t2==24



  if    t2<24:
 
        GPIO.output(37, 1)
        print ("close1")
        time.sleep(1)
        GPIO.output(37, 0)

  elif  t2>25:

        GPIO.output(35, 1)

        print ("open1")

        time.sleep(2)

        GPIO.output(35, 0)

        

  else:

        print ("none1")
       
  j=0
  while(j<36):
      rob()
      time.sleep(5)
      j=j+1
      if i==0:
          break


 # if os.path.isdir("/sys/bus/w1/devices/28-011563e6feff"):

 #   tfile=open("/sys/bus/w1/devices/28-011563e6feff/w1_slave")
#
 #   ttext=tfile.read()
#
 #   tfile.close()
#
#    temp=ttext.split("\n")[1].split(" ")[9]

   # t=float(temp[2:])/1000

   # print t

#  else:

 #   print ('File not found')
  #  t==t2

  if os.path.isdir("/sys/bus/w1/devices/28-011563e8d2ff"):


    tfile2=open("/sys/bus/w1/devices/28-011563e8d2ff/w1_slave")

    ttext2=tfile2.read()

    tfile2.close()

    temp2=ttext2.split("\n")[1].split(" ")[9]

    t2=float(temp2[2:])/1000

   # print (t2)

  else:

    print ('File not found')
    t2==25



  if    t2<25:
        GPIO.output(33, 1)

        print ("close2")

        time.sleep(1)

        GPIO.output(33, 0)

       

  elif  t2>26:
  
        GPIO.output(31, 1)
        print ("open2")

        time.sleep(1)

        GPIO.output(31, 0)
     

  else:

        print ("none2")


  j=0
  while(j<36):
      rob()
      time.sleep(5)
      j=j+1
      if i==0:
          break
