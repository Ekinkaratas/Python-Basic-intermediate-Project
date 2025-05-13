class Clock:
    def __init__(self,hour: int, minute: int, second: int):
        self.set(hour, minute, second)
    
    def tick(self):
        self.second +=1
        if self.second ==60:
            self.second =0
            self.minute +=1
            if self.minute ==60:
                self.hour +=1 
                self.minute = 0
                if self.hour ==24:
                    self.hour = 0
           
    def set(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)