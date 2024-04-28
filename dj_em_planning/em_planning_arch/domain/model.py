from datetime import date


class DomainEMData:
    """EM Data domain model."""

    def __init__(self, date, time, frequency, device, location, grid_1, grid_2, lat, long, nearhit):
        self.date = date
        self.time = time
        self.frequency = frequency
        self.device = device
        self.location = location
        self.grid_1 = grid_1
        self.grid_2 = grid_2
        self.lat = lat
        self.long = long
        self.nearhit = nearhit

    def __str__(self):
        return f"{self.frequency}"
