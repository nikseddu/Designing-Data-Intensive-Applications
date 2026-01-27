from AppendOnlyLogImple import AppendOnlyLog
from HashIndexImple import HashIndex
import struct

class KeyValueStore:

    def __init__(self,filename:str) -> None:
        self.filename = filename
        self.log = AppendOnlyLog(filename)
        self.index = HashIndex()


    def put(self,key:str,value :str):
        
        offset = self.log.append(key,value)
        self.index.set(key,offset=offset)

    
    def get(self, key:str):
        
        offset = self.index.get(key=key)
        if offset is None:
            return None
        

        with open(self.filename, "rb") as f:
            # 1. Seek to the offset from the index
            f.seek(offset)

            # 2. Read key length and skip key
            key_len = struct.unpack(">I", f.read(4))[0]
            f.read(key_len)

             # 3. Read value length and value
            value_len = struct.unpack(">I", f.read(4))[0]
            value_bytes = f.read(value_len)

            return value_bytes.decode("utf-8")



store = KeyValueStore("data.log")

store.put("user:1", "Alice")
store.put("user:2", "Bob")
store.put("user:1", "Alice v2")  # update

print(store.get("user:1"))  # Alice v2
print(store.get("user:2"))  # Bob