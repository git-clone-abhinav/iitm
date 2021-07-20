class StudentResult:
    count = 0
    def __init__(self,Roll_no,Student_name,Math,Physics,Chemistry,Computer,English,Email_id=None):
        # Assigning parameter value to instance variable 
        self.Roll_no = Roll_no
        self.Student_name = Student_name
        self.Email_id = Email_id
        self.Math = Math
        self.Physics = Physics
        self.Chemistry = Chemistry
        self.Computer = Computer
        self.English = English
        StudentResult.count += 1

    # Create Total_marks method
    def Total_marks(self):
        return(str((self.Math+self.Physics+self.Chemistry+self.Computer+self.English))+'/500')
    
    # Create Average_marks method
    def Avergae_marks(self):
        return(str((self.Math+self.Physics+self.Chemistry+self.Computer+self.English)/5))
    
    # Create Max_marks method
    def Max_makrs(self):
        return(max(self.Math,self.Physics,self.Chemistry,self.Computer,self.English))

    # Create Min_marks method
    def Min_marks(self):
        return(min(self.Math,self.Physics,self.Chemistry,self.Computer,self.English))


# Heavy Coder Stuffs going on 