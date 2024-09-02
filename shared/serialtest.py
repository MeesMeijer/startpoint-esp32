from serial import Serial
import time, json 
import os
def split(text: str, max_length = 240) -> list[str]:
    chunks2, indx = ["START"], 0
    for i in range(0, len(text), max_length):
        chunks2.append(f"{indx}~{text[i:i+max_length]}")
        indx += 1 
    chunks2.append(f"STOP")
    return chunks2

def merge(chunks: list[str]):
    # print(chunks)
    chunks.pop(0)
    chunks.pop(-1)
    t = ""
    for ind, data in enumerate(chunks):
        if (place := data.find("~")) < 0:  raise Exception(f"missing ~ on line: {ind}: {data}")
        
        id, data = data[0:place], data[place+1::]
        if int(id) != ind:  raise Exception(f"{id} -> {ind} mismatch..")
        t += data
    
    return t


com = "COM6"

dataTosend = []
buffer: dict[str, list] = {}
transfer: dict[str, bool] = {} 
serialConnection = Serial(com, 115200)

while True:
    if serialConnection.in_waiting > 0:
        recvData = serialConnection.readline().decode().strip()
        # print("[debug] - Got data from port:", com ,"\n -->", len(recvData), recvData[0:14])

        mac, recvData = recvData.split("|", 1)
        # print(mac, recvData[0:14])

        print(mac, recvData)

        continue

        if recvData == '{"CMD": "CONNECTING"}': 
            continue

        if recvData == "START": 
            transfer[mac] = True
            buffer[mac] = []
        
        if transfer[mac]: 
            
            buffer[mac].append(recvData)
        
            if recvData == "STOP":
                transfer[mac] = False

                # print(buffer)
                if buffer[mac].count("START") > 1 or buffer[mac].count("STOP") > 1: 
                    for i in range(1, len(buffer)):
                        if buffer[mac][i] == "START":
                            buffer[mac].remove("START")
                        
                        if buffer[mac][i] == "STOP":
                            buffer[mac].remove("STOP")
                        

                merged = json.loads(merge(buffer[mac]))
                try:
                    os.makedirs(f"./temp/{mac}/")
                except: 
                    pass 
                print("Done.")
                with open(f"./temp/{mac}/{time.time()}.json", "w+") as file: 
                   file.write(json.dumps(merged))

                buffer[mac] = []


    if len(dataTosend) > 0:
        for _ in range(len(dataTosend)):
            msg = dataTosend.pop(0)
            print(f"[debug] - Sending {len(msg)} bytes. \n -->", msg)
            serialConnection.write(msg.encode() + b"\n")




