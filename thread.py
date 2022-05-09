from threading import Thread
import time

def s1():
    time.sleep(1)
    print("1")

def s2():
    time.sleep(0.2)
    print("2")

th = Thread(target=s2)



