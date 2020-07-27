class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is $9999")

    def withdrawl(self,amount):
        new_amount = 9999 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    Card_number = input("insert your card number:-\n ")
    pin_number  = input("enter your pin number:-\n ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy")
    print("2.withdrawl")
    activity = int(input("enter activity number :-\n "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:-\n "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number\n")


if __name__ == "__main__":
    main()