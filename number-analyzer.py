#Author: Aditya Raj
#Assignment: Number Analyzer
#Create a Number Analyzer using Python
#Requirements:
#Take integer n as input
#Generate numbers from 1 to n
#Check each number for even or odd
#Calculate the sum of even numbers
#Calculate the sum of odd numbers
#Calculate the total sum
#Check whether the total sum is even or odd
#Display the results
SEPARATOR="####################################"
GRAY="\033[90m"
RESET="\033[0m"
def num_analyzer():
    try:
        print(f"{SEPARATOR}")
        last_num = int(input("Enter the last number from 1 to "))
        if last_num < 0:
            print(f"{GRAY}[!] Invalid last number{RESET}")
            return
        even_sum = 0
        odd_sum = 0
        for iter in range(1, last_num + 1):
            if iter % 2 == 0:
                even_sum += iter
            elif iter %2 != 0:
                odd_sum += iter
            else:
                print(f"{GRAY}[!] Invalid iter%2 value{RESET}")
        total_sum = even_sum + odd_sum
        print(f"{GRAY}[+] Total sum: {total_sum}{RESET}")
        print(f"{GRAY}[+] Even Sum: {even_sum}{RESET}")
        print(f"{GRAY}[+] Odd Sum: {odd_sum}{RESET}")
        print(f"{GRAY}[+] Total Sum {total_sum} is Even{RESET}" if total_sum % 2 == 0 else f"{GRAY}[+] Total sum {total_sum} is Odd{RESET}")
    except ValueError:
        print(f"{GRAY}[-] You have been chosen a string, process terminated{RESET}")
        return


num_analyzer()