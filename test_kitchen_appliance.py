
import pytest
from kitchen_appliance import KitchenAppliance
from microwave import Microwave
from toaster import Toaster

def test_kitchen_appliance_creation():
    """tests creation and setting appliance type"""
    appliance = KitchenAppliance("Generic Appliance")
    assert appliance.type == "Generic Appliance"

def test_microwave_creation():
    """tests creation and setting microwave brand"""
    microwave = Microwave(brand="LG")
    assert microwave.brand == "LG"

def test_toaster_creation():
    """tests creation and setting toaster wattage"""
    toaster = Toaster(wattage=650)
    assert toaster.wattage == 650

def test_microwave_power_on():
    """tests to see if power is on"""
    microwave = Microwave("Operational Microwave")
    result = microwave.power_on()
    assert result == True



