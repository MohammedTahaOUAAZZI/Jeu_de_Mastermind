import random

def generate_secret_combination():
    colors = ['rouge', 'bleu', 'vert', 'jaune', 'noir', 'blanc']
    return random.choices(colors, k=4)


def get_user_combination():
    colors = ['rouge', 'bleu', 'vert', 'jaune', 'noir', 'blanc']
    while True:
        user_input = input("Entrez une combinaison de 4 couleurs (rouge, bleu, vert, jaune, noir, blanc) séparées par des espaces: ").strip().lower().split()
        if len(user_input) == 4 and all(color in colors for color in user_input):
            return user_input
        else:
            print("Entrée invalide. Assurez-vous d'entrer exactement 4 couleurs parmi les suivantes: rouge, bleu, vert, jaune, noir, blanc. Essayez de nouveau.")

def give_feedback(secret, guess):

    correct_position = 0
    correct_colors = 0
    secret_copy = secret[:]
    guess_copy = guess[:]

    
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            correct_position += 1
            secret_copy[i] = None
            guess_copy[i] = None

    
    for g in guess_copy:
        if g and g in secret_copy:
            correct_colors += 1
            secret_copy[secret_copy.index(g)] = None

    return '*' * correct_position + '-' * correct_colors

def mastermind_game():

    secret_combination = generate_secret_combination()
    max_attempts = 10
    print("Bienvenue au Mastermind!")
    print("Vous devez deviner une combinaison de 4 couleurs parmi rouge, bleu, vert, jaune, noir, blanc.")
    print(f"Vous avez {max_attempts} tentatives pour deviner la combinaison secrète.")

    for attempt in range(1, max_attempts + 1):
        print(f"\nTentative {attempt}/{max_attempts}")
        user_combination = get_user_combination()
        feedback = give_feedback(secret_combination, user_combination)
        print(f"Indices : {feedback}")

        if feedback == '****':
            print("Félicitations! Vous avez deviné la combinaison secrète.")
            break
    else:
        print(f"Vous avez épuisé toutes vos tentatives. La combinaison secrète était: {' '.join(secret_combination)}")

if __name__ == "__main__":
    mastermind_game()


    
