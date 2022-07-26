def main():
    paises = input('Ingrese una lista de paises separados por comas: ').split(',')

    if ' ' in ''.join(paises):
        for i in range(len(paises)):
            if ' ' in paises[i]:
                paises[i] = paises[i].replace(' ', '')

    paises = set(paises)
    paises = list(paises)
    paises.sort()

    print(', '.join(paises))


if __name__ == '__main__':
    main()
