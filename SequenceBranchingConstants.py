vcore = float(input("Enter voltage")) #step 1
multiplier = int(input("Enter Ratio Multiplier (example, 41 for 4100MHz)"))#step 2
baseclock = int(input("Enter Base Clock (example, 100MHz)"))# step
clockspeed = baseclock*multiplier # step 
test = str(input("Would you like a basic analysis of your settings?"))
response = test.lower()


def vcoretest(vcore):
    if vcore >= 1.51:
          print("\nYour voltage should be between 1 and 1.5 (a lower voltage is better and won't strain the VRMs, Mosfets or thermal limits as much")
    else:
        print("\nYour vcore is good!")
def multipliertest(multiplier):
    if 49 >= multiplier >=54:
        print("\nYour all core multiplier may be too high for safe operations, you should have a multiplier that is lower than 54 on Intel, however your systems stability may vary based on how well your chip can overclock.")
    elif multiplier <= 49:
        print("\nYour system should run fine with this multiplier!")
    elif multiplier >= 55:
        print("call the fire brigade")
    else:
        print("not sure how you got here, but hey!")

if response == "yes":
    print("Only accurate for Ryzen 3000 and Intel Core 10th Generation")
    vcoretest(vcore)
    multipliertest(multiplier)

                   
