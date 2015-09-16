import sys

quitQ = input("Type 'quit': ")

if quitQ == "quit":
	print ("Quiting...")
	sys.exit(0)
if quitQ == "Quit":
	print ("Quiting...")
else:
	print ("Oops you did'nt type 'quit'!")