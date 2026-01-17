import random

def play_game():
    while True:
        x = random.randint(0, 1000)
        i = 1
        print("\n--- NEW GAME STARTED ---")
        
        while i <= 3:
            try:
                 a = int(input("Enter the number \U0001F604 : "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if a == x:
                print("YES, U GUESSED IT CORRECTLY \U0001F44F\U0001F44F!!!")             
                break
            else:
                print(f"NO, TRY AGAIN! ONLY {3-i} \U0001F612 ATTEMPTS REMAINING")
                i += 1
        
        if i > 3:
            print(f"GAME OVER! THE NUMBER WAS \U0001F62E : {x}")

        choice = input("\nDo you want to play again \U0001F638 ? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing! Goodbye.")
            input("Press Enter to exit...") 
            break

if __name__ == "__main__":
    play_game()




































































#NISHANK BISARIYA HAS THE RIGHT FOR THE ABOVE CODE 
