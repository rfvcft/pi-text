import pyfiglet
from mpmath import mp


def pi_text(text, fill=True, custom_stream=None):
    """
    Create ascii art of the given text `text`.
    If `fill` is True, have a background to the text which creates a "3D-effect"
    If `custom_stream` is given then this string (repeated) will be used to fill the text in the ascii art
    If `custom_stream` is not given (being None), the digits of pi is used as default
    """

    symbol = "#"
    fill_symbs = [":", ".", "'"]

    ascii_text = pyfiglet.figlet_format(text, font="banner3-D")

    d = ascii_text.count(symbol)

    if custom_stream is None:
        # If no custom stream is defined, let the stream be the right amount of digits of pi
        mp.dps = d-1
        stream = str(mp.pi)
    else:
        # Otherwise, repeat the custom stream until it is longer than the required length
        stream = custom_stream
        while len(stream) < d:
            stream += custom_stream

    digit_count = 0
    out_text = ""
    for char in ascii_text:
        if char == symbol:
            out_text += stream[digit_count]
            digit_count += 1

        elif not fill and char in fill_symbs:
            out_text += " "

        else:
            out_text += char

    header = "\n"*5 + "="*60 + "\n"*5

    return header + out_text + header

if __name__ == '__main__':
    text = "GRATTIS LOVISA!"
    stream = "peepeepoopoo"
    print(pi_text(text, fill=False, custom_stream=stream))

