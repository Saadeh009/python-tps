
# Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

# Zero is the default value for all of the above parameters. There is no need to perform any validation checks.
# The class itself should provide the following facilities:
# •	objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
# •	the class should be equipped with parameter less methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.

# Use the following hints:
# •	all object's properties should be private;
# •	consider writing a separate function (not method!) to format the time string.


def format_time_string(hours, minutes, seconds):

    formatted_hours = str(hours).zfill(2)
    formatted_minutes = str(minutes).zfill(2)
    formatted_seconds = str(seconds).zfill(2)
    return formatted_hours,":", formatted_minutes,":",formatted_seconds
    # return f"{formatted_hours}:{formatted_minutes}:{formatted_seconds}"

class Timer:
    def __init__( self, hours = 0, minutes = 0,seconds =0):
        self.__hours = hours 
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        # return format_time_string(self.__hours, self.__minutes, self.__seconds)
        return "".join(format_time_string(self.__hours, self.__minutes, self.__seconds))

    def next_second(self):
        self.__seconds +=1

        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes +=1
        if self.__minutes == 60 :
            self.__minutes = 0
            self.__hours +=1
        if self.__hours == 24:
            self.__hours = 0

    def prev_second(self):
        self.__seconds -=1
        if self.__seconds < 0:
            self.__seconds=59
            self.__minutes -=1
        if self.__minutes <0 :
            self.__minutes = 59
            self.__hours -= 1
        if self.__hours < 0:
            self.__hours = 23



timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

print ("======")

timer1 = Timer (12, 23, 59)
print(timer1)
timer1.next_second()
print(timer1)
timer1.prev_second()
print(timer1)