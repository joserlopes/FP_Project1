# Projeto realizado por:
# José António Lopes, Nº103938, Mail:jose.r.lopes@tecnico.ulisboa.pt

# ------------------------------------------------------ PRIMEIRA PARTE --------------------------------------------------------------------------------
def corrigir_palavra(char):
    ''' 
    Esta função recebe uma cadeia de carateres que representa uma palavra (potencialmente
    modificada por um surto de letras) e devolve a cadeia de carateres que corresponde a
    aplicacao da sequencia de reducoes conforme descrito para obter a palavra corrigida.


            Parametros:
                char(str): cadeia de carateres

            Retorna:
                char(str): cadeia de carateres devidamente corrigida
    '''
 
    prev_char = ""
    i = 0
    len_char = len(char)
    while i < len_char:
        if prev_char != char[i]:
            if prev_char.upper() == char[i] or prev_char == char[i].upper():
                char = char[:i - 1] + char[i + 1:]  # Intervalo no qual não estão compreendidas as duas letras que têm que ser retiradas
                len_char = len(char)  # Atualizar o tamanho da string porque acabou de perder duas letras
                i -= 2  # Aqui retira-se 2 ao i para "compensar" a perda de duas letras, assim o i não fica fora do índice
                if len_char == 0:  # Parar se a string ficar vazia
                    return char
        prev_char = char[i]
        i += 1
    return char


def eh_anagrama(word1, word2):
    '''
    Esta função recebe duas cadeias de carateres correspondentes a duas palavras e devolve
    True se e só se uma é anagrama da outra, isto é, se as palavras são constituídas pelas
    mesmas letras, ignorando diferenças entre maiúsculas e minúsculas e a ordem entre
    carateres.


            Parametros:
                word1(str): cadeia de caratres correspondentes a uma palavra
                word2(str): cadeia de caratres correspondentes a outra palavra

            Retorna:
                False(bool) caso os dois parametros não sejam anagramas um do outro e True (bool) se o forem
    '''

    if type(word1) != str or type(word2) != str:
        return False
    word1 = word1.upper()
    word2 = word2.upper()
    if len(word1) != len(word2):
        return False
    elif sorted(word1) == sorted(word2):
        return True
    if sorted(word1) != sorted(word2):
        return False

def corrigir_doc(char):
    '''
    Esta função recebe uma cadeia de carateres que representa o texto com erros da documentação
    da BDB e devolve a cadeia de carateres filtrada com as palavras corrigidas e os anagramas
    retirados, ficando apenas a sua primeira ocorrência. Os anagramas são avalidados após a
    correção das palavras e apenas são retirados anagramas que não correspondam à mesma palavra
    (ignorando maíusculas e minúsculas), utilizando ambas as funções anteriormente definidas.
    Esta função verifica a validade do argumento gerando um Value Error com a mensagem '
    corrigir_doc: armugento invalido' caso o seu argumento não seja válido.
    Para este fim, considere que as palavras apenas podem estar separadas por um único espaço,
    que o texto está formado poruma ou mais palavras, e que cada palavra
    é formada apenas por, pelo menos, uma letra (minúscula ou maiúscula).


            Parametros:
                char(str): cadeia de carateres

            Retorna
                list_res(str): cadeia de carateres devidamente corrigida e com os anagramas retirados
    '''
    if type(char) != str:
        raise ValueError("corrigir_doc: argumento invalido")
    if char[-1] == " ":
        raise ValueError("corrigir_doc: argumento invalido")
    if char[0] == " ":
        raise ValueError("corrigir_doc: argumento invalido")
    for c in range(len(char)):
        if not (char[c].isalpha() or ord(char[c]) == 32) or (char[c] == " " and char[c + 1] == " ") or char[c] == "":
            raise ValueError("corrigir_doc: argumento invalido")


    char_with_anag = corrigir_palavra(char)
    char_with_anag_list = char_with_anag.split()
    for word1 in char_with_anag_list:
        for word2 in char_with_anag_list:
            if char_with_anag_list.index(word1) != char_with_anag_list.index(word2) and eh_anagrama(word1, word2) and word2.upper() != word1.upper():
                char_with_anag_list.remove(word2)
    list_res = " ".join(char_with_anag_list)
    return list_res



