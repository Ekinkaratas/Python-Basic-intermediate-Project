class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.even_Numbers = 0
        self.odd_Numbers = 0

    def add_number(self, number: int):
        if number % 2 == 0:
            self.even_Numbers += number
        else:
            self.odd_Numbers += number

        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.numbers

    def average(self):
        if self.count == 0:
            return 0
        return self.numbers / self.count

    def get_even_sum(self):
        return self.even_Numbers

    def get_odd_sum(self):
        return self.odd_Numbers


if __name__ == "__main__":
    stats = NumberStats()

    while True:
        try:
            number = int(input("Please type in integer numbers (exit with -1): "))
        except ValueError:
            print("Please, type a valid integer.")
            continue

        if number == -1:
            break

        stats.add_number(number)

    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers:", stats.get_even_sum())
    print("Sum of odd numbers:", stats.get_odd_sum())
