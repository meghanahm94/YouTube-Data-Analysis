# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:07:01 2019

@author: murmeg01
"""
import pandas as pd
import re 

#Load the data into a pandas dataframe
df = pd.read_csv("C:/Users/murmeg01/Documents/00 MBA EPBA-08/Project/Level 3/video_consolidated_copy.csv")


def funct(my_str):

    
    print(my_str)
    total_time = 0
    h=0; m=0; secs=0;
    
    if my_str == '' or my_str == 0:
        total_time = 0
    
    elif ('H' in my_str) and ('M' in my_str) and ('S' in my_str):
        print("all 3 exist")
        pattern = 'PT(\d*H?)(\d*M?)(\d*S?)'
        str_match = re.search(pattern, my_str)
        if str_match:
        #print(str_match.group(1))
            if str_match.group(1) != '':
                hour = ''.join(filter(lambda i: i.isdigit(), str_match.group(1)))
                print(hour)
                h = int(hour)*3600
                print(h)
            else:
                h=0
            #print(str_match.group(2))
            if str_match.group(2) != '':
                minute = ''.join(filter(lambda i: i.isdigit(), str_match.group(2)))
                print(minute)
                m = int(minute)*60
            else:
                m=0
            #print(str_match.group(3))
            if str_match.group(3) != '':
                secs = ''.join(filter(lambda i: i.isdigit(), str_match.group(3)))
                print(secs)
        total_time = int(h) + int(m) + int(secs)
    

    
    elif ('H' not in my_str) and ('M' in my_str) and ('S' in my_str):
        print("H doesnt exist")
        pattern = 'PT(\d*M?)(\d*S?)'
        str_match = re.search(pattern, my_str)
        if str_match:
        
            #print(str_match.group(2))
            if str_match.group(1) != '':
                minute = ''.join(filter(lambda i: i.isdigit(), str_match.group(1)))
                print(minute)
                m = int(minute)*60
            else:
                m=0
                
            #print(str_match.group(3))
            if str_match.group(2) != '':
                secs = ''.join(filter(lambda i: i.isdigit(), str_match.group(2)))
                print(secs)
        total_time = int(m) + int(secs)
        print(total_time)
        
        
        
        
    elif ('H' not in my_str) and ('M' not in my_str) and ('S' in my_str):
        print("only seconds")
        pattern = 'PT(\d*S?)'
        str_match = re.search(pattern, my_str)
        if str_match:
            if str_match.group(1) != '':
                secs = ''.join(filter(lambda i: i.isdigit(), str_match.group(1)))
                print(secs)
        total_time = int(secs)
        print(total_time)
        
    
    elif ('H' not in my_str) and ('M' in my_str) and ('S' not in my_str):
        print("Only minutes")
        pattern = 'PT(\d*M?)'
        str_match = re.search(pattern, my_str)
        if str_match:
            if str_match.group(1) != '':
                minute = ''.join(filter(lambda i: i.isdigit(), str_match.group(1)))
                print(minute)
                m = int(minute)*60
            else:
                m=0
        total_time = int(m)
        print(total_time)   
        
        
        
    elif ('H' in my_str) and ('M' not in my_str) and ('S' not in my_str):
        print("Only hours")
        pattern = 'PT(\d*H?)'
        str_match = re.search(pattern, my_str)
        if str_match:
            if str_match.group(1) != '':
                hour = ''.join(filter(lambda i: i.isdigit(), str_match.group(1)))
                print(hour)
                h = int(hour)*3600
                print(h)
            else:
                h=0
        total_time = int(h)
        print(total_time)
        
        
    elif ('H' in my_str) and ('M' not in my_str) and ('S' in my_str):
        print("H&S  exist")
        pattern = 'PT(\d*H?)(\d*S?)'
        str_match = re.search(pattern, my_str)
        if str_match:
        #print(str_match.group(1))
            if str_match.group(1) != '':
                hour = ''.join(filter(lambda i: i.isdigit(), str_match.group(1)))
                print(hour)
                h = int(hour)*3600
                print(h)
            else:
                h=0
            if str_match.group(2) != '':
                secs = ''.join(filter(lambda i: i.isdigit(), str_match.group(2)))
                print(secs)
        total_time = int(h) + int(secs)
        
        
        
        
    elif ('H' in my_str) and ('M' in my_str) and ('S' not in my_str):
        print("H&M does exist")
        pattern = 'PT(\d*H?)(\d*M?)'
        str_match = re.search(pattern, my_str)
        if str_match:
        #print(str_match.group(1))
            if str_match.group(1) != '':
                hour = ''.join(filter(lambda i: i.isdigit(), str_match.group(1)))
                print(hour)
                h = int(hour)*3600
                print(h)
            else:
                h=0
            #print(str_match.group(2))
            if str_match.group(2) != '':
                minute = ''.join(filter(lambda i: i.isdigit(), str_match.group(2)))
                print(minute)
                m = int(minute)*60
            else:
                m=0                
        total_time = int(h) + int(m) 
        
        
        
    else:
        total_time = my_str
   
    return total_time
    
all_times=[]    
for index, row in df.iterrows():
    play_time = row['duration']
    my_str = str(play_time)
    total_time = funct(my_str)
    all_times.append(total_time)
    
df['Duration_Seconds'] = all_times

df.to_csv("C:/Users/murmeg01/Documents/00 MBA EPBA-08/Project/Level 3/play_time_data.csv", index=False)     