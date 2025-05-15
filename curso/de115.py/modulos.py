def verificaint(msg):
    while True:
        try:
            n = int(input(msg))
            if n > 3:
                print('ERRO: por favor, digite um número inteiro válido')
                continue
        except:
            print('ERRO: por favor, digite um número inteiro válido')
        else:
            return n


def menu():
    opcao = ''
    print('-' * 40)
    print('                  MENU')
    print('-' * 40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')


def arquivoexiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return False
    else:
        print('Arquivo encontrado')
        return True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Problema ao criar arquivo')
    else:
        print('Arquivo criado com sucesso')
    

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao tentar cadastrar pessoa')
    else:
        a.write(f'{nome}; {idade}\n')
        a.close()