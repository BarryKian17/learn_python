class Resturant():
    menu = {
        'pizza':5000,
        'coke':1000,
        'Burger':5000,
        'pepsi':1000,
        'orange':1500
    }
    def __init__(self):
        self.total = 0
        self.orders = []
    def addOrder(self,order):
        self.orders.append(order)
        self.total+=self.menu[order]
    def printBill(self):
        for order in self.orders:
            print(f'{order} : {self.menu[order]}')
        print(f'Total - {self.total}')

def startProgram():
    table = Resturant()

    while True:
        order = input('order : ')
        table.addOrder(order)

        another = input('order more? y/n ')
        if another == 'y':
            continue
        else:
            table.printBill()
            break

startProgram()