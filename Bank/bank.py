import random
from datetime import datetime

def Age(dob):
    dob = datetime.strptime(dob, '%d/%m/%Y')
    return (datetime.now() - dob).days // 365

def CreditCard():
    print("You want to apply for a credit card. (Yes/No)")
    ans = input().lower()
    if ans == 'yes':
        income = input("Enter your monthly income (in rupees): ").replace(',', "")
        try:
            income = int(income)
            if income >= 15000:
                print("Based on your income, you are eligible for a basic credit card.")
                print("We have Platinum, Gold, and Classic cards available.")
                choice = input("Which one would you like to apply for? ").lower()
                if choice in ['platinum', 'gold', 'classic']:
                    print("Thank you. Your", choice.capitalize(), "Card application is under process.")
                else:
                    print("We didn't recognize the card type. A Classic card will be issued.")
            else:
                print("Sorry, income is too low to be eligible for a credit card.")
        except:
            print("Invalid income entered.")
    else:
        print("Returning to main menu...\n")
        BANK()

def UPI():
    print("It seems you have a UPI issue. Please describe your problem:")
    print("1. Amount debited but not credited")
    print("2. UPI ID entered was wrong")
    print("3. Want to raise a complaint")
    try:
        issue = int(input("Select an option (1-3): "))
        if issue == 1:
            print("Amount usually gets refunded within 48 hours. Please wait.")
        elif issue == 2:
            print("Incorrect UPI ID transactions are not reversible unless recipient agrees.")
        elif issue == 3:
            print("A support ticket will be raised. You will get a response in 24 hours.")
        else:
            print("Invalid option.")
    except:
        print("Please enter a valid number.")

def LOAN():
    print("It seems you want to take a loan. (Yes/No)")
    a1 = input()
    if a1.lower() == 'yes':
        try:
            cibil = int(input("Enter your CIBIL score: "))
            if cibil < 650:
                print("Your CIBIL score is too low for loan approval.")
                return
            print("Which type of loan do you need? (Personal/Vehicle/Home)")
            ltype = input().lower()
            if ltype not in ['personal', 'vehicle', 'home']:
                print("Invalid choice. Proceeding with Personal loan.")
                ltype = 'personal'
            a = input("Do you have an existing bank account? (Yes/No)\n")
            if a.lower() == 'yes':
                ac = input("Enter your account number: ")
                h = input("Enter amount of loan required: ").replace(',', "")
                h = int(h)
                if ltype == 'vehicle' and h > 500000:
                    print("Vehicle loan cannot exceed 5 lakhs.")
                elif ltype == 'home' and h > 2000000:
                    print("Home loan limit exceeded. Max allowed: 20 lakhs.")
                else:
                    interest = {'personal': 11, 'vehicle': 9, 'home': 7}[ltype]
                    repay = h * (1 + interest / 100)
                    print(f"The {ltype} loan amount is {h}.\nAt {interest}% per year, repay amount is {repay:.2f}")
                    s = random.randint(2, 4)
                    if ltype == 'personal' and s % 2 == 0:
                        print("You have an existing personal loan of 68,713.20 rupees.\nNew loan will be sanctioned only after closing existing one.\n")
                    else:
                        print("Loan sanctioned. Amount will be credited shortly.")
            else:
                ACCOUNT()
        except:
            print("Some error occurred. Try again.")
    elif a1.lower() == 'no':
        BANK()

def ACCOUNT():
    print("It seems you want to open a new bank account. (Yes/No)")
    a1 = input()
    if a1.lower() == 'yes':
        name = input("ENTER YOUR NAME AS IN AADHAAR CARD: ")
        try:
            dob = input("Enter your date of birth (DD/MM/YYYY): ")
            age = Age(dob)
            if age >= 18:
                print("You are a major,", name, "and are eligible for a bank account.")
                print("What account would you like to open? (Current/Savings)")
                s = input().lower()
                if s == 'savings':
                    print("You shall maintain a minimum balance of 2000 rupees.")
                elif s == 'current':
                    print("A current account will be opened.")
                else:
                    print("Type not recognized. Savings account will be opened.")
                pan = input("Enter your PAN card number: ")
                s = random.randint(2, 4)
                if s % 2 == 0:
                    print("Congratulations! Account created.\nAccount number: 18045273681\n")
                else:
                    print("SORRY. Your PAN", pan, "is blacklisted.")
            else:
                print("You are a minor. Not eligible for bank account.")
        except:
            print("DOB not entered correctly.")
    LOAN()

def BANK():
    a = input("Hello User! What shall I call you? ")
    print("Hello", a, "how can I help you?")
    c = input().lower().split()

    upi = ['upi', 'online', 'transaction', 'stuck', 'payment', 'server']
    newac = ['bank', 'account', 'open', 'savings', 'current']
    loan = ['take', 'credit', 'loan', 'amount', 'due']
    credit = ['card', 'creditcard', 'apply', 'limit']

    for i in c:
        if i in upi:
            UPI()
            break
        elif i in newac:
            ACCOUNT()
            break
        elif i in loan:
            LOAN()
            break
        elif i in credit:
            CreditCard()
            break
    else:
        print("We hope we are helpful. THANK YOU")

BANK()

