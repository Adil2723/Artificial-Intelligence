import time

class Environment:
    def get_light_intensity(self):
        return input("Enter light intensity (Bright/Dim or w to quit): ")

    def get_motion_status(self):
        return input("Is motion detected? (Yes/No or w to quit): ")


class StreetLightAgent:
    def decide_light_status(self, light_intensity, motion_detected):
        if light_intensity == "Bright":
            return "OFF"
        elif light_intensity == "Dim" and motion_detected == "Yes":
            return "ON"
        else:
            return "OFF"

    def run(self, environment):
        while True:
            light_intensity = environment.get_light_intensity()
            if light_intensity.lower() == "w":
                print("Program stopped")
                break

            motion_detected = environment.get_motion_status()
            if motion_detected.lower() == "w":
                print("Program stopped")
                break

            light_status = self.decide_light_status(light_intensity, motion_detected)
            print("Street Light Status:", light_status)
            print("---------------------------")
            time.sleep(1)


env = Environment()
agent = StreetLightAgent()
agent.run(env)
