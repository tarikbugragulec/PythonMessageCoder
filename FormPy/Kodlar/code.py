
class Codes():
    def Encode(stringdeger):
        encoded_string = ""
        for char in stringdeger:
            if char.isspace() or char == "!":
                # Eğer karakter sayı, boşluk veya ünlem ise aynı karakteri kodlanmadan ekleyelim
                encoded_string += char
            elif char.isdigit():
                if char== '9':
                   char = '0'
                   encoded_string += char
                else :
                    deger= ord(char) + 1
                    nxt_char=chr(deger)
                    encoded_string += nxt_char   
            else:
                # Eğer karakter bir harf ise, bir sonraki harfi elde edelim ve kodlanmış metine ekleyelim
                next_unicode_value = ord(char) + 1
                next_char = chr(next_unicode_value)
                encoded_string += next_char
        return encoded_string

    def Decode(encoded_string):
        decoded_string = ""
        for char in encoded_string:
            if char.isspace() or char == "!":
                # Eğer karakter sayı, boşluk veya ünlem ise aynı karakteri çözücüde ekleyelim
                decoded_string += char
            elif char.isdigit():
                if char == '0':
                    char = '9'
                else:
                    char = str(int(char) - 1)
                decoded_string += char
            else:
                # Eğer karakter bir harf ise, bir önceki harfi elde edelim ve çözücü metine ekleyelim
                prev_unicode_value = ord(char) - 1
                prev_char = chr(prev_unicode_value)
                decoded_string += prev_char
        return decoded_string
            


