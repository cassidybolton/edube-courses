# pcpp1 practice: encapsulation
# attribute encapsulation; @property; getters, setters, and deleters

class AccountError(Exception):
    pass

class BankAccount():
    num_tracker = 0
    def __init__(self, starting_bal=0):
        BankAccount.num_tracker += 1
        self.__account_no = str(BankAccount.num_tracker).zfill(5)
        self.__balance = starting_bal

    @property
    def account_no(self):
        return self.__account_no
    
    @account_no.setter
    def account_no(self, *args):
        raise AccountError('Account number may not be changed')
    
    @account_no.deleter
    def account_no(self):
        if self.__balance > 0:
            raise AccountError('Account with positive balance may not be deleted')
        else:
            self.__account_no = None
            print('Account has been deleted')

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, num):
        if num < 0:
            raise AccountError('Balance may not be set to a negative amount')
        
    @balance.deleter
    def balance(self):
        raise AccountError('Account balance info may not be deleted')
        
    def deposit(self, num):
        if num >= 0:
            self.__balance += num
            if num >= 100000:
                print('Large transaction alert: This transaction will be audited')
        else:
            raise AccountError('Amount must be positive')
        
    def withdraw(self, num):
        if num >= 0:
            self.__balance -= num
            if num >= 100000:
                print('Large transaction alert: This transaction will be audited')
        else:
            raise AccountError('Amount must be positive')

# testing
account = BankAccount(1000)
print(f'#{account.account_no}, ${account.balance}')
account.balance = 200
print(f'#{account.account_no}, ${account.balance}')
account.deposit(1000000)
print(f'#{account.account_no}, ${account.balance}')
del account.account_no
print(f'#{account.account_no}, ${account.balance}')