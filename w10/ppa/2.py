class StudentResult():

    # Creating Constructor for the class
    def __init__(self,Roll_no,Student_name,Math,Physics,Chemistry,Computer,English,Email_id=None):
        # Assigning Parameters value to instance variable
        self.Roll_no = Roll_no
        self.Student_name = Student_name
        self.Email_id = Email_id
        self.Math = Math
        self.Physics = Physics
        self.Chemistry = Chemistry
        self.Computer = Computer
        self.English = English

        # Method to print object variable value
        def Display(self):
            print(s1.Roll_no,s1.Student_name,s1.Math,s1.Physics,s1.Chemistry,s1.Computer,s1.English,s1.Email_id)

