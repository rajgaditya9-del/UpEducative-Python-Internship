#Author: Aditya Raj
#Assignment: ATM Simulation
#Create a simple ATM program using Python
#Requirements:
#Create a function atm()
#Start with a balance of Rs10000
#Display a menu:
#   1.Check Balance
#   2.Deposit
#   3.Withdraw
#   4.Exit
#Use a loop so the menu keeps appearing until the user chooses Exit
#Use conditional statements to perform the selected operation
#Use assignment operators such as += and = deposits and withdrawals
#Do not allow withdrawal if the amount is greater than the avaialbale balance
#Display the updated balance after every transaction
SEPARATOR="####################################"
GRAY="\033[90m"
RESET="\033[0m"
def atm():
    def __checkinBal(orig_amount):
      print(f"{GRAY}[+] curr amount: Rs{orig_amount}{RESET}")
    def __add(orig_amount, amount):
      orig_amount+=amount
      __checkinBal(orig_amount)
    def __sub(orig_amount, amount):
      orig_amount-=amount
      __checkinBal(orig_amount)
    orig_amount=10000.0
    orig_pin=123
    curr_pin=int(input("Enter your atm card pin: "))
    while curr_pin==orig_pin:
        print(f"{SEPARATOR}")
        print("""[+] Choose an option:
    1.Check Balance
    2.Deposit
    3.Withdraw
    4.Exit""")
        user_in = int(input("Select any above option: "))
        print(f"{GRAY}[+] You have chosen an option {user_in}{RESET}")
        if user_in==1:
            __checkinBal(orig_amount)
        elif user_in==2:
            dep_amount=float(input("Enter your deposit amount: Rs"))
            if dep_amount > 0:
                __add(orig_amount, dep_amount)
            else:
                print(f"{GRAY}[!] Invalid deposit input{RESET}")
        elif user_in==3:
            withd_amount=float(input("Enter your withdrawal amount: Rs"))
            if withd_amount > 0 and withd_amount <= orig_amount:
                __sub(orig_amount, withd_amount)
            else:
                print(f"{GRAY}[-] Invalid withdrawal input!{RESET}")
        elif user_in==4:
            print(f"{GRAY}[-] ===Exit==={RESET}")
            break
        else:
            print(f"{GRAY}[!] Invalid option{RESET}")
    else:
      print(f"{GRAY}[-] Wrong atm card pin{RESET}")


atm()