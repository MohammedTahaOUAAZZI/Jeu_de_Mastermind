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




    
