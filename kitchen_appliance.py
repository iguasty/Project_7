
class KitchenAppliance:
    """Define basic kitchen appliance"""
    def __init__(self):
        self.type = "Kitchen Appliance"
        self.brand = "Brand"
        self.color = "Color"
        self.wattage = None
        
    def __str__(self):
        """Print out attributes of self"""
        return f"Kitchen Appliance type: {self.type}\nBrand: {self.brand}\nColor: {self.color}\nWattage: {self.wattage}"
    
    def power_on(self):
        """Power on method"""
        print("Powering on!")
        