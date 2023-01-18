from FIGURAS import Rectangulo, Circulo, probar_figura

def main():
    op = 0
    while op != 3:
        print('*' * 20)
        print('|  MENU DE OPCIONES  |')
        print('1 - Rectangulo \n'
              '2 - Circulo \n'
              '3 - Salir')
        print('*' * 20)

        op = int(input('Ingrese una opcion: '))
        if op != 0 and op <= 3:

            if op == 1:
                base = float(input('Ingrese la base del rectangulo: '))
                altura = float(input('Ingrese la altura del rectangulo: '))
                rectangulo = Rectangulo(base, altura)
                probar_figura(rectangulo)
            elif op == 2:
                radio = float(input('Ingrese el radio: '))
                cir = Circulo(radio)
                probar_figura(cir)
        if op == 3:
            print('Cerrando el programa....')
        else:
            print('La opcion elegida no es valida!')

if __name__ == '__main__':
    main()
