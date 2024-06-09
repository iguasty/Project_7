import kitchen_appliance

class Microwave(kitchen_appliance.KitchenAppliance):
    """Microwave (inherited KitchenAppliance)"""
    def __init__(self,type="Microwave", brand="Samsung", color="Black", wattage=1100):
        super().__init__(type, brand, color, wattage)
        
    def start_process(self):
        """Start a microwave cycle"""
        if self.type == "Microwave":
            raise MotorError            #raises error
        return super().start_process()
        
class MotorError(kitchen_appliance.MajorApplianceError):
    def __init__(self, message="A motor error has occured, please restart microwave or consult user manual."):
        super().__init__(message)