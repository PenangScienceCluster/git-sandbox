import random

def slot_machine():
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎"]
    print("Welcome to the Slot Machine!")
    input("Press Enter to spin the reels...")

    # Spin the reels
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    # Display the result
    print("\n--- Slot Machine ---")
    print(f"| {reel1} | {reel2} | {reel3} |")
    print("--------------------")

    # Check for a win
    if reel1 == reel2 == reel3:
        print("🎉 Jackpot! You won! 🎉")
    elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
        print("😊 You got a small win!")
    else:
        print("😢 Better luck next time!")

# Run the slot machine
if __name__ == "__main__":
    slot_machine()