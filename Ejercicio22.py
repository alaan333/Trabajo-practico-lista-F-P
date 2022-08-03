# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

from lista import Lista
class Jedi:

    def __init__(self, nombre, especie, maestro, sable_luz):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable_luz = sable_luz

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.maestro} | {self.sable_luz}"


lista_jedi = Lista()
lista_jedi2 = Lista()

file = open('C:/Users/Fernando Paz/Primer proyecto JS/Algoritmo2022/Algoritmo y estructura de datos/PythonAlan/Archivoslocales/Trabajo-practico-lista-py/jedis.txt')
lineas = file.readlines()
lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')
    lista_jedi.insertar(Jedi(datos[0],
                             datos[2],
                             datos[3].split('/'),
                             datos[4].split('/')),'nombre')
    lista_jedi2.insertar(Jedi(datos[0],
                              datos[2],
                              datos[3],
                              datos[4].split('/')),'especie')
   

# a. listado ordenado por nombre y por especie;
print('Listado por nombre: ')
lista_jedi.barrido()        
print()
print('Lista por especie: ')
lista_jedi2.barrido()
print()

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
dato = lista_jedi.busqueda('ahsoka tano', 'nombre')
if dato:
    print(f'Nombre: {dato.info.nombre}')
    print(f'Especie: {dato.info.especie}')
    print(f'Maestro: {dato.info.maestro}')
    print(f'Sable de luz: {dato.info.sable_luz}')
else:
    print('el Jedi no esta en la lista')
print()
dato = lista_jedi.busqueda('kit fisto', 'nombre')
if dato:
    print(f'Nombre: {dato.info.nombre}')
    print(f'Especie: {dato.info.especie}')
    print(f'Maestro: {dato.info.maestro}')
    print(f'Sable de luz: {dato.info.sable_luz}')
else:
    print('el Jedi no esta en la lista')
print()

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print('Alumnos de Yoda:')
lista_jedi.padawans_de('yoda')
print()
print('Alumnos de Luke Skywalker: ')
lista_jedi.padawans_de('luke skywalker')
print()

# d. mostrar los Jedi de especie humana y twi'lek;
print('Jedis raza humano: ')
lista_jedi.barrido_humanos()
print()
print("Jedis raza twi'lek: ")
lista_jedi.barrido_twi_lek()
print()

# e. listar todos los Jedi que comienzan con A;
print('Jedi que comienzan con A: ')
lista_jedi.barrido_comienza_con('a')
print()

# f. mostrar los Jedi que usaron sable de luz de más de un color;
print('Jedi que usaron mas de un color de sable de luz: ')
lista_jedi.barrido_sable_mas_de_uno()
print()

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print('Jedi que usaron sable de luz amarillo o violeta: ')
lista_jedi.barrido_amarillo_violeta()
print()

# h. indicar los nombres de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print('Padawans de Qui-Gon Jin: ')
lista_jedi.padawans_de('qui-gon jin')
print()
print('Padawans de Mace Windu: ')
lista_jedi.padawans_de('mace windu')
print()