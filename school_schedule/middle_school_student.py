from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation = False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
            
    def summary(self):
        return (f"{self.name} is a {self.grade} "
            f"enrolled in {self.get_num_classes()} classes: "
            f"{self.display_classes()}"
            f"{self.name}'s transportation status is {self.gets_transportation}")
        
