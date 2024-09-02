def split(text: str, max_length = 240) -> list[str]:
    chunks2, indx = ["START"], 0
    for i in range(0, len(text), max_length):
        chunks2.append(f"{indx}~{text[i:i+max_length]}")
        indx += 1 
    chunks2.append(f"STOP")
    return chunks2

def merge(chunks: list[str]):
    chunks.pop(0)
    chunks.pop(-1)
    t = ""
    for ind, data in enumerate(chunks):
        if (place := data.find("~")) < 0:  raise Exception(f"missing ~ on line: {ind}: {data}")
        
        id, data = data[0:place], data[place+1::]
        if int(id) != ind:  raise Exception(f"{id} -> {ind} mismatch..")
        t += data
    
    return t

info = {
    "user": {
        "name": "MeesM",
        "pass": "mes",
        "id": "1"
    },
    "sensors": {
        "1212-1212-1212":{
            "place": "Woonkamer",
            "status": "Offline",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-121212":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212121":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212122":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212123":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212124":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212125":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212126":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        }
    },
    "sensors2": {
        "1212-1212-1212":{
            "place": "Woonkamer",
            "status": "Offline",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-121212":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212121":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212122":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212123":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212124":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212125":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        },
        "2121-212121-1212126":{
            "place": "Slaapkamer",
            "status": "Online",
            "LastPacket": "1234674124761246"
        }
    }
}

import json 


tests = json.dumps(info)
print(len(tests), len(split(tests)))

chunks = split(tests)

print(f"Sending {len(chunks)} chunks..")

test2 = json.loads(merge(chunks))

print(test2)