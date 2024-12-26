import pyinputplus as pyip

def main():
    bread_types = ["wheat", "white", "sourdough"]
    protein_types = ["chicken", "turkey", "ham", "tofu"]
    cheese_types = ["cheddar", "Swiss", "mozzarella"]
    condiments = ["mayo", "mustard", "lettuce", "tomato"]

    bread = pyip.inputMenu(bread_types,prompt="Choose your bread type:\n",numbered=True)
    protein = pyip.inputMenu(protein_types,prompt="Choose your protein type:\n",numbered=True)
    want_cheese = pyip.inputYesNo(prompt="Do you want cheese? (y/n)") == "yes"
    cheese = None
    if want_cheese:
        cheese = pyip.inputMenu(cheese_types,prompt="Choose your cheese type:\n",numbered=True)
    want_condiments = {condiment: pyip.inputYesNo(prompt=f"Do you want {condiment} (y/n)?") == "yes"
                       for condiment in condiments}
    num_sandwiches = pyip.inputInt(prompt="How many sandwiches would you like?",min=1)

    prices = {
        "bread": 1.00,
        "protein": 2.00,
        "cheese": 0.50,
        "condiments": 0.25
    }

    total_price = ((prices["bread"] + prices["protein"] + (prices["cheese"] if want_cheese else 0) +
                   sum(prices["condiments"] for cond in want_condiments.values() if cond))
                   * num_sandwiches)

    print("\nYour order summary:")
    print(f"Bread: {bread}")
    print(f"Protein: {protein}")
    if want_cheese:
        print(f"Cheese: {cheese}")
    for condiment, wanted in want_condiments.items():
        if wanted:
            print(f"Condiment: {condiment}")
    print(f"Number of sandwiches: {num_sandwiches}")
    print(f"Total price: ${total_price:.2f}")

if __name__ == "__main__":
    main()
