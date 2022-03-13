class atm:
    def __init__(self,cardnumber,Pin):
        self.cardnumber = cardnumber
        self.Pin = Pin
    def checkbalance(self):
        print("your balance is 50650")
    def withdrawl(self,amount):
        newAmount = 50650-amount
        print("u have withdrawn amount"+str(amount) + "your remaining balance is " + str(newAmount))

def main():
    cardNumber = input("enter your card number")
    cardPin = input("enter your card pin")
    newUser = atm(cardNumber,cardPin)
    print("choose your activity")
    print("1. balance enquiry 2. withdrawl")
    activity = int(input ("enter your activity number"))
    if (activity == 1):
        newUser.checkbalance()
    elif (activity == 2):
        amount = int(input ("enter the amount"))
        newUser.withdrawl(amount)
    else:
        print("enter a valid number")
if __name__ == "__main__":
    main()
