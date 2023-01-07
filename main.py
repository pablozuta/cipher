message = "la madrugada fue apagando mis recuerdos"
shift = 7
ULTIMO_CARACTER = 90
RANGO_CARACTERES = 26
# creamos un contenedor con un empty string
frase_cipher = ""

# iterar por cada letra del mensaje
for letra in message.upper():
    if letra.isalpha():
        # convertir el mensaje a codigo ASCII
        letra_code = ord(letra)

        cipher_code = letra_code + shift

        if cipher_code > ULTIMO_CARACTER:
            cipher_code -= RANGO_CARACTERES

        cipher_letra = chr(cipher_code)

        frase_cipher = frase_cipher + cipher_letra
    else:
        frase_cipher = frase_cipher + letra    
        
print(frase_cipher)