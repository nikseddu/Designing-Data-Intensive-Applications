import struct

class AppendOnlyLog:


    def __init__(self,filename:str) -> None:
        """
        
        Record format
        | key_len (4 bytes) | key | value_len (4 bytes) | value |

        
        """
        self.file = open(filename,'ab')

    
    def append(self, key:str, value:str) -> int:

        """
        Docstring for append
        
        Append a key value pair in the in the file
        """

        offset = self.file.tell()

        key_bytes = key.encode("utf-8")
        value_bytes = value.encode("utf-8")

        self.file.write(struct.pack(">I",len(key_bytes)))
        self.file.write(key_bytes)

        self.file.write(struct.pack(">I",len(value_bytes)))
        self.file.write(value_bytes)

        self.file.flush()


        return offset