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

def vigenere(ciphertext,key):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tabla=[["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
           ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A"],
           ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B"],
           ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"],
           ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D"],
           ["F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E"],
           ["G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F"],
           ["H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G"],
           ["I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H"],
           ["J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"],
           ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
           ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
           ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
           ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
           ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"],
           ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
           ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"],
           ["R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"],
           ["S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"],
           ["T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"],
           ["U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"],
           ["V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"],
           ["W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"],
           ["X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"],
           ["Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"],
           ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]]
    n = len(key)
    decifrado = ""
    positionKey = 0
    if len(key) < len(ciphertext):
        for i in range(len(ciphertext)):
            key += key[int(i % n)]
    for i in range(len(ciphertext)):
        if (ciphertext[i]) not in alpha:
            decifrado += ciphertext[i]
        else:
            decifrado += alpha[tabla[alpha.index(key[positionKey])].index(ciphertext[i])]
            positionKey += 1
    return decifrado

def binary(ciphertext):
    ciphertext=(ciphertext.strip().replace(" ","")).replace("\n","")
    decifrado=""
    for i in range (len(ciphertext)//8):
        porcion=ciphertext[i*8:(i+1)*8]
        decifrado+=chr(int(str(porcion),2))
    return decifrado;

menu = """1) Decifrar mensaje con Caesar
2) Decifrar mensaje con atbash
3) Decifrar mensaje con A1Z26
4) Decifrar mensaje con Combined cipher
5) Decifrar mensaje con Number Codes
6) Decifrar mensaje con Vigenere
7) Decifrar mensaje binario
8) Salir"""
opcion = ""
while opcion != "7":
    print(menu)
    opcion = input("\nEscoja una opcion: ")
    print("\n")
    if opcion == "1":
        print("deciframiento: ", caesar(input("Texto a decifrar con Caesar: ")))
    elif opcion == "2":
        print("deciframiento: ", atbash(input("Texto a decifrar con atbash: ")))
    elif opcion == "3":
        print("deciframiento: ", A1Z26(input("Texto a decifrar con A1Z26: ")))
    elif opcion == "4":
        print("deciframiento: ", combined(input("Texto a decifrar con Combined cipher: ")))
    elif opcion == "5":
        print("deciframiento:",numberCode(input("Texto a decifrar con Number code: ")))
    elif opcion == "6":
        print("deciframiento: ", vigenere(input("Texto a decifrar con Vigenere: "),input("Llave del cifrado: ")))
    elif opcion == "7":
        print("deciframiento:",binary(input("Numero binario a decifrar: ")))
    elif opcion == "8":
        print("Adios")
    else:
        print("Opcion incorrecta")
    print("\n")