class TimeConverter:
    # Create constructor for TimeConverte
    def __init__(self,seconds):
        self.seconds = seconds

    def Second_to_Minutes(self):
        min = self.seconds // 60
        sec = self.seconds % 60
        return (str(min) + " min " + str(sec) + " sec")\

    def Second_to_Hours(self):
        min = self.seconds // 60
        sec = self.seconds % 60
        hours = min // 60 
        min = min % 60
        return (str(hours) + " hours " +str(min) + " min " + str(sec) + " sec")
    
    def Second_to_Days(self):
        min = self.secondsa // 60
        min = self.seconds // 60
        sec = self.seconds % 60
        hours = min // 60 
        min = min % 60
        days = hours // 24
        hours = hours % 24
        return (str(days) + " hours " + str(hours) + " hours " +str(min) + " min " + str(sec) + " sec")
        