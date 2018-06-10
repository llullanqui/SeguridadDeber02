def caesar(ciphertext):
    decifrado = ""
    for caracter in ciphertext:
        if ord(caracter)<ord('A') or ord(caracter)>ord('Z'):
            decifrado += caracter
        else:
            val = ord(caracter)
            val -= 3
            if val<ord('A'):
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
    ciphertext+=" "
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

listaDeSoluciones = ["WELCOMETOGRAVITYFALLS.",
                     "NEXTWEEKRETURNTOBUTTISLAND.",
                     "HESSTILLINTHEVENTS.",
                     "CARLAWHYWONTYOUCALLME?",
                     "ONWARDSAOSHIMA",
                     "MRCAESARIANWILLBEOUTNEXTWEEKMRATBASHWILLSUBSTITUTE",
                     "PAPERJAMDIPPERSAYSAUUGHWXQHGADSADUH",
                     "EPLURIBUSTREMBLEY",
                     "NOTHGWELLSAPPROVED",
                     "SORRYDIPPERBUTYOURWENDYISINANOTHERCASTLE",
                     "THEINVISIBLEWIZARDISWATCHING",
                     "BROUGHTTOYOUBYHOMEWORKTHECANDY",
                     "HEAVYISTHEHEADTHATWEARSTHEFEZ",
                     "NEXTUPFOOTBOTTWOGRUNKLESGREVENGE",
                     "VIVANLOSPATOSDELAPISCINA",
                     "BUTWHOSTOLETHECAPERS",
                     "HAPPYNOWARIEL",
                     "ITWORKSFORPIIIIIIIIIIIIIIIIIGS",
                     "LIARMONSTERSNAPPYDRESSER",
                     "SEARCHFORTHEBLINDEYE"
                     ]

def numberCode(ciphertext):
    ciphertext += " "
    decifrado = ""
    lista = [] #lista[0] indice del cap, el resto son los indices de las letras
    actual = ""
    for caracter in ciphertext:
        if not ord('0') <= ord(caracter) <= ord('9'):
            if caracter == ")":
                lista.append([actual])
                actual=""
            elif caracter == ",":
                lista[-1].append(actual)
                actual=""
            elif caracter == "]":
                lista[-1].append(actual)
                lista[-1].append(" ")
                actual=""
            elif caracter == " " and actual != "":
                lista[-1].append(actual)
                actual=""
        else:
            actual+=caracter

    for subLista in lista:
        for item in subLista[1:]:
            if item == " ":
                decifrado += " "
            else:
                decifrado += listaDeSoluciones[int(subLista[0])-1][int(item)-1]
    return decifrado

def vigenere(ciphertext):
    decifrado = ""
    return decifrado

#print("deciframiento: ", caesar(input("Texto a decifrar con Caesar: ")))
#print("deciframiento: ", atbash(input("Texto a decifrar con atbash: ")))
#print("deciframiento: ", A1Z26(input("Texto a decifrar con A1Z26: ")))
#print("combined: ", combined(input("Texto a decifrar con combined cipher: ")))
print("number code:",numberCode(input("Texto a decifrar con number code: ")))