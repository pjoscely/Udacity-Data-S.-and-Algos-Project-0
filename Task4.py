"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""



"""Accumulator lists"""
send_texts = [] #distinct send text
receive_texts = [] #distinct recieve text
receive_calls = [] #distinct recieve calls
tele_mrk = [] #distinct possible telemarketers

"""
This function strips spaces, parentheses and a leading zeros to return a pure 10-digit number
actually not needed according to reviewer, but left as a code stub.
def clean_num(n):

    if " " in n:
        n = n.replace(" ","")
    if "(0" in n:
        n = n.replace("(0","")
        n = n.replace(")","")
    return n
"""      



for record in texts:
    temp_send = record[0]
    if temp_send not in send_texts:
        send_texts.append(temp_send)
        
    temp_rec = record[1]
    if temp_rec not in receive_texts:
        receive_texts.append(temp_rec)
        
for record in calls:
    temp_rec = record[1]
    if temp_rec not in receive_calls:
        receive_calls.append(temp_rec)
        
        
for record in calls:
    temp_send = record[0]
    if temp_send not in send_texts and temp_send not in receive_texts and temp_send not in receive_calls:
        if temp_send not in tele_mrk:
            tele_mrk.append(temp_send)

#sort list of possible telemarketers
tele_mrk.sort()        
        
print("These numbers could be telemarketers: ")
for item in tele_mrk:
    print(item)
    
    