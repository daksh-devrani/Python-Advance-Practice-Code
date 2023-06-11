import time
def measureRuntime(func): #to time our code
    start_time=time.time() #takes current time
    func()
    end_time=time.time()
    print(end_time-start_time)

def power(limit):
    return [x**2 for x in range(limit)]

measureRuntime(lambda : power(5000000))
