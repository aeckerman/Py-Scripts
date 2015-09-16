import time

string = input("What should I print?\n")
amount = float(input("How long should I wait?\n"))

print ("")
time.sleep(amount)
print (string)