
class KitchenAppliance:
    """Define basic kitchen appliance"""
    def __init__(self, type="Kitchen Appliance", brand="Brand", color="Color", wattage=None):
        self.type = type
        self.brand = brand
        self.color = color
        self.wattage = wattage
        
    def __str__(self):
        """Print out attributes of self"""
        return f"   Kitchen Appliance type: {self.type}\n   Brand: {self.brand}\n   Color: {self.color}\n   Wattage: {self.wattage}\n"
    
    def power_on(self):
        """Power on method"""
        print("Powering on!")
        return True
        
    def start_process(self):
        """Start kitchen appliance cycle/process"""
        self.message = "Starting appliance cycle..."
        print(self.message)
    
    def input_time(self):
        """Input time for kitchen appliance"""
        bad_input = True
        
        while bad_input:
            try:
                time = input("Enter a valid time (seconds) ->")
                time = int(time)
                bad_input = False
            except ValueError as ve:
                print(f"That is not a valid time!")
                
        print(f"You entered {time} seconds!")
            
class MajorApplianceError(Exception):
    def __init__(self, message="A kitchen appliance error has occured, please restart appliance or consult user manual."):
        super().__init__()
        self.message = message

    
