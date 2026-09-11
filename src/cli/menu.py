# translation dictionaty
translations = {
    "title": "=== PORTAL DA CIDADE ===",
    "option1": "1 - Cadastrar Publicação.",
    "option2": "2 - Listar Publicações.",
    "option3": "3 - Buscar por Palavra.",
    "option4": "4 - Filtrar por Categoria.",
    "option5": "5 - Sair.",
    "choices": "Escolha uma opção: ",
    "Invalid": "Escolha Invalida! Tente uma opção entre 1 e 5.",
    "error": "Tente uma das opções!",
}


# function that will display the options to the user.
def display_menu():
    while True:
        print(translations["title"])
        print(translations["option1"])
        print(translations["option2"])
        print(translations["option3"])
        print(translations["option4"])
        print(translations["option5"])

        try:
            user_choice = int(input(translations["choices"]))
            if user_choice < 1 or user_choice > 5:
                print(translations["Invalid"])
        except ValueError:
            print("error")
            continue
        return user_choice


# function to process the choice
def process_choice(user_choice: int):
    if user_choice == 1:
        print("Registration not yet implemented")
    elif user_choice == 2:
        print("Registration not yet implemented 2 ")
    elif user_choice == 3:
        print("Registration not yet implemented 3 ")
    elif user_choice == 4:
        print("Registration not yet implemented 4 ")
    else:
        print("Exit")


choose = display_menu()
process_choice(choose)
