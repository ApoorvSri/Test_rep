class Fan:
    rpm=100
    def __init__(self,a,b):
        self.dial=a
        self.state=False

        self._name=b
    def up(self,x):
        self.dial+=x
        if self.dial>5:
            self.dial=1
        print("Fan speed is:", (self.rpm) * (self.dial))
    def down(self,x):
        self.dial-=x
        if self.dial<=0:
            self.dial=5
        print("Fan speed is:", (self.rpm) * (self.dial))
    def state_update(self,x):
        if x == 'OFF':
            self.state=False
        if x == 'ON':
            self.state =  True
        print("Fan speed is:", (self.rpm) * (self.dial))


print("HAVELLS")
Havells=Fan(1,'Havells')
Havells._name='Usha'
print(Havells.name)
Havells.up(3)
Havells.down(5)
Havells.Turn_off()
Havells.Turn_on(2)

# print("USHA")
# usha =Fan(3,'USHA')
# usha.up()
# usha.down()
# usha.Turn_off()
# usha.Turn_on(4)


