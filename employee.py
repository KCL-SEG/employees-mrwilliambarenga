"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from contextlib import nullcontext


class Employee:
    def __init__(self, name, base_rate, base_time=1, commission_rate=0, commission_time=1):
        self.name = name
        self.base_rate = base_rate
        self.base_time = base_time
        self.commission_rate = commission_rate
        self.commission_time = commission_time

    def get_pay(self):
        return (self.base_rate * self.base_time) + (self.commission_rate * self.commission_time)

    def __str__(self):

        contract = ""
        commission = ""

        if self.base_time > 1:
            contract = "hourly"
        else:
            contract = "monthly"

        if self.commission_rate > 0:
            if self.commission_time > 1:
                commission = "contract"
            else:
                commission = "bonus"
        else:
            commission = "none"

        if contract == "monthly":
            if commission == "none":
                return f"{self.name} works on a monthly salary of {self.base_rate}. Their total pay is {self.get_pay()}."
            elif commission == "contract":
                return f"{self.name} works on a monthly salary of {self.base_rate} and receives a commission for {self.commission_time} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.base_rate} and receives a bonus commission of {self.commission_rate}. Their total pay is {self.get_pay()}."
        else:
            if commission == "none":
                return f"{self.name} works on a contract of {self.base_time} hours at {self.base_rate}/hour. Their total pay is {self.get_pay()}."
            if commission == "contract":
                return f"{self.name} works on a contract of {self.base_time} hours at {self.base_rate}/hour and receives a commission for {self.commission_time} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.base_time} hours at {self.base_rate}/hour and receives a bonus commission of {self.commission_rate}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', base_rate=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', base_rate=25, base_time=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', base_rate=3000, commission_rate=200, commission_time=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', base_rate=25, base_time=150, commission_rate=220, commission_time=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', base_rate=2000, commission_rate=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', base_rate=30, base_time=120, commission_rate=600)