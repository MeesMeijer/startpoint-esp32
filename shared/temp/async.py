import time 

class Progress: 
    done = False




def cb(prog: Progress):
    prog.done = True

def handleBigData(prog: Progress, data: list[int], callback):

    for line in data: 
        time.sleep(1)
        print("Ouch", line)
    
    callback(prog)


prog = Progress()
handleBigData(prog, [x for x in range(0, 5)], cb)

print("Waiting")
t1 = time.time()
while not prog.done: 
    print(f"Waiting {(time.time() - t1)} sec.")
    time.sleep(0.9)




