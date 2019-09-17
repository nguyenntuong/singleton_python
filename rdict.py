class ReadOnlyAfterWrite(Exception):
    pass
class ReadOnlyDict(dict):
    def __setitem__(self, key, value):
        if key not in self.keys():
            self.setdefault(key,value)
        else:
            raise ReadOnlyAfterWrite("Key: ",key)
