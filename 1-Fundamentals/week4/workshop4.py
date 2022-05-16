class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, 'has a balance of:', self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, user, amount):
        print('You are transfering $' + str(amount), 'to', user.name)
        if int(input('Enter your pin: ')) == self.pin:
            self.withdraw(amount)
            user.deposit(amount)
            return True
        else:
            print('Invalid PIN')
            return False

    def request_money(self, user, amount):
        print('You are requesting $' + str(amount), 'from', user.name)
        if int(input('Enter your PIN: ')) != self.pin:
            print('Invalid PIN')
            return False
        elif input("Enter " + user.name + "'s password: ") != user.password:
            print('Invalid password')
            return False
        else:
            user.withdraw(amount)
            self.deposit(amount)
            return True

        # Driver Code for Task 1
        #bob = User("Bob", 1234, "password")
        #print(bob.name, bob.pin, bob.password)

        # Driver Code for Task 2
        #bob = User("Bob", 1234, "password")
        #print(bob.name, bob.pin, bob.password)
        # bob.change_name('Bobby')
        # bob.change_pin(4321)
        # bob.change_password('newpassword')
        #print(bob.name, bob.pin, bob.password)

        # Driver Code for Task 3
        #bob = BankUser('Bob', 1234, 'password')
        #print(bob.name, bob.pin, bob.password, bob.balance)

        # Driver Code for Task 4
        #bob = BankUser('Bob', 1234, 'password')
        # bob.show_balance()
        # bob.deposit(500)
        # bob.show_balance()
        # bob.withdraw(250)
        # bob.show_balance()


# Driver Code for Task 5
bob = BankUser('Bob', 1234, 'password123')
billy = BankUser('Billy', 321, 'billy123')
billy.deposit(5000)
billy.show_balance()
bob.show_balance()
print()

if billy.transfer_money(bob, 500):
    billy.request_money(bob, 250)
billy.show_balance()
bob.show_balance()
