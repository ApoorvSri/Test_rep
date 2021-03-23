class Fan:
    rpm=100
    def __init__(self,a):
        self.dial=a
    def up(self):
        self.dial+=1
        print("Fan speed is:", (self.rpm) * (self.dial))
    def down(self):
        self.dial-=1
        print("Fan speed is:", (self.rpm) * (self.dial))




fan1=Fan(1)
fan1.up()
fan1.down()
