import unittest

class Cellphone():

  def __init__(self, number):
    self.my_number = number 


  def call(self):
    print("we are calling you %s" % (self.my_number))

  def sms(self):
    print("sms to my mom from %s" % (self.my_number))





cellphone1 = Cellphone("0821110000")
print("first")
cellphone1.call()

print("SMS")
cellphone1.sms()

#Ccellphone2 = Cellphone("0831230000")
#Ccellphone2.call()



#Ccellphone1.call()

#Cprint("forth")
#Ccellphone2 = cellphone("0831230000")
#Ccellphone1.call()
#cellphone1.sms()


#cellphone2.call()





