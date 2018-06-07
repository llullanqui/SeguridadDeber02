def caesar(ciphertext):
    decifrado = ""
    for caracter in ciphertext:
        if ord(caracter)<ord('A') or ord(caracter)>ord('Z'):
            decifrado += caracter
        else:
            val = ord(caracter)
            val -= 3
            if val<65:
                val+=26
            decifrado += chr(val)
    return decifrado

def atbash(ciphertext):
    decifrado = ""
    for caracter in ciphertext:
        if ord(caracter)<ord('A') or ord(caracter)>ord('Z'):
            decifrado += caracter
        else:
            decifrado += chr(ord('A') + ord('Z') - ord(caracter))
    return decifrado

#print("deciframiento: ", caesar(input("Texto a decifrar con Caesar: ")))
#print("deciframiento: ", atbash(input("Texto a decifrar con atbash: ")))