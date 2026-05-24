class Staff:
    def __init__(self, name, staff_id, department):
        self.name = name
        self.staff_id = staff_id
        self.department = department

    def display_info(self):
        print("Name", self.name)
        print("Staff ID", self.staff_id)
        print("Department", self.department)


class Teacher(Staff):
    def __init__(self, name, staff_id, department, courses, salary):
        self.name = name
        self.staff_id = staff_id
        self.department = department
        self.courses = courses
        self.salary = salary

    def teach(self):
        print("Teaching courses", self.courses)

    def display_info(self):
        print("Name", self.name)
        print("Staff ID", self.staff_id)
        print("Department", self.department)
        print("Courses", self.courses)
        print("Salary", self.salary)


class AdminStaff(Staff):
    def __init__(self, name, staff_id, department, role, working_hours):
        self.name = name
        self.staff_id = staff_id
        self.department = department
        self.role = role
        self.working_hours = working_hours

    def perform_task(self):
        print("Performing role", self.role)

    def display_info(self):
        print("Name", self.name)
        print("Staff ID", self.staff_id)
        print("Department", self.department)
        print("Role", self.role)
        print("Working Hours", self.working_hours)


class ResearchAssistant(Staff):
    def __init__(self, name, staff_id, department, research_topic, stipend):
        self.name = name
        self.staff_id = staff_id
        self.department = department
        self.research_topic = research_topic
        self.stipend = stipend

    def work_on_research(self):
        print("Research topic", self.research_topic)

    def display_info(self):
        print("Name", self.name)
        print("Staff ID", self.staff_id)
        print("Department", self.department)
        print("Research Topic", self.research_topic)
        print("Stipend", self.stipend)


teacher1 = Teacher("Dr. Smith", "T101", "Computer Science", ["AI", "ML"], 80000)
admin1 = AdminStaff("Ms. Johnson", "A202", "Administration", "Manager", 40)
research1 = ResearchAssistant("Alex Brown", "R303", "Engineering", "Robotics", 2000)

teacher1.display_info()
teacher1.teach()

admin1.display_info()
admin1.perform_task()

research1.display_info()
research1.work_on_research()
