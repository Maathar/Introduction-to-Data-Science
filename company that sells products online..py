"""Suppose you work for a company that sells products online. 
Your boss has asked you to create a decision tree to help them 
decide whether or not to launch a new product. 
Here's the data you have:
• The cost to manufacture the product is $20 per unit.
• The price at which the product can be sold is $40 per unit.
• The fixed cost to launch the product is $50,000.
• The estimated demand for the product is 10,000 units.
Here are the possible outcomes:
• If the product is launched and demand is greater than or equal 
to 10,000 units,the company will make a profit of $200,000.
• If the product is launched and demand is less than 10,000 units,
the company will make a profit of $100,000.
• If the product is not launched, the company will not make any
 profit or loss.
 Your task is to create a decision tree to help your boss decide 
 whether or not to launch the new product. Use the data provided 
 above to determine the expected value of each decision.
 Once you have created the decision tree, calculate the expected 
 value of launching the product and not launching the product.
 Based on your analysis, what recommendation would you give your 
 boss?"""

# Define the variables
cost = 20
price = 40
fixed_cost = 50000
demand = 10000

# Define the outcomes
profit_high = 200000
profit_low = 100000
no_profit = 0

# Calculate the expected values
launch_profit = (demand * (price - cost) - fixed_cost) * (demand >= 10000) + profit_low * (demand < 10000)
no_launch_profit = no_profit

# Print the results
print("Expected profit if launched: $" + str(launch_profit))
print("Expected profit if not launched: $" + str(no_launch_profit))

# Make a recommendation
if launch_profit > no_launch_profit:
    print("Recommendation: Launch the new product")
else:
    print("Recommendation: Do not launch the new product")
    
"""Based on the expected profit analysis, I would recommend that
 the boss launches the new product, as the expected profit is
 positive and higher than the expected profit if the product is 
 not launched."""