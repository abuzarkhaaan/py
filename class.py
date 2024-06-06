class Human:
    def __init__(self,n,o):
        self.name= n
        self.occupation= o
    
    def do_work(self):
        if self.occupation =="tennis":
            print(self.name, "play tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots flim")
        
    def speaks(self):
         print(self.name,"says how are you?")

tom= Human("tom cruis","tennis")
tom.do_work()
tom.speaks()

maria = Human("maria","actor")
maria.do_work()
maria.speaks()