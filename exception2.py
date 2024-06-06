class Accident(Exception):
    def __init__( self,msg):
        self.msg=msg
    def print_exception(self):
        print("User defined exeption:", self.msg)




try:
    raise Accident("memory")
except Accident as e:
    e.print_exception()