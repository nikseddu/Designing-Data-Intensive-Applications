class HashIndex:

 
    """
    In-memory hash map

    Key  -> byte offset in the data file
    
    """

    def __init__(self) -> None:
        self.index = {}

    def set(self,key:str,offset:int):
        self.index[key] = offset


    def get(self, key:str):
        return self.index[key]
    

