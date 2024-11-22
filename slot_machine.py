import random 

def deposit():
    """"Git the user's deposit amount."""
    while True:
        try:
            amount = float(input("enter the amount you what to deposit: $"))
            if amount > 0: 
                return amount
            else:
                print("The amount must be greater then Zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
            
def get_bet(balance):
    """Get the user's bet amount."""
    while True:
        try:
            bet = float(input("Enter your bet amount: $"))
            if 0 < bet <= balance:
                return bet
            else:
                print(f"Bet must be between $1 and your current balance of ${balance}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def spin_slot_machine():
    """Simulate spinning the slot machine."""
    symbols = ["🍒", "🍋", "🍊", "💎", "🔔"]  
    return [random.choice(symbols)for _ in range(3)]

def check_winnings(spin, bet) :
    """Determine winning based on the slot machine result.""" 
    if spin[0] == spin[1] == spin[2]:
        return bet * 5 # All three symbols match: 5x multiplier 
    elif spin[0] == spin[1] or spin[1] == spin[2] or spin[0] == spin [2]:
        return bet * 2 # Two symbols match: 2x multiplier
    return 0 # No matches: Lose bet

def main ():
    print("🎰 Welcome to the Slot Machine! 🎰")
    balance = deposit()
    
    while balance > 0 :
        print(f"Your current balance is: ${balance: .2f}")
        bet = get_bet(balance)
        print("Spinning the slot machine...")
        
        spin = spin_slot_machine()
        print(" | ".join(spin))
        
        winnings = check_winnings(spin, bet)
        if winnings > 0 :
            print(f"🎉 You won ${winnings:.2f}! 🎉")
            balance += winnings - bet 
            
        else:
            print("😢 You lost your bet. Better luck next time!")
            balance -= bet
            
            
        if balance == 0 :
            print("Your balance is $0. Game over.")
            break
        
        play_again = input("Do you want to play again? (y/n):").lower()
        if play_again != "y":
            break
        
    print(f"Thanks for playing! you left with ${balance: .2f}. Goodbye!")
    
if __name__ == "__main__":
    main()           