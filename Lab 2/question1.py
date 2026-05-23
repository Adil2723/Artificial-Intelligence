class SmartLight:
    def __init__(self, location):
        self.location = location
        self.power_state = "OFF"

    def switch_on(self):
        self.power_state = "ON"
        print(f"{self.location} light turned ON.")

    def switch_off(self):
        self.power_state = "OFF"
        print(f"{self.location} light turned OFF.")

    def show_status(self):
        print(f"{self.location} light is {self.power_state}.")


light1 = SmartLight("Living Room")
light2 = SmartLight("Bedroom")

light1.switch_on()
light2.switch_off()

light1.show_status()
light2.show_status()