# ------------------------------------------------------ SEGUNDA PARTE --------------------------------------------------------------------------------


def obter_posicao(char, num):
    '''
    Esta função recebe uma cadeia de carateres contendo apenas um caráter que representa
    a direção de um único movimento ('C', 'B', 'E' ou 'D') e um inteiro representando a
    posição atual (1, 2, 3, 4, 5, 6, 7, 8 ou 9); e devolve o inteiro que corresponde à nova
    posição após do movimento.


            Parametros:
                char(str): cadeia de carateres que representa a direção de um único movimento
                num(int): número inteiro representando a posição inicial

            Retorna:
                num(int): número inteiro correspondente à nova posição após o movimento
    '''

    if char == "C" and num >= 4:
        num = num - 3
    if char == "B" and num <= 6:
        num = num + 3
    if char == "E" and num != 1 and num != 4 and num != 7:
        num = num - 1
    if char == "D" and num != 3 and num != 6 and num != 9:
        num = num + 1
    return num


def obter_digito(char, num): 
    '''
    Esta função recebe uma cadeia de carateres contendo uma sequência de um ou mais movimentos
    e um inteiro representando a posição inicial; e devolve o inteiro que corresponde
    ao dígito a marcar após finalizar todos os movimentos, utilizando a função obter_posicao
    anteriormente definida


            Parametros:
                char(str): cadeia de carateres que representa a sequência de movimentos
                num(int): número inteiro representando a posição inicial

            Retorna:
                num(int): número inteiro correspondente à nova posição após finalizar todos os movimentos
    '''

    for letter in char:
        num = obter_posicao(letter, num)
    return num


def obter_pin(sequence):
    '''
    Esta função recebe um tuplo contendo entre 4 e 10 sequências de movimentos e devolve
    o tuplo de inteiros que contÊm o pin codificado de acordo com o tuplo de movimentos,
    sendo que a posição inicial é o número 5.
    Esta função deve verificar a validade do seu argumento conforme descrito nesta secção
    (isto é, tuplo de entre 4 e 10 sequ^encias de movimentos, em que cada movimento é uma
    string com 1 ou mais carateres 'C', 'B', 'E' ou 'D'), gerando um ValueError com a
    mensagem 'obter_pin: argumento invalido' caso o seu argumento não seja válido.


        Parametros:
            sequence(tuple): tuplo contendo entre 4 a 10 sequências de movimentos

        Retorna:
            pin(tuple): tuplo contendo os inteiros correspondentes ao pin codificado
            de acordo com o parametro sequence.
    '''

    if type(sequence) != tuple:
        raise ValueError("obter_pin: argumento invalido")
    if len(sequence) == 0:
        raise ValueError("obter_pin: argumento invalido")
    if len(sequence) > 10 or len(sequence) < 4:
        raise ValueError("obter_pin: argumento invalido")
    for seq in sequence:
        if len(seq) == 0:
            raise ValueError("obter_pin: argumento invalido")
        for letter in seq:
            if ord(letter) < 66 or ord(letter) > 69:
                raise ValueError("obter_pin: argumento invalido")
    num = 5
    pin = ()
    for series_digit in sequence:
        for letter in series_digit:
            num = obter_posicao(letter, num)
        pin += (num,)
    return pin



# ------------------------------------------------------ TERCEIRA PARTE -------------------------------------------------------------------------------


def eh_cifra(cifra):
    '''
    Esta função recebe uma cadeia de carateres e devolve True se essa cadeia é uma cifra
    (uma ou mais palavras encriptadas separadas por traços)


            Parametros:
                cifra(str): cadeia de caratéres

            Retorna:
                True(bool) se o parametro corresponde a uma cifra (uma ou mais palavras encriptadas separadas por
                traços), Falso(bool) se não corresponde
    '''

    if type(cifra) != str or len(cifra) == 0 or cifra == "" or not cifra[0].isalpha():
        return False
    for a in range(len(cifra.split("-"))):
        for letter in cifra.split("-")[a]:
            if letter == "" or not letter.isalpha() or not (96 < ord(letter) < 123):
                return False
    return True


