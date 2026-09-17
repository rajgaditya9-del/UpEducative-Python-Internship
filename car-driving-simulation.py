#Author: Aditya Raj
#Assignment: Car Drive simulator
#Requirements:
#   1.A car (name, speedLimit, start(), stop(), speedUP(), speedDown(), showSpeed())
#   2.user can start the car 
#   3.user can see Speed,
#   4.can change speed (speedUp 10+, speedDown 10-)
#   5.can stop the car.
SEPARATOR="####################################"
GRAY="\033[90m"
RESET="\033[0m"
class Car:
    car_name = ""
    curr_speed = max_speed = 0.0
    bEngineStarted = False
    speed_increament = speed_decreament = 10
    def dashboard(self):
        if self.car_name is not None:
            print(f"{GRAY}[+] You are driving {self.car_name} at {self.curr_speed}km/hr and whose max speed is {self.max_speed}km/hr{RESET}")
        else:
            print(f"{GRAY}[!] Invalid car name={self.car_name}{RESET}")
    def Start(self):
        if not self.bEngineStarted:
            self.curr_speed = 0.0
            self.bEngineStarted = True
            print(f"{GRAY}[+] {self.car_name} Engine is started{RESET}")
        elif self.bEngineStarted:
            print(f"{GRAY}[+] {self.car_name} Engine already started{RESET}")
        self.dashboard()
    def Speedup(self):
        if self.bEngineStarted:
            if self.curr_speed >= 0.0 and self.curr_speed < self.max_speed:
                #0, 10, 20, 30, .... (always multiple of 10)
                self.curr_speed += self.speed_increament
            elif self.curr_speed == self.max_speed:
                print(f"{GRAY}[+] {self.car_name} is already running at max speed of {self.max_speed}km/hr{RESET}")
            self.dashboard()
        else:
            print(f"{GRAY}[+] {self.car_name} Engine is not started{RESET}")
    def Speeddown(self):
        if self.bEngineStarted:
            if self.curr_speed <= self.max_speed and self.curr_speed > 0.0:
                #30, 20, 10, 0, .... (always multiple of 10)
                self.curr_speed -= self.speed_decreament
            elif self.curr_speed == 0:
                print(f"{GRAY}[+] {self.car_name} is already stopped at speed of {self.max_speed}km/hr{RESET}")
            self.dashboard()
        else:
            print(f"{GRAY}[+] {self.car_name} Engine is not started{RESET}")
    def Stop(self):
        if self.bEngineStarted:
            self.bEngineStarted = False
            self.curr_speed = 0.0
            print(f"{GRAY}[+] {self.car_name} is Stopped{RESET}")
        else:
            print(f"{GRAY}[+] {self.car_name} is already Stopped{RESET}")
    def Operation(self):
        while(True):
            try:
                print(f"{SEPARATOR}")
                print("""1. Start
2. SpeedUp by 10
3. Speeddown by 10
4. Stop
5. Exit""")
                opIdx = int(input("Choose your operation index: "))
                if opIdx == 1: self.Start()
                elif opIdx == 2: self.Speedup()
                elif opIdx == 3: self.Speeddown()
                elif opIdx == 4: self.Stop()
                elif opIdx == 5: break
                else:
                    print(f"{GRAY}[!] Invalid input{RESET}")
            except ValueError:
                print(f"{GRAY}[-] You have been chosen a string, process terminated{RESET}")
                break


Ferrari = Car()
Ferrari.car_name = "Ferrai"
Ferrari.max_speed = 100
Ferrari.Operation()