import numpy as np
import time
t0 = 0 
t1 = 0
xxx = 0

def start():
    global t0,t1,xxx 
    t0 = time.time()
    xxx = np.arange(10000000)
    t1 = time.time()
    t0 = time.time()
def end():
    global t0,t1,xxx 
    t0 = time.time()
    yyy = np.sin(xxx)
    t1 = time.time()
    print('Process : %f'%(t1-t0))

#simple test
start()
print("hello world")
end()