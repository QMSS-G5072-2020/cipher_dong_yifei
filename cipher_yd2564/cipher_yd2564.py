def cipher(text, shift, encrypt=True):
    """
    Encrypts or decrypts the alphabetical portion of strings based on a given
    integer value of shift.

    Parameters
    ----------
    text : str
        A string that you want to encrypt/decrypt.
    shift : int
        An integer by which you want to shift the value of a letter.
    encrypt : bool
        A boolean indicating whether you want to apply the encrypt (True)
        or decrypt (False) of the text.

    Returns
    -------
    str
        The encrypted/decrypted text

    Example
    -------
    >>> from cipher_yd2564 import cipher_yd2564
    >>> text = "Happy Coding!"
    >>> shift = 1
    >>> cipher_yd2564.cipher(text, shift, encrypt = True)
    'Ibqqz Dpejoh!'
    >>> text = 'Ibqqz Dpejoh!'
    >>> cipher_yd2564.cipher(text, shift, encrypt = False)
    'Happy Coding!'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
