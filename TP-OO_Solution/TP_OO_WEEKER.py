# Weeker Class

class WeekDayError(Exception):
    pass

week=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
class Weeker:
    def __init__(self,day):
        if day in week:
            self.day=day 
            self.nd=week.index(self.day)           
        else:
            raise WeekDayError("Not A Day!!!")
    
    def __str__(self):
        return str(self.day)
        

    def add_days(self,n):
        self.nd=self.nd+n
        self.nd=self.nd%7
        self.day=week[self.nd]

        

    def substract_days(self,n):
        self.nd=self.nd-n
        self.nd=self.nd%7
        self.day=week[self.nd]

def main():
    try:
        weekday = Weeker('Tue')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.substract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError as e:
        print(e)
    #  print("Sorry, I can't serve your request.")


    

if __name__=="__main__":
    main()
    

