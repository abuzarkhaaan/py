class Father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print(":i love cooking")

class Child(Father,Mother):
    def sports(self):
        print("i love cricket")

c = Child()
c.gardening()
c.cooking()
c.sports()
        