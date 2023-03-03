class Statistics:
    def __init__(self, data):
        self.data = data
        
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return max(self.data) - min(self.data)
    
    def mean(self):
        return sum(self.data) / len(self.data)
    
    def median(self):
        sorted_data = sorted(self.data)
        n = len(self.data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]
    
    def mode(self):
        freq_dict = {}
        for num in self.data:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        mode_count = max(freq_dict.values())
        modes = [num for num, freq in freq_dict.items() if freq == mode_count]
        return {'mode': modes[0], 'count': mode_count}
    
    def std(self):
        import math
        n = len(self.data)
        mean = sum(self.data) / n
        deviations = [(x - mean) ** 2 for x in self.data]
        variance = sum(deviations) / (n - 1)
        return math.sqrt(variance)
    
    def var(self):
        n = len(self.data)
        mean = sum(self.data) / n
        deviations = [(x - mean) ** 2 for x in self.data]
        variance = sum(deviations) / (n - 1)
        return variance
    
    def freq_dist(self):
        freq_dict = {}
        for num in self.data:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        return freq_dict
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) 
print('Sum: ', data.sum()) 
print('Min: ', data.min()) 
print('Max: ', data.max()) 
print('Range: ', data.range()) 
print('Mean: ', data.mean()) 
print('Median: ', data.median()) 
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.std()) 
print('Variance: ', data.var()) 
print('Frequency Distribution: ', data.freq_dist())
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()

    def add_income(self, description, amount):
        self.incomes.add((description, amount))

    def add_expense(self, description, amount):
        self.expenses.add((description, amount))

    @property
    def total_income(self):
        return sum(amount for _, amount in self.incomes)

    @property
    def total_expense(self):
        return sum(amount for _, amount in self.expenses)

    @property
    def account_balance(self):
        return self.total_income - self.total_expense

    @property
    def account_info(self):
        return f"{self.firstname} {self.lastname}:\nIncome: {self.incomes}\nExpense: {self.expenses}\nBalance: {self.account_balance}"


person = PersonAccount("mohammed", "nasir")


person.add_income("Salary", 5000)
person.add_income("Bonus", 1000)
person.add_expense("Rent", 2000)
person.add_expense("Groceries", 500)

print(person.account_info)
