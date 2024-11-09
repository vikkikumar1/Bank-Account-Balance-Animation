import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Bank Class with animation properties
class Bank:
    def __init__(self):
        self.sutter = False

    def start(self):
        self.sutter = True
        print("Machine starts...")

    def stop(self):
        self.sutter = False
        print("Machine stops...")


# Account Class
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        self.account_balance = [balance]  # Track balance changes

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.account_balance.append(self.balance)
            print("Rs", amount, "is debited from your account")

    def credit(self, amount):
        self.balance += amount
        self.account_balance.append(self.balance)
        print("Rs", amount, "is credited to your account")


# Initialize Bank and Account objects
bank = Bank()
account = Account(19000, 34567891233)

# Start Machine and Perform Transactions
bank.start()
time.sleep(1)

# Perform some transactions
account.debit(1000)
account.credit(500)
account.credit(3000)
account.debit(5000)
account.debit(50)
time.sleep(1)
bank.stop()

# Animation Code
fig, ax = plt.subplots()
x_data = list(range(len(account.account_balance)))
ax.set_xlim(0, len(x_data) - 1)
ax.set_ylim(0, max(account.account_balance) + 5000)
line, = ax.plot([], [], lw=3, color='blue')

# Initialization function for animation
def init():
    line.set_data([], [])
    return line,

# Update function for animation
def update(frame):
    x = x_data[:frame + 1]
    y = account.account_balance[:frame + 1]
    line.set_data(x, y)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=len(x_data), init_func=init, blit=True, interval=500, repeat=False)

# Plotting details
plt.title("Bank Account Balance Animation")
plt.xlabel("Transaction Steps")
plt.ylabel("Balance (Rs)")
plt.show()
