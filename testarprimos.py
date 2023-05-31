def testaprimo(num):
    """
    Verifica se um número é primo.

    Args:
        num (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    # 1 não é primo!
    if num == 1:
        return False
    # Devemos procurar um divisor de 2 até a metade do número. Se existir pelo menos um, não é primo!
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    # Se o loop terminar e não encontrar divisores, o número é primo!
    else:
        return True


if __name__ == "__main__":
    """
    Solicita um número inteiro ao usuário e verifica se é primo.
    Imprime uma mensagem informando se o número é primo ou não.
    """
    numero = int(input())
    if testaprimo(numero):
        print(f'{numero} eh primo')
    else:
        print(f'{numero} nao eh primo')
