

def count(word: str) -> int:
    word_len = len(word.replace(" ",""))
    return word_len


word_to_count = count(str(input('Entrez un mot :')))
print(f'Votre mot à une longueur de {word_to_count} caractères.')