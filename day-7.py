s={"MON","TUE","WED"}
print(type(s))
s.add("FRI")

s.update("THU")
print(s)



#Difference between REMOVE and DISCARD



"""s.remove("SUN")
print(s)
s.discard("SUN")

print(s)"""


#FROZEN SRT =TUPLES(THIS IS WHY WE CAN USE IT AS DICT KEYS)
#MTSQL ME V DATA KEY VALUE  PAIR KE FORM ME STORE HOTAA H

#DICTIONARY



D={}
print(type(D))
D={"101":"Civil","102":"ME","155":"cse(iot)"}
print(D.keys())
print(D.values())

print(D["155"])
D["101"]="CSE"
print(D)
print(D.pop("101"))
print(D)


print(D.pop("155"))


# keys of DICT are unique
#list cannot be used as keys



print(D.items())
p={101:"ce",102:"ME",155:["CSE","CSE(IOT)"]}
print( "The branch at index 1 is",p[155][1])


#trversing means to visiting data structures
#windows os code is written in 10 to  15 lacs lines




# CONCEPT OF OOPS


class Car:
    def __init__(self):
        
        
    
        self.brand="Suzuki"
        self.colour="Blue"
        self.top_speed=200
        

car=Car()
print(car)
print(car.brand)
print(car.colour)
print(car.top_speed)

##################################################
class Car:
    def __init__(self,b,c,ts):
        
        
    
        self.brand=b
        self.colour=c
        self.top_speed=ts

car=Car("Maruti","black",200)
print(car.brand)
car=Car("BMW","gold",900)
print(car.brand)

#BY THE HELP OF THIS CLASS WE CAN STATE SPEED,


######################################################



class Car:
    def __init__(self,b,c,ts):
        
        
    
        self.brand=b
        self.colour=c
        self.top_speed=ts
        
    def accelerate(self): 
         
         print("Your car top speed is",self.top_speed)
         


car=Car("BMW","gold",900)
print(car.accelerate())

#############################################

class Lion:
    def __init__(self,s,p):

        self.fur=s
        self.food=p
    def jungle(self):

        print("quality of fur",self.fur)



lion=Lion("smooth","flesh")
print(lion.jungle())


#######################################
class College:
    def __init__(self,n,loc):
        
        
    
        self.name=n
        self.location=loc

    def msg(self):
        print(self.name+"is present at"+self.location)



class Department(College):
    def __init__(self,name,ids):
        self.id=ids

college=College("GEC Vaishali","Vaishali")
dep=Department()





















