def eh_checksum(checksum):
    '''
    Esta função recebe uma cadeia de carateres e devolve True se essa cadeia é um checksum
    (5 letras minúsculas entre parêntesis retos)


            Parametros:
                checksum(str): cadeia de carateres

            Retorna:
                True(bool) se o parametro corresponde a um checksum (5 letras minúsculas entre parêntesis retos),
                Falso(bool) se não corresponde
    '''

    if type(checksum) != str or checksum[0] != "[" or checksum[-1] != "]" or len(checksum) != 7:
        return False
    for a in range(1, len(checksum) - 1):
        if not (96 < ord(checksum[a]) < 123):
            return False
    return True


def eh_chave_seguranca(chave):
    '''
    Esta função recebe um tuplo e devolve True se esse tuplo é uma sequência de segurança
    (um tuplo com dois ou mais números inteiros positivos de segurança)


            Parametros:
                chave(tuple): tuplo

            Retorna:
                True(bool) se o parametro corresponde a uma sequência de segurança
                (um tuplo com dois ou mais números inteiros positivos de segurança),
                Falso(bool) se não corresponde
    '''

    if type(chave) != tuple or len(chave) < 2:
        return False
    for num in chave:
        if type(num) != int or num < 0:
            return False
    return True


def eh_entrada(BDB_entry):
    '''
    Esta função recebe um argumento de qualquer tipo e devolve True se e só se o seu argumento corresponde
    a uma entrada BDB, um tuplo com 3 campos (uma cifra, um checksum e uma seuqência de segurança),
    utilizando as 3 funções anteriormente definidas


            Parametros:
                BDB_entry(universal): argumento de qualquer tipo

            Retorna:
                True(bool) se o argumento corresponde a uma entrada BDB
                (um tuplo com 3 campos: uma cifra, uma sequência de controlo e uma sequência de segurança)
                e False(bool) se não corresponde
    '''

    if type(BDB_entry) != tuple or len(BDB_entry) != 3:
        return False
    if eh_cifra(BDB_entry[0]) and eh_checksum(BDB_entry[1]) and eh_chave_seguranca(BDB_entry[2]):
        return True
    return False


def validar_cifra(cifra, seq_controlo):
    '''
    Esta função recebe uma cadeia de carateres contendo uma cifra e uma outra cadeia de
    carateres contendo um checksum, e devolve True se e só se o checksum
    é coerente com a cifra conforme descrito (se a sequência de controlo é formada pelas cinco letras
    mais comuns na sequência encriptada, por ordem inversa de ocorrências, com empates
    decididos por ordem alfabética)


            Parametros:
                cifra(str): cadeia de caratéres correspondente a uma cifra
                seq_controlo(str): cadeia de caratéres corresponde a um checksum, potencialmente errada

            Retorna:
                True(bool): True se e só se a checksum é coerente com a cifra, Falso(Bool) se isso não acontece
    '''

    str1 = ""
    count = {}
    list_cifra = cifra.split("-")
    str_res = ""
    for let in list_cifra:
        str1 += let
    for letter in sorted(str1):
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    list_rep = list(count.values())
    list_letters = list(count.keys())
    for i in range(len(list_letters)):
        maxim = max(list_rep)
        let_max = list_letters[list_rep.index(maxim)]
        str_res = str_res + let_max
        list_letters.remove(let_max)
        list_rep.remove(maxim)
        if len(str_res) == 5:
            break
    if str_res == seq_controlo[1:6]:
        return True
    else:
        return False


def filtrar_bdb(list_bdb_entry):
    '''
    Esta função recebe uma lista contendo uma ou mais entradas da BDB e devolve apenas
    a lista contendo as entradas em que o checksum não é coerente com a cifra correspondente,
    na mesma ordem da lista original. Esta função deve verificar a validade do
    seu argumento, gerando um ValueError com a mensagem 'filtrar_bdb: argumento
    invalido' caso o seu argumento não seja válido


            Parametros:
                list_bdb_entry(lista): lista contendo uma ou mais entradas da BDB

            Retorna:
                list_res(lista):devolve apenasa lista contendo as entradas em que o
                checksum não é coerente com a cifra correspondente
    '''
    if type(list_bdb_entry) != list:
        raise ValueError('filtrar_bdb: argumento invalido')
    if len(list_bdb_entry) == 0:
        raise ValueError('filtrar_bdb: argumento invalido')
    for bdb_entry in list_bdb_entry:
        if not eh_entrada(bdb_entry):
            raise ValueError('filtrar_bdb: argumento invalido')

    list_res = []
    for user in list_bdb_entry:
        if not validar_cifra(user[0], user[1]):
            list_res += (user,)
    return list_res


