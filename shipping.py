"""
Sal's Shippers - Shipping Cost Calculator

This program calculates the cheapest shipping option based on package weight.
"""

weight = 41.5
cost = None
ground_rate = 20
drone_rate = 0
premium_rate = 125

# ground Shipping
if weight <= 2:
  cost = 1.5 * weight + ground_rate
  print("Ground shipping cost : $" , cost)

elif weight <= 6:
  cost = 3 * weight + ground_rate
  print("Ground shipping cost : $" , cost)

elif weight <= 10:
  cost = 4 * weight + ground_rate
  print("Ground shipping cost : $" , cost)

else:
  cost = 4.75 * weight + ground_rate

  print("Ground shipping cost : $" , cost)

# premium shipping
print("Ground Shipping Premium $", premium_rate)


# drone Shipping
if weight <= 2:
  cost = 4.5* weight + drone_rate
  print("Drone shipping cost : $" , cost)

elif weight <= 6:
  cost = 9 * weight + drone_rate
  print("Drone shipping cost : $" , cost)

elif weight <= 10:
  cost = 12 * weight + drone_rate
  print("Drone shipping cost : $" , cost)

else:
  cost = 14.25 * weight + drone_rate

  print("Drone shipping cost : $" , cost)






