
import random

class Person:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

class GuessWhoGame:
    def __init__(self, people):
        self.people = people
        self.secret_person = random.choice(people)

    def display_attributes(self):
        attributes = []
        for person in self.people:
            attributes.append(person.attributes)
        return attributes

    def guess_person(self, attributes):
        for attribute in attributes:
            if attribute not in self.secret_person.attributes:
                return "No"
        return "Yes"

def main():
    # Definir las personas y sus atributos
    people = [
        Person("John", ["Rojo", "Deportivo", "SUV","Mercedes"]),
        Person("Alice", ["Azul", "Sedan", "Electrico", "Ferrari"]),
        Person("Bob", ["Negro", "Camioneta", "Diesel", "peugeot"]),
        Person("Emma", ["Blanco", "Convertible", "Gasolina", "Nissan"]),
        Person("Alexis", ["Plata", "Sedan", "Gas", "Mercedes"]),
        Person("Eduardo", ["Gris", "Deportivo", "Gasolina", "Omoda"]),
        Person("Alejandro", ["Verde", "Camioneta", "Gasolina", "Chrysler"]),
        Person("Mariana", ["Cafe", "Sedan", "Gasolina", "Hyundai"]),
        # Añade más personas con sus atributos aquí
    ]

    # Iniciar el juego
    game = GuessWhoGame(people)

    print("Bienvenido al juego de Adivina Quien - Tema: Coches")

    while True:
        print("\nAtributos disponibles:")
        for i, attributes in enumerate(game.display_attributes()):
            print(f"{i + 1}. {attributes}")

        guesses = []
        for _ in range(3):
            guess = input("\nElige un atributo para adivinar (ejemplo: Rojo): ").capitalize().strip()
            guesses.append(guess)

        if "Salir" in guesses:
            print("Hasta luego")
            break

        result = game.guess_person(guesses)

        if result == "Yes":
            print(f"Si, el personaje secreto tiene los atributos '{', '.join(guesses)}'. Has ganado")
            break
        else:
            print(f"No, el personaje secreto no tiene todos los atributos '{', '.join(guesses)}'.")

if __name__ == "__main__":
    main()
