# TIMER

class Timer:
    def __init__(self,hours=0,mins=0,sec=0):
        self.hours=hours
        self.mins=mins
        self.sec=sec

    
    def __str__(self):
        h=str(self.hours)
        m=str(self.mins)
        s=str(self.sec)
        x=0
        if self.hours<10: h=str(x)+h
        if self.mins<10: m=str(x)+m
        if self.sec<10: s=str(x)+s

        return h+":"+m+":"+s
        

    def next_sec(self):
        if self.sec==59: 
            self.sec=0
            if self.mins==59:
                self.mins=0
                if self.hours==23:
                    self.hours=0
                else: self.hours=self.hours+1
            else: self.mins=self.mins+1
        else: self.sec=self.sec+1
        

    def prev_sec(self):
        if self.sec==0:
            self.sec=59
            if self.mins==0:
                self.mins=59
                if self.hours==0:
                    self.hours=23
                else: self.hours=self.hours-1
            else: self.mins=self.mins-1
        else: self.sec=self.sec-1

    
def main():
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_sec()
    print(timer)
    timer.prev_sec()
    print(timer)

    

if __name__=="__main__":
    main()
    

