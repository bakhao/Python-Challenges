import string

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st: str):

        st_encode = " "
        shift_target = 0
        alphabets = list(string.ascii_lowercase)
        st = st.lower()
        print(st)
        for i in st:
            st_encode += chr(ord(i) + self.shift)
        return st_encode.upper()

    def decode(self, st):
        pass