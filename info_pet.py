# Função para coletar nome
def coletar_nome():
    return input("Nome do pet: ")

# Função para coletar idade
def coletar_idade():
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            elif idade > 50:
                print("A idade parece muito alta. Verifique e tente novamente.")
            else:
                return idade
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

# Função para coletar peso
def coletar_peso():
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            elif peso > 500:  # Limite superior razoável para o peso
                print("O peso parece muito alto. Verifique e tente novamente.")
            else:
                return peso
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

# Função para coletar informações sobre o pet
def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet.")
    nome = coletar_nome()
    idade = coletar_idade()            
    peso = coletar_peso()

    # Exibindo as informações coletadas
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso:.2f} kg")  

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
