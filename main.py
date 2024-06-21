import random

def generate_secret_combination():
    colors = ['rouge', 'bleu', 'vert', 'jaune', 'noir', 'blanc']
    return random.choices(colors, k=4)