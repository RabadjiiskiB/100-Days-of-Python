import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
natoAlphabet = {row["letter"]: row["code"] for (index, row) in df.iterrows()}
while True:
    userI = input("Enter your name ").upper()
    try:
        word = [natoAlphabet[s] for s in userI]
    except KeyError:
        print("Should contain only letters")
    else:
        print(word)
        break

