import kitchen_appliance

class Toaster(kitchen_appliance.KitchenAppliance):
    """Toaster (inherited KitchenAppliance)"""
    def __init__(self, type="Toaster", brand="LG", color="Chrome", wattage=500):
        super().__init__(type, brand, color, wattage)
        
    def start_process(self):
        """Start a toaster time cycle"""
        if self.type == "Toaster":
            raise ToastStuckError            #raises error and crashes program
        return super().start_process()
        
class ToastStuckError(kitchen_appliance.MajorApplianceError):
    def __init__(self, message="Toast stuck error has occured, please remove toast or consult user manual."):
        super().__init__(message)