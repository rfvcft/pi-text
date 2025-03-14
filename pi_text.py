import pyfiglet
from mpmath import mp


def pi_text(text, symbol="#"):
    ascii_text = pyfiglet.figlet_format(text, font="banner3-D")

    d = ascii_text.count(symbol)
    mp.dps = d-1
    pi = str(mp.pi)

    digit_count = 0
    pi_text = ""
    for i, char in enumerate(ascii_text):
        if char == symbol:
            pi_text += pi[digit_count]
            digit_count += 1
        else:
            pi_text += char

    header = "\n"*5 + "="*60 + "\n"*5
    
    return header + pi_text + header

if __name__ == '__main__':
    text = "GRATTIS LOVISA!"
    print(pi_text(text))
