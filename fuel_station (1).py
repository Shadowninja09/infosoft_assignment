class FuelStation():
    def __init__(self, disel: int, petrol: int, electric: int):
        # constructor which takes three initial int value which represent the number of stations of respective vehicle
        # slots is a dictionary belonging to an object storing the number of filling station in the fuel station
        self.slots = {
            "disel": disel,
            "petrol": petrol,
            "electric": electric
        }
        # open_slots is a dictionary belonging to an object storing the available filling station which can be used
        # by the user initially the open_slots=slots,but we cannot assign it this way because open_slots will only be
        # a reference to slots this would cause problem when we change the number of open slots
        self.open_slots = {
            "disel": disel,
            "petrol": petrol,
            "electric": electric
        }

    def fuel_vehicle(self, fuel_type: str) -> bool:
        """function for fueling a vehicle"""
        # if the number of open_slots of fuel_type is greater than 0 then the user can use that filling station
        if self.open_slots[fuel_type] > 0:
            # when in use, the available slots must decrease by 1
            self.open_slots[fuel_type] -= 1
            return True
        # if no slots are available for the fuel_type then user cannot use the filling station
        return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        """function for freeing a filling station"""
        # if the number of open_slots is less than the actual number of slots in the FuelStation then we increase the
        # open_slots of specified fuel_type by 1
        if self.open_slots[fuel_type] < self.slots[fuel_type]:
            self.open_slots[fuel_type] += 1
            return True
        # if the number of open_slots is equal to or greater than actual slots then we return false as we cannot
        # increase the actual number of slots of the FuelStation
        return False


f = FuelStation(2, 2, 1)
print(f.fuel_vehicle("disel"))
print(f.fuel_vehicle("petrol"))
print(f.fuel_vehicle("disel"))
print(f.fuel_vehicle("electric"))
print(f.fuel_vehicle("disel"))
print(f.open_fuel_slot("disel"))
print(f.fuel_vehicle("disel"))
print(f.open_fuel_slot("electric"))
print(f.open_fuel_slot("electric"))
