class Bank:
    bank_name = 'SBI'
    def __init__(self, name, age, bal):
        self.user_name = name
        self.age = age
        self.user_balance = bal

    def get_info(self):
        print(f'''User Name: {self.user_name} and balance: {self.user_balance}, Bank Name: {Bank.bank_name}''');
b1 = Bank('Ashu', 24, 28000)
print(b1.bank_name) # SBI
print(Bank.bank_name) # SBI
b1.get_info()