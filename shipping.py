"""
Sal's Shippers - Shipping Cost Calculator

This program calculates the cheapest shipping option based on package weight.
"""

weight = 1.5
cost = None
drone_rate = 0


# drone Shipping
if weight <= 2:
  cost = 4.5* weight + drone_rate

elif weight <= 6:
  cost = 9 * weight + drone_rate

elif weight <= 10:
  cost = 12 * weight + drone_rate

else:
  cost = 14.25 * weight + fdrone_rate

print(cost)




