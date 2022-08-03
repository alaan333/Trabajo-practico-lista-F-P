# 21. Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
# nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudación.
# Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado
# año–;
# b. mostrar los datos de la película que más recaudo;
# c. indicar las películas con mayor valoración del público, puede ser más de una;
# d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una
# lista auxiliar–:
# I. por nombre,
# II. por recaudación,
# III. por año de estreno,
# IV. por valoración del público.

from lista import Lista

class Peliculas:

    def __init__(self, nombre, valoracion_publico, anio_estreno, recaudacion):
        self.nombre = nombre
        self.valoracion_publico = valoracion_publico
        self.anio_estreno = anio_estreno
        self.recaudacion = recaudacion

    def __str__(self):
        return f"{self.nombre} | {self.valoracion_publico} | {self.anio_estreno} | {self.recaudacion}"

peliculas = [
    {'name': 'AA', 'val_publ': 4, 'a_est': 1996,  'recaudacion': 22088888},
    {'name': 'BB', 'val_publ': 7, 'a_est': 2004,  'recaudacion': 30500000},
    {'name': 'CC', 'val_publ': 5, 'a_est': 1965,  'recaudacion': 32088888},
    {'name': 'DD', 'val_publ': 5, 'a_est': 1978,  'recaudacion': 21000000},
    {'name': 'EE', 'val_publ': 9, 'a_est': 2021,  'recaudacion': 25000000},
    {'name': 'FF', 'val_publ': 8, 'a_est': 2012,  'recaudacion': 25670000},
    {'name': 'GG', 'val_publ': 10, 'a_est': 2004,  'recaudacion': 13789000},
]

lista_peliculas=Lista()
lista_aux=Lista()

for pelicula in peliculas:
    lista_peliculas.insertar(Peliculas(pelicula['name'],
                                           pelicula['val_publ'],
                                           pelicula['a_est'],
                                           pelicula['recaudacion']), 'nombre')

# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado año–;
anio=int(input('Ingrese el año:'))
print(f'Peliculas del año {anio}:')
lista_peliculas.barrido_x_anio(anio)
print()

# b. mostrar los datos de la película que más recaudo;
lista_peliculas.pelicula_que_mas_recaudo()
print()

# c. indicar las películas con mayor valoración del público, puede ser más de una;
print('Peliculas mejor valoradas por el publico: ')
lista_peliculas.barrido_valoracio_publico()
print()

# d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una
# lista auxiliar–:
# I. por nombre,
# II. por recaudación,
# III. por año de estreno,
# IV. por valoración del público.
                                                        #probamos obteniendo elemento e insertandolo en la lista auxiliar
print('Lista ordenada por nombre:')
lista_peliculas.barrido()
print()

print('Lista ordenada por recaudacion:')
for i in range(lista_peliculas.tamanio()):
    dato=lista_peliculas.obtener_elemento(i)
    lista_aux.insertar(dato,'recaudacion') 
lista_aux.barrido()
print()

print('Por año de estreno: ')
#para vaciar la lista_peliculas
for i in range(lista_peliculas.tamanio()):
    dato=lista_peliculas.obtener_elemento(0)
    lista_peliculas.eliminar(dato)
#insertamos
for i in range(lista_aux.tamanio()):
    dato=lista_aux.obtener_elemento(i)
    lista_peliculas.insertar(dato,'anio_estreno')
lista_peliculas.barrido()
print()

print('Por valoracion del publico: ')
#para vaciar la lista_aux
for i in range(lista_aux.tamanio()):
    dato=lista_aux.obtener_elemento(0)
    lista_aux.eliminar(dato)
#insertamos
for i in range(lista_peliculas.tamanio()):
    dato=lista_peliculas.obtener_elemento(i)
    lista_aux.insertar(dato,'valoracion_publico')
lista_aux.barrido()