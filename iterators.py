class RemoteControl():
    def __init__(self):
        self.channel = ["HBO,","CNN","abc,","espn"]
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index+=1
        if self.index== len(self.channels):
            raise StopIteration
        return self.channel[self.index]
r = RemoteControl()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
