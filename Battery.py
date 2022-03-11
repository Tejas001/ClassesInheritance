# Instances as attributes
class Battery:

    def __init__(self,size = 50):
        self.size = size
        self.charge_level = 0

    def get_range(self):
        if self.size == 50:
            return 250
        elif self.size == 100:
            return 500
