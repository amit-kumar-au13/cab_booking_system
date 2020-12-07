# class to gather and access the driver data
class Driver:
    def __init__(self):
        self.driver = []
    def driver_info(self, name, cabno, contact, available, location_x, location_y):
        drivers = {"name": name, "cabno": cabno, "contact": contact,
                   "available": available, "x1": location_x, "x2": location_y}
        self.driver.append(drivers)
        return drivers
    def getDriverslist(self):
        return self.driver