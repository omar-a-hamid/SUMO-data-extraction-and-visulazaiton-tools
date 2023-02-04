import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
# import time
import datetime   
from config import scale
from config import parking_maneuver
# df['A'].value_counts()


import os


if parking_maneuver:
    parking_maneuver_bin = 1
else:
    parking_maneuver_bin = 0
  

directory = "ss/city_freq" 
  
# checking if the directory demo_folder2 
# exist or not.
if not os.path.isdir(directory):
    
    # if the demo_folder2 directory is 
    # not present then create it.
    os.makedirs(directory)


index = 0
freq = []
dict = {}
time_axis = []
# for min in range(1440):
#     dict[str(min)] = ""
# for index in range(23):

#     df = pd.read_csv("output_"+str(index)+".csv")
#     freq.append(df['dateandtime'].value_counts().copy)

#     print(freq)

for index in range(23):

    df = pd.read_csv("output_"+str(index)+".csv")
    freq.append(sum(df['dateandtime'].value_counts()))
    # freq.append((df['dateandtime'].value_counts()))


    # print(freq)


# plt.plot(range(0,23*60),freq)

plt.plot(range(0,23),freq)
plt.xlabel("Hour")
plt.ylabel("Number of Trips")
plt.title("frequency Graph")
plt.xlim([0, 22])


time = datetime.datetime.now()
title_temp = str(directory+'/frequncy_graph_s'+str(scale)+'_p'+str(parking_maneuver_bin)+'_'+str(time)+'.png') #append date and time to screenshot
title = title_temp.replace(':','-') #OS can't save file conating ':' 

plt.savefig(title)

# save graph 
# while True:
#     pass


"""
    counter = 1
    for ref_id in range(len(df)):
        new_ref_id.append(counter)
        counter+=1

    df['ref_id'] = range(1, len(df) + 1)

    

    df.to_csv("Bstop_ref_id.csv", index=False)
    
    print(df)
"""