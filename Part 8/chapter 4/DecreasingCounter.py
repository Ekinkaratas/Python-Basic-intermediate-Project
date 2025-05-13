class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        if self.Value <= 0:
            print("your balance has run out")
            self.value = 0
        print("value:", self.value)

    def decrease(self):
        self.Value-= 1

    def set_to_zero(self):
        self.value = 0

    def incrase(self,num =1):
        self.value += num