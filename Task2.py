"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#dictionary of numbers and total time for a given number
dict_of_times = {}

for record in calls:
    if record[0] not in dict_of_times.keys():
        dict_of_times[record[0]] = int(record[-1]) 
    else:
        dict_of_times[record[0]] += int(record[-1])
        
    if record[1] not in dict_of_times.keys():
        dict_of_times[record[1]] = int(record[-1]) 
    else:
        dict_of_times[record[1]] += int(record[-1])
#for key, val in dict_of_times.items():
    #print(key, val)
    
       
"""list comphrehension method to find longest time and numberadapted from stack overflow"""    
longest_time = max(dict_of_times.values())  
longest_number = [k for k, v in dict_of_times.items() if v ==longest_time] 
#print result which is first item in list longest number
print(longest_number[0],"spent the longest time", longest_time, "seconds, on the phone during September 2016.")