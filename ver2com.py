from Process import *
start()
datahex = 'fffffff'
box1 = ""

data_sim2 = datahex
table = []

datahex = list(datahex)



def convert(data):
    global box1
    if data == "0":
        box1 = box1 + "f"    
    elif data == "1":
        box1 = box1 + "e"
    elif data == "2":
        box1 = box1 + "d"
    elif data == "3":
        box1 = box1 + "c"
    elif data == "4":
        box1 = box1 + "b"
    elif data == "5":
        box1 = box1 + "a"
    elif data == "6":
        box1 = box1 + "9"
    elif data == "7":
        box1 = box1 + "8"
    elif data == "8":
        box1 = box1 + "7"
    elif data == "9":
        box1 = box1 + "6"  
    elif data == "a":
        box1 = box1 + "5"
    elif data == "b":
        box1 = box1 + "4"
    elif data == "c":
        box1 = box1 + "3"
    elif data == "d":
        box1 = box1 + "2"
    elif data == "e":
        box1 = box1 + "1"
    elif data == "f":
        box1 = box1 + "0"
    else :
        box1 = box1 + str(data)

for row in datahex :
    data = str(row)
    convert(data)
    
data_sim = box1
box1 = int(box1,16)
print(data_sim2)
print(data_sim)
print(box1/1000)
end()
