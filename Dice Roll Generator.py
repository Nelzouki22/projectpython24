import random

def roll_dice(num_rolls):
    results = []
    for _ in range(num_rolls):
        roll_result = random.randint(1, 6)
        results.append(roll_result)
    return results

def main():
    num_rolls = int(input("Enter the number of dice rolls: "))
    dice_results = roll_dice(num_rolls)
    
    print("\nDice Rolls:")
    for i, result in enumerate(dice_results, start=1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
