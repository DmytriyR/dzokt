from abc import ABC, abstractmethod

class Robot(ABC):
        self.name = name
        self.model = model
        self.power_level = power_level
    def show_info(self):
        print(f"Name - {self.name}, model - {self.model}, power_level - {self.power_level}%")
    @abstractmethod
    def perform_task(self):
        pass
    def charge(self, charge):
        self.power_level = min(100, self.power_level + charge)
        print(f"Name - {self.name}, model - {self.model}, charge to - {self.power_level}%")

class WorkerRobot(Robot):
    def __init__(self, name, model, tool, robot_file, file = "robot_file.txt"):
        super().__init__(name, model)
        self.tool = tool
        self.file = file
    def __enter__(self):
        self.file = open(self.file, "w")
        return self.file

    def perform_task(self):
        if self.power_level >= 10:
            self.power_level -= 10
            print(f"{self.name}, model - {self.model}, completed the task with the help of the tool - {self.tool}, power_level - {self.power_level}")
        else:
            print(f"{self.name}, model - {self.model} - does not have enough power to perform the task.")
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"{exc_type} go wrong {exc_val}")
class DefenseRobot(Robot):
    def __init__(self,name, model, weapon):
        super().__init__(name, model)
        self.weapon = weapon
    def perform_task(self):
        if self.power_level >= 15:
            self.power_level -= 15
            print(f"{self.name}, model - {self.model}, defended himself using a weapon - {self.weapon}, power_level - {self.power_level}")
        else:
            print(f"{self.name}, model - {self.model} - does not have enough power to perform the task.")
    def __del__(self):
        print("Об'єкт очищено")
class ServiceRobot(Robot):
    def __init__(self, name, model, service_type):
        super().__init__(name, model)
        self.service_type = service_type
    def perform_task(self):
        if self.power_level >= 5:
            self.power_level -= 5
            print(
                f"{self.name}, model - {self.model}, the service was provided - {self.service_type}, power_level - {self.power_level}")
        else:
            print(f"{self.name}, model - {self.model} - does not have enough power to perform the task.")
    def __del__(self):
        print("Об'єкт очищено")

robot_working = WorkerRobot("Bob", "X1", "Wrench", "robot_file.txt")
robot_defence = DefenseRobot("Defender", "Z3", "Laser")
robot_employe = ServiceRobot("Helper", "S2", "Cleaning")

with robot_working as fl:
    fl.write(f"Name: {robot_working.name}, Power level: {robot_working.power_level}")

robot_working.show_info()
robot_working.perform_task()
robot_working.perform_task()
robot_working.charge(25)
robot_working.show_info()

robot_defence.show_info()
robot_defence.perform_task()
robot_defence.perform_task()
robot_defence.charge(25)
robot_defence.show_info()

robot_employe.show_info()
robot_employe.perform_task()
robot_employe.perform_task()
robot_employe.show_info()
robot_employe.charge(15)
robot_employe.show_info()
