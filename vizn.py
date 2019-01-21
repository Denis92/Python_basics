import random


class Transform_words:
    """a class for generating the correct code word and converting input words to a list of individual characters"""

    def __init__(self, input_word, input_code_w="cat", input_code_num="123"):
        self.input_word = input_word
        if self.input_word.isalpha():
            self.input_code = input_code_w
            self.input_word = self.input_word.lower()
            self.input_code = self.input_code.lower()
            self.list_dictionary = [_ for _ in range(ord('a'), ord('z') + 1)]
        elif self.input_word.isdigit():
            self.input_code = input_code_num
            self.list_dictionary = [_ for _ in range(ord('0'), ord('9') + 1)]

    def transform_intup_word(self):
        """converting the input word into a list of characters"""
        list_word = list(self.input_word)
        return list_word

    def transform_code_words(self):
        """code word formation"""
        temp_list_code = list(self.input_code)
        list_code = []
        while len(self.transform_intup_word()) != len(list_code):
            for i in temp_list_code:
                if len(list_code) != len(self.transform_intup_word()):
                    list_code.append(i)
                else:
                    break
        return list_code


class Encryption(Transform_words):
    """Class for encoding and decoding words"""

    def __init__(self, input_words, coded_words, coded_num):
        super().__init__(input_words, coded_words, coded_num)
        self.keyword = self.transform_code_words()
        self.input_words = self.transform_intup_word()
        self.val_start = self.list_dictionary[0]
        # random.shuffle(self.list_dictionary) #to generate a random word table

    def shift_f(self, i):
        """character shift function to form a string"""
        temp_input_list = self.list_dictionary[i:].copy()
        for _ in range(i):
            temp_input_list.append(self.list_dictionary[_])
        return temp_input_list

    def matrix_code_list(self):
        """the formation of a table for encoding and decoding"""
        matrix_output = [self.shift_f(i) for i in range(len(self.list_dictionary))]
        return matrix_output

    def coded_words(self):
        """the coding function"""
        temp_list = self.matrix_code_list()
        encode_words = []
        for i in range(len(self.input_words)):
            encode_words.append(
                chr(temp_list[ord(self.input_words[i]) - self.val_start][ord(self.keyword[i]) - self.val_start]))
        return encode_words

    def decoded_word(self):
        """decode function"""
        temp_list = self.matrix_code_list()
        temp_coded_list = self.coded_words()
        decode_words = []
        for j in range(len(temp_coded_list)):
            for i in range(len(temp_list)):
                if temp_list[ord(self.keyword[j]) - self.val_start][i] == ord(temp_coded_list[j]):
                    decode_words.append(chr(i + self.val_start))
        return decode_words


code_w = "cat"
code_n = "123"
input_text = input("Input your text in english language: ").split(" ")
encode_word = []
decode_word = []
for i in input_text:
    crypt = Encryption(i, code_w, code_n)
    encode_word.append("".join(crypt.coded_words()))
    decode_word.append("".join(crypt.decoded_word()))
print(" ".join(encode_word))
print(" ".join(decode_word))
