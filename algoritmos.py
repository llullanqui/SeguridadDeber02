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

def A1Z26(ciphertext):
    decifrado = ""
    i = 0
    while i < len(ciphertext):
        if ciphertext[i] == "-":
            decifrado += ""
        elif ord(ciphertext[i])<ord('0') or ord(ciphertext[i])>ord('9'):
            decifrado += ciphertext[i]
        else:
            if ord('0') <= ord(ciphertext[i+1]) <= ord('9'):
                decifrado += chr(int(ciphertext[i:i+2])+ord('A')-1)
                i += 1
            else:
                decifrado += chr(int(ciphertext[i])+ord('A')-1)
        i += 1
    return decifrado

def combined(ciphertext):
    return caesar(atbash(A1Z26(ciphertext)))



#print("deciframiento: ", caesar(input("Texto a decifrar con Caesar: ")))
#print("deciframiento: ", atbash(input("Texto a decifrar con atbash: ")))
#print("deciframiento: ", A1Z26(input("Texto a decifrar con A1Z26: ")))
#print("combined: ", combined(input("Texto a decifrar con combined cipher: ")))
