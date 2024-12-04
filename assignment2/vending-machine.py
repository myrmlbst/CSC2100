# ASSIGNMENT 2

# display menu in tabular form (number, item, price)
print(f"{'N'}{'Item':>10}{'Price':>10}")
print(f"{'1'}{'Twix':>10}{'1.25$':>10}")
print(f"{'2'}{'Snickers':>10}{'1.50$':>10}")
print(f"{'3'}{'KitKat':>10}{'1.00$':>10}")
print(f"4{'Leo':>10}{'0.75$':>10}")
print(f"5{'Juice':>10}{'1.00$':>10}")

# initialize variables to be used for calculations
choice = 0

twix_counter = 0
snickers_counter = 0
kitkat_counter = 0
leo_counter = 0
juice_counter = 0

# take user input and ask for quantity of each item
while choice != -1:
    choice = int(input("\nEnter your choice (or -1 to quit): "))

    if choice != -1:
        quantity = int(input("Enter your quantity: "))

        if choice == 1:
            twix_relative_price = (quantity * 1.25)
            print(quantity, "Twix added to cart for", twix_relative_price, "$")
            twix_counter += quantity
        if choice == 2:
            snickers_relative_price = (quantity * 1.50)
            print(quantity, "Snickers added to cart for", snickers_relative_price, "$")
            snickers_counter += quantity
        if choice == 3:
            kitkat_relative_price = (quantity * 1.00)
            print(quantity, "KitKat added to cart for", kitkat_relative_price, "$")
            kitkat_counter += quantity
        if choice == 4:
            leo_relative_price = (quantity * 0.75)
            print(quantity, "Leo added to cart for", leo_relative_price, "$")
            leo_counter += quantity
        if choice == 5:
            juice_relative_price = (quantity * 1.00)
            print(quantity, "Juice added to cart for", juice_relative_price, "$")
            juice_counter += quantity

# display final purchase information
print("\nYou've purchased the following:")
print(f"{'Item'}{'Quantity':>15}{'Price':>10}")

total_price = 0

if twix_counter >= 1:
    twix_total_price = twix_relative_price * twix_counter
    print(f"{'Twix'}{twix_counter:>9}{twix_relative_price:>15}")
    total_price += twix_relative_price
if snickers_counter >= 1:
    snickers_total_price = snickers_relative_price * snickers_counter
    print(f"{'Snickers'}{snickers_counter:>5}{snickers_relative_price:>15}")
    total_price += snickers_relative_price
if kitkat_counter >= 1:
    kitkat_total_price = kitkat_relative_price * kitkat_counter
    print(f"{'KitKat'}{kitkat_counter:>7}{kitkat_relative_price:>15}")
    total_price += kitkat_relative_price
if leo_counter >= 1:
    leo_total_price = leo_relative_price * leo_counter
    print(f"{'Leo'}{leo_counter:>10}{leo_relative_price:>15}")
    total_price += leo_relative_price
if juice_counter >= 1:
    juice_total_price = juice_relative_price * juice_counter
    print(f"{'Juice'}{juice_counter:>8}{juice_relative_price:>15}")
    total_price += juice_relative_price

print("\nYour total price is:", total_price)

# display discount (if applicable)
final_quantity = twix_counter + snickers_counter + kitkat_counter + leo_counter + juice_counter
if final_quantity >= 15:
    discount = total_price - (total_price / 10)
    print("More than 15 items were bought, 10% discount will be applied.")
    print("Your discounted total price is:", round(discount, 2))