# Project_7
 Inheritance and exceptions

**Design:**

The generic object I chose for this project to demonstrate inheritance and could cause exceptions was a kitchen appliance. 

    Object: KitchenAppliance

A generic excpetion for the appliance object is: 

    KitchenApplianceError

Two subclasses of the object:

    Microwave class
    Toaster class

Two subclasses of the exception: 

    MotorError
    FilamentHeatingError

Inheritance diagram:

                     Kitchen Appliance
                    /                  \
            Microwave                    Toaster
           /        \                  /         \
  MotorError   DoorCloseError   ToastStuckError   FilamentHeatingError


**Program Design:**

User can interact with kitchen appliances which can trigger exceptions and errors which will then be handled by the program. The kitchen appliances is implemented using inheritance from a parent class called KitchenAppliance. The two child classes that inherit KitchenAppliance are Microwave and Toaster. Microwave has a subclass inherited from KitchenApplianceError called MotorError. Toaster has a subclass inherited from KitchenApplianceError called FilamentHeatingError.


**Testing**

I implemented a testing file called test_kitchen_appliance.py. The tests run check if the objects are being created and their attributes are being set properly. Another test checks to see if the power is on. After implementing the tests, I realized they weren't utilizing the pytest module... oh well...

***To cause the program to crash with an unhandled exception, uncomment out line 35 in main.py***