# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
# de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
# la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
# o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

from lista import Lista
from random import randint,choice

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas

    def __str__(self):
        return self.nombre

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"

enternadores = [
    {'name': 'Ash', 'tor_gan': 15, 'bat_gan': 45,  'bat_per': 11},
    {'name': 'Brock', 'tor_gan': 3, 'bat_gan': 12,  'bat_per': 14},
    {'name': 'Gary', 'tor_gan': 0, 'bat_gan': 23,  'bat_per': 3},
    {'name': 'Misty', 'tor_gan': 1, 'bat_gan': 10,  'bat_per': 12},
    {'name': 'Lance', 'tor_gan': 50, 'bat_gan': 57, 'bat_per': 1},
]

pokemons = [
    {'name': 'Charizard', 'nivel': 45, 'tipo': 'fuego', 'subtipo': 'volador'},
    {'name': 'Pikachu', 'nivel': 12, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'Blaziken', 'nivel': 90, 'tipo': 'fuego', 'subtipo': 'lucha'},
    {'name': 'Butterfly', 'nivel': 20, 'tipo': 'insecto', 'subtipo': 'volador'},
    {'name': 'Onix', 'nivel': 27, 'tipo': 'roca', 'subtipo': 'tierra'},
    {'name': 'Gyarados', 'nivel': 53, 'tipo': 'agua', 'subtipo': 'dragon'},
    {'name': 'Jalapeño', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'planta'},
    {'name': 'Pelipper', 'nivel': 23, 'tipo': 'agua', 'subtipo': 'volador'},
    {'name': 'Tyrantrum', 'nivel': 23, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'Terrakion', 'nivel': 23, 'tipo': 'tierra', 'subtipo': 'dragon'},
    {'name': 'Wingull', 'nivel': 23, 'tipo': 'agua', 'subtipo': 'lucha'},
]

lista_entrenadores = Lista()

for entrenador in enternadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'],
                                           entrenador['tor_gan'],
                                           entrenador['bat_per'],
                                           entrenador['bat_gan']), 'nombre')

for entrenador in enternadores:
    for i in range(randint(1, 5)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'],
                                      pokemon['nivel'],
                                      pokemon['tipo'],
                                      pokemon['subtipo']), 'nombre')

lista_entrenadores.barrido_lista_lista()
print()

# a. obtener la cantidad de Pokémons de un determinado entrenador;
entre=str(input('Ingrese entrenador para saber cuantos Pokemons posee: ')).capitalize()
pos=lista_entrenadores.busqueda(entre,'nombre')
print(entre)
if (pos):
    print(f'Cantidad de pokemon del entrenador {entre}: {pos.sublista.tamanio()}')
else:
    print('El entrenador no esta en la lista')

# b. listar los entrenadores que hayan ganado más de tres torneos;
print()
print('Entrenadores con mas de tres torneos ganados:')
lista_entrenadores.barrido_entrenador_mas_tres()
print()

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
lista_entrenadores.pokemon_mayor_nivel_entrenador_mas_torneos()
print()

#d. mostrar todos los datos de un entrenador y sus Pokémos;
entre=str(input('Ingrese entrenador para ver sus datos y sus Pokemons: ')).capitalize()
pos=lista_entrenadores.busqueda(entre,'nombre')
if (pos):
    print(entre)
    print(f'Torneos ganados: {pos.info.torneos_ganados}')
    print(f'Batallas ganadas: {pos.info.batallas_ganadas}')
    print(f'Batallas perdidas: {pos.info.batallas_perdidas}')
    print()
    print(f'Pokemons de {entre}:')
    pos.sublista.barrido()
else:
    print('No se encontro el entrenador en la lista')
print()

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print('Entrenadores que ganaron mas del 79% de sus batallas:')
lista_entrenadores.barrido_entrenador_porcentaje_ganados()
print()

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print('Entrenadores con Pokemons tipo fuego/planta o agua/volador: ')
lista_entrenadores.barrido_entrenadores_fyp_o_ayv()
print()

# g. el promedio de nivel de los Pokémons de un determinado entrenador
entre=str(input('Ingrese entrenador para saber promedio del nivel de sus Pokemons: ')).capitalize()
pos=lista_entrenadores.busqueda(entre,'nombre')
if (pos):
    lista_entrenadores.promedio_de_nivel_pokemons(pos)
else:
    print('No se encontro el entrenador en la lista')
print()

# h. determinar cuántos entrenadores tienen a un determinado Pokémon
pokemon=str(input('Ingrese el Pokemon para saber cuantos entrenadores lo tienen: ')).capitalize()
lista_entrenadores.quienes_tienen_a_este_pokemon(pokemon)
print()

# i. mostrar los entrenadores que tienen Pokémons repetidos
print('Entrenadores con Pokemons repetidos: ')
lista_entrenadores.barrido_entrenadores_poke_repetidos()
print()

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
lista_entrenadores.determinados_pokemon_ty_te_wi()
print()

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

entrenador=str(input('Ingrese el entrenador: ')).capitalize()
pokemon=str(input('Ingrese el Pokemon: ')).capitalize()
pos=lista_entrenadores.busqueda(entrenador,'nombre')
pos_poke=pos.sublista.busqueda(pokemon,'nombre')
if (pos) and (pos_poke):
    print(f'Entrenador: {pos.info.nombre}')
    print(f'Torneos ganados: {pos.info.torneos_ganados}')
    print(f'Batallas ganadas: {pos.info.batallas_ganadas}')
    print(f'Batallas perdidas: {pos.info.batallas_perdidas}')
    print()
    print(f'Pokemon: {pos_poke.info.nombre}')
    print(f'Nivel: {pos_poke.info.nivel}')
    print(f'Tipo: {pos_poke.info.tipo}')
    print(f'Subtipo: {pos_poke.info.subtipo}')
else:
    print('El entrenador no tiene a ese Pokemon o el entranador no está en la lista')