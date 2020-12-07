class Rider:
    def __init__(self):
        self.info = []
    def register_rider(self, name, location, phone_no, booking, location_x, location_y):
        rider = {"name": name, "location": location, "phone_no": phone_no, "booking": booking,
                 "y1": location_x, "y2": location_y}
        self.info.append(rider)
        return rider
    def historyofrides(self):
        print("we will update you after sometime")
        return self.info