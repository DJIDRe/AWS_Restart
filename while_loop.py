import random

print("¡Bienvenido a Adivina el Número!")
print("Las reglas son simples. Pensaré en un número y tú intentarás adivinarlo.")

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Adivina un número entre 1 y 10:  ")
    if int(guess) == number:
        print("Acertó {}. ¡Eso es correcto! ¡Tú ganas!".format(guess))
        isGuessRight = True
    else: 
        print("Acertó {}. Lo siento, no es eso. Intentar otra vez.".format(guess))