# ------------------------------------------------------ QUARTA PARTE ---------------------------------------------------------------------------------

def obter_num_seguranca(hidden_security_num):
    '''
    Esta função recebe um tuplo de números inteiros positivos e devolve o número de segurança
    (a menor diferença positiva entre qualquer par de números)


            Parametros:
                hidden_security_num(tuple): tuplo de números inteiros positivos

            Retorna:
                min(int): a menor diferença positiva entre qualquer par de números do argumento
    '''

    min = float("inf")
    for i in range(len(hidden_security_num)):
        for j in range(i + 1, len(hidden_security_num)):
            if abs(hidden_security_num[i] - hidden_security_num[j]) < min:
                min = abs(hidden_security_num[i] - hidden_security_num[j])
    return min


def decifrar_texto(char, sec_number):
    '''
    Esta função recebe uma cadeia de carateres contendo uma cifra e um número de segurança,
    e devolve o texto decifrado (trocar cada letra avançando no alfabeto um número de vezes
    igual ao número de segurança de cada entrada mais um para as posições pares, e menos
    um para as posições ímpares do texto)


            Parametros:
                char(str): cadeia de carateres contendo uma cifra
                sec_number(int): número de segurança

            Retorna:
                "".join(cifra)(str): texto decifrado conforme descrito anteriormente
    '''

    cifra = list("".join(char.split(" ")))
    sec_number = sec_number % 26
    sec_number_2 = sec_number
    for i in range(len(cifra)):
        sec_number_2 = sec_number
        ord_letter = ord(cifra[i])
        if cifra[i] == "-":
            cifra[i] = " "
        else:
            if i % 2 == 0:
                sec_number_2 += 1
            else:
                sec_number_2 -= 1

            if ord_letter + sec_number_2 > 122:
                cifra[i] = chr(ord_letter - (26 - sec_number_2))
            else:
                cifra[i] = chr(ord_letter + sec_number_2)
    return "".join(cifra)


def decifrar_bdb(list_bdb_entry):
    '''
    Esta função recebe uma lista contendo uma ou mais entradas da BDB e devolve uma
    lista de igual tamanho, contendo o texto das entradas decifradas na mesma ordem.
    Esta função deve verificar a validade do seu argumento, gerando um ValueError com
    a mensagem 'decifrar_bdb: argumento invalido' caso o seu argumento não seja
    válido


            Parametros:
                list_bdb_entry(lista): uma lista contendo uma ou mais entradas da BDB

            Retornaa:
                list_res(lista): lista de igual tamanho ao argumento,
                contendo o texto das entradas decifradas na mesma ordem
    '''

    if len(list_bdb_entry) == 0:
        raise ValueError ('decifrar_bdb: argumento invalido')
    if type(list_bdb_entry) != list:
        raise ValueError('decifrar_bdb: argumento invalido')
    for bdb_entry in list_bdb_entry:
        if not eh_entrada(bdb_entry):
            raise ValueError('decifrar_bdb: argumento invalido')


    list_res = []
    for user in list_bdb_entry:
        list_res += [decifrar_texto(user[0], obter_num_seguranca(user[2]))]
    return list_res

# ------------------------------------------------------ QUINTA PARTE ---------------------------------------------------------------------------------

