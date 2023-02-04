import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
from config import scale
from config import parking_maneuver
from config import normalized_city_speed

# df['A'].value_counts()


import os


if parking_maneuver:
    parking_maneuver_bin = 1
else:
    parking_maneuver_bin = 0
  


directory = "ss/city_speed" 
  
# checking if the directory demo_folder2 
# exist or not.
if not os.path.isdir(directory):
    
    # if the demo_folder2 directory is 
    # not present then create it.
    os.makedirs(directory)

index = 0
avg_speed = []
dict = {}
time_axis = []
# for min in range(1440):
#     dict[str(min)] = ""
# for index in range(23):

#     df = pd.read_csv("output_"+str(index)+".csv")
#     freq.append(df['dateandtime'].value_counts().copy)

#     print(freq)
# result=df.loc[df['a'] == 11,'b'].values[0]

for index in range(23):

    df = pd.read_csv("output_"+str(index)+".csv")
    # speed.append(sum(df['spdK/m'].value_counts()))
    
    speeds = df['spdK/m']
    # print(df['spdK/m'])
    # b = df['spdK/m'].value_counts()
    # print(df['spdK/m'].value_counts())
    # print(sum(a)/b)
    # print(len(df))
    number_trips = (len(df))

    # print(sum(a)/len(df))
    avg_speed.append(sum(speeds)/number_trips)


    # speed.append(sum(df['spdK/m'].value_counts()))
    # freq.append((df['dateandtime'].value_counts()))


    # print(freq)
    # print(avg_speed)

"""
"""
# plt.plot(range(0,23*60),freq)


# print(max(avg_speed))
if normalized_city_speed:
    max_val = (max(avg_speed))

# normalized  = (avg_speed/max_val)
    normalized = []

    for index in range(len(avg_speed)): 
        if not avg_speed[index]:
            avg_speed[index] = max_val
        normalized.append(avg_speed[index]/max_val)
    # print(normalized)
    plt.plot(range(0,23),normalized)
    plt.ylabel("Normalized Average Speed")
    plt.ylim([0, 1.1])
else:
    
    plt.plot(range(0,23),avg_speed)
    plt.ylabel("Average Speed")
    # plt.ylim([0, 1.1])


plt.xlabel("Hour")

plt.title("City Average Speed")
plt.xlim([0, 22])



time = datetime.datetime.now()
title_temp = str(directory+'/city_speed_graph_s'+str(scale)+'_normalized_'+str(normalized_city_speed)+'_p'+str(parking_maneuver_bin)+'_'+str(time)+'.png') #append date and time to screenshot
title = title_temp.replace(':','-') #OS can't save file conating ':' 

plt.savefig(title)

"""
    counter = 1
    for ref_id in range(len(df)):
        new_ref_id.append(counter)
        counter+=1

    df['ref_id'] = range(1, len(df) + 1)

    

    df.to_csv("Bstop_ref_id.csv", index=False)
    
    print(df)
"""