class PresentDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self):
        if (self.year % 4 == 0 and not self.year % 100 == 0) or self.year % 400 == 0:
            return True
        else:
            return False

    def is_legal(self):
        # 注入bug
        if not (2000 <= self.year <= 2100 and 1 <= self.month <= 12 and 1 <= self.day <= 31):
            # return False
            return True
        else:
            if self.month in [4, 6, 9, 11] and self.day >= 31:
                return False
            if self.month == 2:
                if self.is_leap_year() and self.day > 29:
                    return False
                elif not self.is_leap_year() and self.day > 28:
                    return False
            return True

    def add_day(self, n_day):
        if not self.is_legal():
            return "None"
        for d in range(n_day):
            self.add_one_day()
        return f"{self.year}/{self.month}/{self.day}"

    def add_one_day(self):
        if self.day < 28:
            self.day = self.day + 1
        elif self.day == 28:
            if not self.month == 2:
                self.day = self.day + 1
            elif self.month == 2:
                if self.is_leap_year():
                    self.day = self.day + 1
                else:
                    self.day = 1
                    self.add_one_month()
        elif self.day == 29:
            if not self.month == 2:
                self.day = self.day + 1
            else:
                self.day = 1
                self.add_one_month()
        elif self.day == 30:
            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                self.day = self.day + 1
            elif self.month in [4, 6, 9, 11]:
                self.day = 1
                self.add_one_month()
        elif self.day == 31:
            self.day = 1
            self.add_one_month()

    def add_one_month(self):
        if not self.month == 12:
            self.month = self.month + 1
        else:
            self.month = 1
            self.add_one_year()

    def add_one_year(self):
        self.year = self.year + 1


def decide_date_type(test_sample):
    year, month, day = test_sample
    present_date = PresentDate(year, month, day)
    result = present_date.add_day(1)
    return result


if __name__ == "__main__":
    # 用于测试
    test_date = PresentDate(1900, 1, 1)
    for i in range(365):
        print(test_date.add_day(1))
