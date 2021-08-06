def converter(pesos_type, dollar_value):
    pesos = input("How many " + pesos_type + " pesos do you have?: ")
    pesos = float(pesos)
    dollars = pesos / dollar_value
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")


menu = """
Welcome to the currency converter 💰

1 - Colombian pesos
2 - Argentinian pesos
3 - Mexican pesos

Choose an option: """

option = input(menu)

if option == "1":
    converter("colombian", 3875)
elif option == "2":
    converter("argentinian", 65)
elif option == "3":
    converter("mexican", 24)
else:
    print("Write a correct option")

