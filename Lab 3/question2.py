import time

class Environment:
    def __init__(self):
        self.rooms = {
            1: input("Is Room 1 dirty? (Yes/No): "),
            2: input("Is Room 2 dirty? (Yes/No): "),
            3: input("Is Room 3 dirty? (Yes/No): ")
        }

    def is_dirty(self, room_number):
        return self.rooms[room_number].lower() == "yes"

    def clean_room(self, room_number):
        self.rooms[room_number] = "No"
        print(f"Room {room_number} cleaned.")

    def all_clean(self):
        return all(status.lower() == "no" for status in self.rooms.values())

    def show_state(self):
        print("Current room states:", self.rooms)


class Robot:
    def __init__(self, environment):
        self.environment = environment
        self.position = 1

    def move_left(self):
        if self.position > 1:
            self.position -= 1
            print(f"Moved to Room {self.position}")

    def move_right(self):
        if self.position < 3:
            self.position += 1
            print(f"Moved to Room {self.position}")

    def clean(self):
        if self.environment.is_dirty(self.position):
            self.environment.clean_room(self.position)
        else:
            print(f"Room {self.position} is already clean.")

    def run(self):
        while not self.environment.all_clean():
            self.environment.show_state()
            self.clean()
            if self.position == 1:
                self.move_right()
            elif self.position == 2:
                if self.environment.is_dirty(1):
                    self.move_left()
                else:
                    self.move_right()
            elif self.position == 3:
                self.move_left()
            time.sleep(1)

        print("All rooms are clean!")


env = Environment()
robot = Robot(env)
robot.run()
