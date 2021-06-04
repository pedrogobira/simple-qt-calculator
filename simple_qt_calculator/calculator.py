import re


# Verifica se um token é um operador válido
def is_operator(token):
    if (token == '+' or token == '-' or token == '*' or token == '/'):
        return True
    else:
        return False


# Arredonda o resultado com base na resposta do usuário
def formatting_for_print(number):
    if re.match(r'^[-]?\d+\.\d{3,}$', str(number)):
        number = round(number, 2)

    number = re.sub(r'\.', ',', str(number))
    return number


# Atribuindo sinais corretos aos números.
def assigning_signals(tokens):
    # Verificando se o primeiro número é negativo.
    if tokens[0] == '+':
        tokens.pop(0)
    elif tokens[0] == '-':
        tokens[1] = tokens[1] * -1
        tokens.pop(0)

    # Atribuindo sinal a um número da lista se existir dois sinais vizinhos.
    for index, item in enumerate(tokens):
        if is_operator(item):
            try:
                if tokens[index + 1] == '-':
                    tokens[index + 2] = tokens[index + 2] * -1
                    tokens.pop(index + 1)
                elif tokens[index + 1] == '+':
                    tokens.pop(index + 1)
            except IndexError:
                pass  # Ignora exceção IndexError. Exceção esperada.


#  Recebe uma lista de tokens e o tipo de operação (qual prioridade?) que
#  precisa ser resolvida.
def calculate_operations(tokens, priority):
    # O index precisa sempre ser 0 para uma nova verificação
    index = -1
    try:
        while (index < len(tokens) - 1):
            index += 1
            if (not is_operator(tokens[index]) and is_operator(tokens[index+1])
                    and not is_operator(tokens[index+2])):

                if priority == 'high':
                    if (tokens[index+1] == "*"):
                        result = tokens[index] * tokens[index+2]
                    elif (tokens[index+1] == '/'):
                        result = tokens[index] / tokens[index+2]
                    else:
                        continue
                elif priority == 'low':
                    if (tokens[index+1] == "+"):
                        result = tokens[index] + tokens[index+2]
                    elif (tokens[index+1] == '-'):
                        result = tokens[index] - tokens[index+2]
                    else:
                        continue

                tokens[index] = result
                tokens.pop(index+2)
                tokens.pop(index+1)
                index = -1
    except IndexError:
        pass  # Ignora exceção IndexError. Exceção esperada.


def calculator(expression):
    # Removendo espaços em branco
    expression = re.sub(r'\s', '', expression)

    # Substituindo vírgulas por pontos
    expression = re.sub(r',', '.', expression)

    # Substituindo sinais de prioridade por parênteses
    expression = re.sub(r'[\[\{]', '(', expression)
    expression = re.sub(r'[\]\}]', ')', expression)

    # Multiplicação quando não existe operador entre número e parêntese
    expression = re.sub(r'(?<=\d)\(', '*(', expression)
    expression = re.sub(r'\)(?=\d)', ')*', expression)

    # Verificando se existe algum par de parênteses, passando para "match".
    match = re.search(r'(\([^()]*\))', expression)

    # Se existir algum par de parênteses, "match" terá um objeto Match.
    # A subexpressão capturada será solucionada recursivamente com "calculator"
    while match:
        match_without_parenthesis = re.sub(r'[\(\)]', '', match.group(0))
        match_result = calculator(match_without_parenthesis)
        expression = expression.replace(match.group(), str(match_result))
        match = re.search(r'(\([^()]*\))', expression)

    # Lista de tokens (componentes léxicos)
    tokens = []
    # Intermediário para unificar números
    current_value = ''

    # Criando tokens para cálculos. Números (float) ou operadores (string).
    for item in expression:
        if is_operator(item):
            if not current_value == '':
                tokens.append(float(current_value))
            tokens.append(item)
            current_value = ''
        else:
            current_value += item
    tokens.append(float(current_value))

    # Atribuindo sinais para números positivos e negativos
    assigning_signals(tokens)

    # Priorizando operações
    calculate_operations(tokens, 'high')
    calculate_operations(tokens, 'low')

    # "tokens" é reduzido a um lista com um único valor, o resultado.
    return tokens[0]


# Função de entrada
def run_calculator(user_input):
    try:
        result = calculator(user_input)
        if isinstance(result, float):
            return formatting_for_print(result)
        else:
            return 'Expressão matemática inválida'
    except Exception:
        return 'Expressão matemática inválida'
