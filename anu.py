import random

moves = ["rock", "paper", "scissors"]

# Track player's move history
player_history = []

def ai_move():
    if not player_history:
        return random.choice(moves)

    # Predict player's most common move
    predicted = max(set(player_history), key=player_history.count)

    # AI plays the move that beats the predicted move
    if predicted == "rock":
        return "paper"
    elif predicted == "paper":
        return "scissors"
    else:
        return "rock"

def winner(player, ai):
    if player == ai:
        return "draw"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return "player"
    else:
        return "ai"

print("🎮 Rock Paper Scissors (Player vs AI)")
print("Type rock, paper, scissors or quit")

player_score = 0
ai_score = 0

while True:
    player = input("\nYour move: ").lower()

    if player == "quit":
        print("\nGame Over!")
        break

    if player not in moves:
        print("❌ Invalid move! Try again.")
        continue

    player_history.append(player)
    ai = ai_move()

    print(f"AI chose: {ai}")

    result = winner(player, ai)

    if result == "player":
        print("✅ You win this round!")
        player_score += 1
    elif result == "ai":
        print("❌ AI wins this round!")
        ai_score += 1
    else:
        print("🤝 It's a draw!")

    print(f"Score → You: {player_score} | AI: {ai_score}")

print(f"\nFinal Score → You: {player_score} | AI: {ai_score}")
print("Thanks for playing! 👋")