def eh_utilizador(info):
    '''
    Esta função recebe um argumento de qualquer tipo e devolve True se e só se o seu
    argumento corresponde a um dicionário contendo a informação de utilizador relevante
    da BDB conforme descrito, isto é, com o nome de utilizador (chave 'name'), a senha potencialmente
    corrompida (chave 'pass')) e a regra individual de quando essa senha foi definida (chave 'rule')).
    Nomes e senhas devem ter tamanho mínimo 1 e podem conter qualquer caráter


            Parametros:
                info(universal): argumento de qualquer tipo

            Retorna:
                True(bool) se e só se o seu argumento corresponde a um dicionário contendo a informação
                de utilizador relevante da BDB conforme descrito, isto é, nome, senha e regra individual,
                False(bool) se o contrário acontece
    '''

    if type(info) != dict or len((info)) != 3:
        return False
    if "name" not in info or "pass" not in info or "rule" not in info:
        return False
    if type(info["name"]) != str:
        return False
    if type(info["pass"]) != str:
        return False
    if type(info["rule"]) != dict:
        return False
    if len(info["name"]) == 0:
        return False
    if len(info["pass"]) == 0:
        return False
    if len(info["rule"]) != 2:
        return False
    if "vals" not in info["rule"] or "char" not in info["rule"]:
        return False
    if type(info["rule"]["vals"]) != tuple or (type(info["rule"]["char"]) != str and not info["rule"]["char"].isalpha()) or len(info["rule"]["char"]) != 1:
        return False
    if len(info["rule"]["vals"]) != 2 or type(info["rule"]["vals"][0]) != int or type(info["rule"]["vals"][1]) != int or type(info["rule"]["vals"]) != tuple:
        return False
    if info["rule"]["vals"][0] < 0 or (info["rule"]["vals"][0] > info["rule"]["vals"][1]):
        return False
    return True


def eh_senha_valida(password, indiv_rule):
    '''
    Esta função recebe uma cadeia de carateres correspondente a uma senha e um dicionário
    contendo a regra individual de criação da senha, e devolve True se e só se a senha cumpre
    com todas as regras de definição, gerais (as senhas devem conter pelo menos três vogais minúsculas ('aeiou')
    e devem conter pelo menos um caráter que apareça duas vezes consecutivas) e individual
    (as regras individuais são codificadas pelo valor da chave 'rule' de cada entrada como
    dicionários com as chaves 'vals' e 'char'. O valor de 'vals' é um tuplo de dois
    inteiros positivos correspondentes ao menor (primeira posição) e o maior (segunda
    posição) número de vezes que uma determinada letra minúscula (valor da chave 'char')
    deve aparecer)


            Parametros:
                password(str): cadeia de carateres correspondente a uma senha
                indiv_rule(dict): dicionário contendo a regra individual de criaçãao da senha

            Retorna:
                True(bool) se e só se a senha cumpre com todas as regras de definição
                (gerais e individual) conforme descrito, False(bool) se o contrário acontece
    '''

    #REGRAS GERAIS
    if not any(c1 == c2 for c1, c2 in zip(password, password[1:])):
        return False

    count_vow = 0
    for letter in password:
        if (ord(letter) == 97 or ord(letter) == 101 or ord(letter) == 105
                or ord(letter) == 111 or ord(letter) == 117):
            count_vow += 1
    if count_vow < 3:
        return False
    #REGRAS INDIVIDUAIS
    min_letter = indiv_rule["vals"][0]
    max_letter = indiv_rule["vals"][1]
    count_gen = password.count(indiv_rule["char"])
    if min_letter <= count_gen <= max_letter:
        return True
    return False


def filtrar_senhas(list_dict):
    '''
    Esta função recebe uma lista contendo um ou mais dicionários correspondentes às entradas
    da BDB como descritas anteriormente, e devolve a lista ordenada alfabeticamente
    com os nomes dos utilizadores com senhas erradas. Esta função deve verificar a validade
    do seu argumento, gerando um ValueError com a mensagem 'filtrar senhas:
    argumento invalido' caso o seu argumento n~ao seja válido.


            Parametros:
                list_dict(lista): lista contendo um ou mais dicionários correspondentes
                 às entradasda BDB como descritas anteriormente

            Retorna:
                sorted(list_name)(lista): lista ordenada alfabeticamente
                com os nomes dos utilizadores com senhas erradas
    '''
    if type(list_dict) != list:
        raise ValueError("filtrar_senhas: argumento invalido")
    if len(list_dict) == 0:
        raise ValueError("filtrar_senhas: argumento invalido")
    if type(list_dict) != list:
        raise ValueError ("filtrar_senhas: argumento invalido")
    for items in list_dict:
        if not eh_utilizador(items):
            raise ValueError ("filtrar_senhas: argumento invalido")

    list_name = []
    for user in list_dict:
        if not eh_senha_valida(user["pass"], user["rule"]):
            list_name += [user["name"]]
    return sorted(list_name)
