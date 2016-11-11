import time
import os
import fnmatch
import MySQLdb as mdb
import logging
logging.basicConfig(filename='/home/pi/DS18B20_error.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#function for storing readings into MySql
def insertDB(IDs, temperature):

  try:

    con = mdb.connect('localhost', 'root', 'koshak', 'teplica');
    cursor = con.cursor()

    for i in range(0,len(temperature)):
      sql = "INSERT INTO DS18B20(sensor_id, date, time, value) \
      VALUES ('%s', '%s', '%s', '%s' )" % \
      (IDs[i], time.strftime("%Y-%m-%d"), time.strftime("%H:%M"), temperature[i])
      cursor.execute(sql)
      sql = []
      con.commit()

    con.close()

  except mdb.Error, e:
    logger.error(e)

#get readings from sensors every 10 minutes and store them to MySql
#while True:

temperature = []
IDs = []

for filename in os.listdir("/sys/bus/w1/devices"):
  if fnmatch.fnmatch(filename, '28-011563e8d2ff'):
    with open("/sys/bus/w1/devices/" + filename + "/w1_slave") as fileobj:
        lines = fileobj.readlines()
    if lines[0].find("YES"):
        pok = lines[1].find('=')
        temperature.append(float(lines[1][pok+1:pok+7])/1000)
        IDs.append(filename)
    else:
          logger.error("Error reading sensor with ID: %s" % (filename))

if (len(temperature)>0):
  insertDB(IDs, temperature)

#  time.sleep(1800)

