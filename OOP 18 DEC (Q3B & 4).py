#!/usr/bin/env python
# coding: utf-8

# In[9]:


from abc import ABC, abstractmethod
class computer(ABC):
    @abstractmethod
    def disp(self):
        pass
    def display1(self):
        print("welcome to bms")



# In[13]:


class laptop(computer):
    def disp(self):
        print("welcome")
l1=laptop()
l1.display1()
l1.disp()


# In[14]:


from abc import ABC, abstractmethod
class vehicle(ABC):
    def __init__(self,w):
        self.wheel=w
    @abstractmethod
    def start(self):
        pass
    def noofwheels(self):
        print(self.wheel)
class bike(vehicle):
    def start(self):
        print("Kickstart")
class car(vehicle):
    def start(self):
        print("Selfstart")
class bus(vehicle):
    def start(self):
        pass
b1=bike(2)
c1=car(4)
bu1=bus(6)
b1.start()
b1.noofwheels()
c1.start()
c1.noofwheels()
bu1.start()
bu1.noofwheels()


# In[18]:


#create a class called as credit, make the limit variable completely private to the outside of the class and
#balance should be Accessible outside the class  but not modifiable since we don't want external code to arbitrarily
#modify the card balance. to achieve this make a get balance() field public however balance
#can only be modified via withdraw and deposit methods that have safeguards in check place.
class creditcard():
    def __init__(self,limit):
        self.__bal=0
        self.__lim=limit
    def get_balance(self):
        return self.__bal
    def withdraw(self,amt):
        if amt>0:
            if amt>self.__bal:
                print("TRANSACTION FAILED")
            else:
                self.__bal=self.__bal-amt
                print(f"Transaction successful! Remaining balance={self.__bal}")
        else:
            print("Invalid Amount")
    def deposit(self,amt):
        if amt>0:
            self.__bal=self.__bal+amt
            print(f"Transaction successful! Updated Balance={self.__bal}")
        else:
            print("Invalid amount")
obj=creditcard(1000)
obj.deposit(500)
obj.withdraw(100)
obj.get_balance()
        
        


# In[16]:


# Q4.import the abc module to create the abstract base class. create the class that inherits the abc class and define an abstract method named mileage().
# inherit the base class from three different subclasses and implement the abstract method differently. create the objects to call the abstract method
from abc import ABC, abstractmethod
class car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class sedan(car):
    def mileage(self):
        print("Sedan mileage: 25 miles per gallon")
class SUV(car):
    def mileage(self):
        print("SUV mileage: 20 miles per gallon")
class ec(car):
    def mileage(self):
        print("Electric car mileage: 100 miles per charge")
h1=sedan()
h1.mileage()
n1=SUV()
n1.mileage()
a1=ec()
a1.mileage()


# In[ ]:




