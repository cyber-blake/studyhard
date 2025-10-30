from watering_system import *
import pytest


# * 1.1
@pytest.fixture
def watering_system():
    watering_system = WateringSystem()
    watering_system.add_area("Garden", 30)
    return watering_system


def test_initial_soil_moisture(watering_system):
    assert watering_system.areas["Garden"]["soil_moisture"] == 30


# * 1.2
def test_add_water(watering_system):
    watering_system.water_level = 2000
    watering_system.add_water(500)
    assert watering_system.water_level == 2500


# * 1.3
def test_add_existing_area(watering_system):
    watering_system.add_area("Garden", 50)
    assert watering_system.areas["Garden"]["soil_moisture"] == 30


# * 1.4
def test_add_new_area(watering_system):
    watering_system.add_area("Lawn", 40)
    assert "Lawn" in watering_system.areas


# * 1.5
def test_water_spray_supply(watering_system):
    watering_system.water_spray_supply("Garden", 15)
    assert watering_system.areas["Garden"]["spray_water"] == 15


# * 1.6
cases = [("Garden", 10, 80)]


@pytest.mark.parametrize("area,duration,expected_moisture", cases)
def test_water_area(watering_system, area, duration, expected_moisture):
    watering_system.water_area(area, duration)
    assert watering_system.areas[area]["soil_moisture"] == expected_moisture


# * 1.7
@pytest.mark.xfail
def test_water_area_not_enough_water(watering_system):
    watering_system.areas["Garden"]["soil_moisture"] = 0
    x = watering_system.water_area("Garden", 30)
    assert x


# * 1.8
def test_max_soil_moisture(watering_system):
    watering_system.areas["Garden"]["soil_moisture"] = 100
    watering_system.water_area("Garden", 30)
    assert watering_system.areas["Garden"]["soil_moisture"] == 100


# * 1.9
def test_soil_moisture_after_long_watering(watering_system):
    watering_system.water_area("Garden", 60)
    assert watering_system.areas["Garden"]["soil_moisture"] == 100


# * 1.10
def test_soil_moisture_after_watering(watering_system):
    watering_system.water_area("Garden", 30)
    assert watering_system.areas["Garden"]["soil_moisture"] == 100
