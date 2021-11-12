alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = 'Dnes mame pekne pocasi!!'


def caesar(message, n):
    cipher = ''
    for i in message:
        if i.lower() not in alphabet:
            cipher += i
            continue
        nr = alphabet.index(i.lower())  # letter position
        nr_new = (nr + n) % len(alphabet)  # new position
        if i.isupper():
            enc = alphabet[nr_new].upper()
        else:
            enc = alphabet[nr_new]  # encrypted letter
        cipher += enc
    print(cipher)


caesar(text, -2)
