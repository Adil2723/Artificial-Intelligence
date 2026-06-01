class DeliveryRobot:
    def __init__(self, start=0, goal=15):
        self.position = start
        self.goal = goal
        self.steps = 0
        self.path = [self.position]

    def decide_action(self):
        if self.position < self.goal:
            return +1
        elif self.position > self.goal:
            return -1
        else:
            return 0 

    def move(self, action):
        if action != 0:
            self.position += action
            self.steps += 1
            self.path.append(self.position)

    def run(self):
        while self.position != self.goal:
            action = self.decide_action()
            self.move(action)
        print("Goal reached at position", self.position)
        print("Path taken:", self.path)
        print("Total steps:", self.steps)


robot = DeliveryRobot()
robot.run()
