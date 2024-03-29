import traci
import time
import traci.constants as tc
import pytz
import datetime
from random import randrange
import pandas as pd
import os
import numpy as np
import shutil
from config import scale
from config import parking_maneuver

#  columnnames = ['dateandtime', 'vehid', 'coord', 'gpscoord', 'spdK/m', 'edge', 'lane', 'displacement', 'turnAngle' , 'vehDen']

# parking_maneuver = "true"

# scale = 1


if parking_maneuver:
    parking_maneuver_bin = 1
else:
    parking_maneuver_bin = 0
  


# time.process_time()


time_temp = str(datetime.datetime.now())
rt_time = time_temp.replace(':','-')
directory = "SUMO_run/s_"+str(scale)+'p_'+str(parking_maneuver_bin)+'_'+str(rt_time)
  
# checking if the directory demo_folder2 
# exist or not.
# if not os.path.isdir(directory):
    
#     # if the demo_folder2 directory is 
#     # not present then create it.
    # os.makedirs(directory)

os.makedirs(directory)

year = "2022"
month = "12"
day = "6"

# hour =""
# minutes =""
# seconds =""

def getdatetime(n):

    # print("start getdatetime: ",time.process_time())
    # year = "2022"
    # month = "12"
    # day = "6"
    # h = 0*3600
    # m = 0*60
    # s = 0

    # n = n + h + m

    n = n % (24 * 3600)
    hour = str(n // 3600)
 
    n = n % 3600
    minutes = str(n // 60)
 
    n %= 60
    # seconds = str(n)
    
    # t = datetime.datetime(year, month, day, hour, minutes, seconds)
    # DATIME = t.strftime("%Y-%m-%d %H:%M:%S")
    DATIME = (year+"-"+month+"-"+day+" "+hour+":"+minutes+":"+str(n))

    # print("start getdatetime: ",time.process_time())
    
    return DATIME

def flatten_list(_2d_list):

    # print("start flatten list: ",time.process_time())

    flat_list = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    # print("end flatten list: ",time.process_time())

    return flat_list


sumoCmd = ["sumo", "-c", "../osm.sumocfg", "--scale", str(scale),'--parking.maneuver',str(parking_maneuver),"-W"] #scale tarffic by 3 times, disable all warnings
# sumoCmd = ["sumo", "-c", "../osm.sumocfg", "--scale", str(scale),'--parking.maneuver',str(parking_maneuver),"--no-warnings"] #scale tarffic by 3 times, disable all warnings
# sumoCmd = ["sumo", "-c", "../osm.sumocfg", "--scale", str(scale),'--parking.maneuver',str(parking_maneuver),"sumo_warnings=False"] #scale tarffic by 3 times, disable all warnings

traci.start(sumoCmd)
# traci.

# set a speed limit of 60 km/h for all lanes in the network
for lane_id in traci.lane.getIDList():
    traci.lane.setMaxSpeed(lane_id, 13.8)  # 16.67 m/s is equivalent to 60 km/h
                                           #13.8 m/s is 50km/h

packBigData = []

s = 0
hours = 0
print("start: ",time.process_time())

while traci.simulation.getMinExpectedNumber() > 0:
        # while s < (60*10):
        #     s+=1
        #     traci.simulationStep();
        # print("start while traci sim: ",time.process_time())

        # for i in range(0,60):
        #     s+=1
        #     traci.simulationStep();
        #     # print(" traci step: ",time.process_time())
        s+=60
        traci.simulationStep(s);

        vehicles=traci.vehicle.getIDList();
        # print("Vehicle: ", len(vehicles), " at datetime: ", getdatetime(s))
        for i in range(0,len(vehicles)):

                # print("start for i in vehicle: ",time.process_time())


                #Function descriptions
                #https://sumo.dlr.de/docs/TraCI/Vehicle_Value_Retrieval.html
                #https://sumo.dlr.de/pydoc/traci._vehicle.html#VehicleDomain-getSpeed
                # vehid = vehicles[i]
                # x, y = traci.vehicle.getPosition(vehicles[i])
                # coord = [x, y]
                # lon, lat = traci.simulation.convertGeo(x, y)
                # gpscoord = [lon, lat]
                spd = (traci.vehicle.getSpeed(vehicles[i])*3.6)
                edge = traci.vehicle.getRoadID(vehicles[i])
                # lane = traci.vehicle.getLaneID(vehicles[i])
                # displacement = round(traci.vehicle.getDistance(vehicles[i]),2)
                # turnAngle = round(traci.vehicle.getAngle(vehicles[i]),2)

                #Packing of all the data for export to CSV/XLSX
                # vehList = [getdatetime(s), vehid, coord, gpscoord, spd, edge, lane, displacement, turnAngle , len(vehicles)]
                vehList = [getdatetime(s),  spd, edge, len(vehicles)]
                
                


                # idd = traci.vehicle.getLaneID(vehicles[i])

    
                #Pack Simulated Data
                packBigDataLine = flatten_list([vehList])

                # np_vehList = np.array(vehList)
                # packBigDataLine =  np_vehList.flatten()

                packBigData.append(packBigDataLine)

                # print("end for i in vehicle: ",time.process_time())





                ##----------MACHINE LEARNING CODES/FUNCTIONS HERE----------##


                ##---------------------------------------------------------------##






                ##----------CONTROL Vehicles and Traffic Lights----------##

                #***SET FUNCTION FOR VEHICLES***
                #REF: https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html
                # NEWSPEED = 15 # value in m/s (15 m/s = 54 km/hr)
                # if vehicles[i]=='veh2':
                #         traci.vehicle.setSpeedMode('veh2',0)
                #         traci.vehicle.setSpeed('veh2',NEWSPEED)


                #***SET FUNCTION FOR TRAFFIC LIGHTS***
                #REF: https://sumo.dlr.de/docs/TraCI/Change_Traffic_Lights_State.html
                # trafficlightduration = [5,37,5,35,6,3]
                # trafficsignal = ["rrrrrrGGGGgGGGrr", "yyyyyyyyrrrrrrrr", "rrrrrGGGGGGrrrrr", "rrrrryyyyyyrrrrr", "GrrrrrrrrrrGGGGg", "yrrrrrrrrrryyyyy"]
                # tfl = "cluster_4260917315_5146794610_5146796923_5146796930_5704674780_5704674783_5704674784_5704674787_6589790747_8370171128_8370171143_8427766841_8427766842_8427766845"
                # traci.trafficlight.setPhaseDuration(tfl, trafficlightduration[randrange(6)])
                # traci.trafficlight.setRedYellowGreenState(tfl, trafficsignal[randrange(6)])

                ##------------------------------------------------------##
        if s > ((3600*hours) + 3600): #??
            print("*************************************************************************")

                # print("end for i in vehicle: ",time.process_time())
            print(hours ,time.process_time()) #
            print("*************************************************************************")
            columnnames = ['dateandtime',  'spdK/m', 'edge', 'vehDen']
            dataset = pd.DataFrame(packBigData, index=None, columns=columnnames)
            dataset.to_csv(f"output_{hours}.csv", index=False)
            dataset.to_csv(f"{directory}/output_{hours}.csv", index=False)
            packBigData=[]
            hours+=1


traci.close()
if s <= ((3600*hours) + 3600):#what is this? 
    print("*************************************************************************")
    print(hours)
    print("*************************************************************************")
    columnnames = ['dateandtime',  'spdK/m', 'edge','vehDen']
    dataset = pd.DataFrame(packBigData, index=None, columns=columnnames)
    dataset.to_csv(f"output_{hours}.csv", index=False)
    dataset.to_csv(f"{directory}/output_{hours}.csv", index=False)

    packBigData=[]
    hours+=1

#Generate Excel file

shutil.copy('SUMO/stats.json', str(directory)+'/') #not tested

time.sleep(5)








