#Author: Aditya Raj
#Assignment: Login System
#Create a simple login system using Python
#Requirements:
#   1.Create a function login()
#   2.Store a username and password
#   3.Give the user a maximum of 3 attempts to enter the correct credentials
#   4.Use a loop to allow multiple attempts
#   5.Use conditional statements to check whether the username and password are correct
#   6.Use an assignment operator such as attempts +=1
#   7.If the user enters the correct details, display:
#       Login successful!
#   8.After 3 incorrect attempts, display:
#       Account locked!
SEPARATOR="####################################"
GRAY="\033[90m"
RESET="\033[0m"
def login():
    g_userName="admin"
    g_userPass="123"
    max_attempt=2 #0, 1, 2
    curr_attempt=0
    IsLocked=False
    while(curr_attempt < 3 and not IsLocked):
        print(f"{SEPARATOR}")
        try:
            curr_userName=str(input("Enter Your UserName:"))
            curr_userPass=str(input("Enter Your Password:"))
            if len(curr_userName) > 0 and len(curr_userPass) > 0:
                if curr_userName==g_userName and curr_userPass==g_userPass:
                    print(f"{GRAY}[+] Login successful{RESET}")
                    break
                else:
                    print(f"{GRAY}[!] Incorrect username or password.\nAttempts remaining: {max_attempt-curr_attempt}{RESET}")
                    if curr_attempt==max_attempt:
                        IsLocked=True
                    curr_attempt+=1
            else:
                print(f"{GRAY}[!] Invalid credentials{RESET}")
        except ValueError:
            print(f"{GRAY}[-] You have been chosen a string, process terminated{RESET}")
            return
    else:
        print(f"{GRAY}[-] Account locked{RESET}")

login()