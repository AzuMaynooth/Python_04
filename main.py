'''

In this exercise, you are tasked to write a Python program that simulates operations on a company's account and a warehouse.
The program should handle various commands for performing operations like adding/subtracting balance, recording sales and purchases,
displaying account balance, showing warehouse status, and reviewing recorded operations.

Instructions:

1. Write a program that displays available commands upon launch. The commands are:
  - balance
  - sale
  - purchase
  - account
  - list
  - warehouse
  - review
  - end

2. Handle each command uniquely:
  - 'balance': The program should prompt for an amount to add or subtract from the account.
  - 'sale': The program should prompt for the name of the product,
  its price, and quantity.
  Perform necessary calculations and update the account and warehouse accordingly.

  - 'purchase': The program should prompt for the name of the product, its price, and quantity.
    Perform necessary calculations and update the account and warehouse accordingly.
    Ensure that the account balance is not negative after a purchase operation.

  - 'account': Display the current account balance.
  - 'list': Display the total inventory in the warehouse along with product prices and quantities.
  - 'warehouse': Prompt for a product name and display its status in the warehouse.
  - 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range.
  If ‘from’ and ‘to’ are empty, display all recorder operations.
  Handle cases where 'from' and 'to' values are out of range.
  - 'end': Terminate the program.

3. After executing any command, the program should again display the list of commands and prompt for the next command.

Hints:

- Use a loop to continuously prompt for commands until the 'end' command is entered.
- Keep track of the account balance and warehouse inventory.
- Remember to handle edge cases, like invalid command inputs, negative amounts during a 'purchase' operation, or out-of-range indices during a 'review' operation.
- The balance, sale, and purchase commands are remembered by the program.
- Handle user inputs that are not as expected. The program should not crash in these cases, but instead, it should display an appropriate error message.

'''
class Item:
  def __init__(self, name, amount, price):
    self.name = name
    self.amount = amount
    self.price = price

  def __str__(self):
      return f"[{self.name} {self.amount} {self.price}]"

def balance():
    print('-'*50,
          '\n Starting with balance calculations \n',
          '-'*50)

    global account_balance
    global operations

    try:
        op = input('What do you want to do?\n'
                   '1) add\n'
                   '2) subtract\n')
        amount = abs(int(input('Enter the amount: ')))

        if op == 'add':
            account_balance += amount

        elif op == 'subtract':

            if account_balance - amount >= 0:
                account_balance -= amount
            else:
                print('Balance is too low\n')

        operations.append(['Blance: ', amount])

    except ValueError:
        print('Please add numeric value. \n')

    print('Final account balance: ', account_balance)


def sale():
    print('-' * 50,
          '\n Starting with sale calculations \n',
          '-' * 50)

    global catalog
    global operations
    try:

        item_name = input('Add product name: ')
        item_amount = abs(int(input('Add items amount: ')))
        item_price = abs(float(input('Add price: ')))
        item = Item(item_name, item_amount, item_price)
        catalog.append(item)
        operations.append(['Sales', item_name, item_amount, item_price])
        print(*catalog)

    except ValueError:
        print('Please add numeric value. \n')

def purchase():
    global catalog
    global account_balance
    global operations

    print('-' * 50,
          '\n Starting with purchase calculations \n',
          '-' * 50)
    try:
        item_name = input('Add product name: ')
        item = None
        for it in catalog:
            if item_name == it.name:
                print('Product is available!')
                item = it
                break

        if item is None:

            print('Your item is not available')
        else:
            item_amount = abs(int(input('Add amount of items to buy: ')))

            if item.amount < item_amount:
                print('Not enough stock from that product to purchase.')
            else:
                print('Enough products available.')

                item.amount = item.amount - item_amount
                account_balance += item.price * item_amount
                print('After', account_balance)
                operations.append(['Purchase', account_balance])
    except ValueError:
        print('Your item is not available \n')
def account():
    print('-'*50,
          '\n Starting with balance calculations \n',
          '-'*50)
    print(account_balance)
def lista():
    print('-' * 50,
          '\n Catalog state \n',
          '-' * 50)
    print(*catalog)
def warehouse():
    global catalog
    global account_balance

    print('-' * 50,
          '\n Check if item is available on catalog \n',
          '-' * 50)
    try:
        check_product = input('Add product to check: ')
        item = None
        for it in catalog:
            if check_product == it.name:
                print('Product is available!')
                item = it
                print(item)
                break

        if item is None:
            print('Your item is not available')

    except ValueError:
        print('Your must be string \n')

def review():

    print('Select range of values to check in the operations')
    print(*operations, sep='\n')
    print(len(operations))
    start = abs(int(input('Add minimum value that you want to review: ')))
    stop = abs(int(input('Add maximum value that you want to review: ')))

    if 1 <= start <= len(operations) and 1 <= stop <= len(operations) and start <= stop:

        for index in range(start-1, stop):
            print(operations[index])
    else:
        print('please select a valid number between the range 1 and', len(operations))

def end():
    print('Program is terminated.')
    exit()

account_balance = 0
catalog = []
operations = []

commando = None

while commando != 'end':
    print('-' * 50,
          '\n Select one of the following options: \n',
          '-' * 50,
          '\n1) balance\n'
          '2) sale\n'
          '3) purchase\n'
          '4) account\n'
          '5) list\n'
          '6) warehouse\n'
          '7) review\n'
          '8) end\n')

    commando = input('Write option: ')

    if commando == 'balance':
        balance()
    elif commando == 'sale':
        sale()
    elif commando == 'purchase':
        purchase()
    elif commando == 'account':
        account()
    elif commando == 'list':
        lista()
    elif commando == 'warehouse':
        warehouse()
    elif commando == 'review':
        review()
    elif commando == 'end':
        end()
    else:
        print('Invalid input, try again, please.\n')