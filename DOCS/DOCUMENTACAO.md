# Documentação do Projeto - Info de Pets

## Descrição

O projeto é um script Python que coleta informações básicas sobre um pet (nome, idade e peso) e exibe essas informações ao usuário. As funções incluídas garantem que as entradas sejam válidas e estejam dentro de limites razoáveis.

## Estrutura do Código

### Função `coletar_nome()`

**Descrição:**  
Solicita ao usuário que insira o nome do pet.

**Retorno:**  
- `str`: O nome do pet inserido pelo usuário.

**Uso:**  

    nome = coletar_nome()


### Função `coletar_idade()`

**Descrição:** 
Coleta a idade do pet a partir da entrada do usuário. A função garante que a idade seja um número inteiro não negativo e não superior a 50 anos.

**Retorno:**  
- `int`: A idade do pet em anos.

**Uso:**  

    idade = coletar_idade()

### Função `coletar_peso()`

**Descrição:** 
Coleta o peso do pet a partir da entrada do usuário. A função garante que o peso seja um número de ponto flutuante não negativo e não superior a 500 kg.

**Retorno:**  
- `float`: O peso do pet em quilogramas.

**Uso:**  

    peso = coletar_peso()

### Notas:

- Se o usuário inserir um valor não numérico ou um valor fora do intervalo permitido, a função solicitará a entrada novamente até que um valor válido seja fornecido.

### Função `coletar_informacoes_pet()`

**Descrição:** 
Função principal que solicita ao usuário o nome, a idade e o peso do pet usando as funções `coletar_nome()`, `coletar_idade()` e `coletar_peso()`. Em seguida, exibe as informações coletadas.

**Uso:**  

    coletar_informacoes_pet()

### Funcionamento
A função coletar_informacoes_pet() é chamada.
O usuário é solicitado a inserir o nome, a idade e o peso do pet.
Cada entrada é validada pelas respectivas funções (`coletar_nome()`, `coletar_idade()` e `coletar_peso()`).
As informações coletadas são exibidas ao usuário.
### Exemplo de Execução
Ao executar o código, o usuário verá o seguinte:

    ```bash
    Por favor, insira as informações sobre seu pet.
    Nome do pet: Rex
    Idade do pet (em anos): 5
    Peso do pet (em kg): 10

    Informações do pet:
    Nome: Rex
    Idade: 5 anos
    Peso: 10.00 kg
    ```

