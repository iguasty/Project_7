import kitchen_appliance
import microwave
import toaster
import os

os.system('cls') #clear terminal

print("\nWelcome to the kitchen appliance tester!\n\nCreating a generic kitchen appliance object...\n")
#generic object
appliance = kitchen_appliance.KitchenAppliance()
print(appliance)
appliance.power_on()



print("\n\nNow creating a microwave.\n")
#microwave object, inherits from KitchenAppliance
my_microwave = microwave.Microwave()
print(my_microwave)
my_microwave.power_on()
my_microwave.input_time()  #get input from user on cycle time in seconds

try:
    my_microwave.start_process()   #start cycle 
except microwave.MotorError as me:
    print(me.message)

print("\nNow creating a toaster...\n")

#toaster object, inherits from KitchenAppliance
my_toaster = toaster.Toaster()
print(my_toaster)
my_toaster.input_time()
my_toaster.power_on()
# my_toaster.start_process()  #uncomment this line to cause program to crash with an exception

print("\nThis is the end...")