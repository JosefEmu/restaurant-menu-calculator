#!/usr/bin/env python
"""
Address this problems
 - doesn't duplicate items in the receipt print out
 - allow for use by multiple customers without restarting the program everytime
"""


import time

def spacer():
	print("-"*33)
def t(secs):
	time.sleep(secs)

#menu= key:(item, price)
menu= {
	1 : ("Chicken strips", 35.0),
	2 : ("French Fries", 2.50),
	3 : ("Hamburger", 4.00),
	4 : ("Hotdog", 3.50),
	5 : ("Large Drink", 1.75),
	6 : ("Medium Drink", 1.50 ),
	7 : ("Milk Shake", 2.25),
	8 : ("Salad", 3.75),
	9 : ("Small Drink", 1.25)
}		

print("We have the following on menu today:")
for k in menu.values():
	print(f"{k[0]}...............at ${k[1]}")
	
new_order= ""
print()
while True:
	m= input("New Order: ")
	new_order+=m 
	if m== "":
		break
print("Your order is ready..\n")
t(1)

total= 0
print("Your order is as below: ")
spacer()

for i in new_order:
	n= int(i)
	print(menu[n][0], " at $", menu[n][1])
	total+=menu[n][1]

spacer()
print(f"Total=  $ {total}")
spacer()
