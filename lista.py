
def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoLista():
    info, sig, sublista = None, None, None


class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sublista = Lista()

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def lista_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    
    def barrido_entrenador_mas_tres(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.torneos_ganados > 3):
                print(aux.info)
            aux = aux.sig

    def pokemon_mayor_nivel_entrenador_mas_torneos(self):
        mayor=self.__inicio
        aux=self.__inicio
        while(aux is not None):
            if(aux.info.torneos_ganados>mayor.info.torneos_ganados):
                mayor=aux
            aux=aux.sig

        poke_aux=mayor.sublista.__inicio
        mayor_poke=mayor.sublista.__inicio
        while(poke_aux is not None):
            if(poke_aux.info.nivel>mayor_poke.info.nivel):
                mayor_poke=poke_aux
            poke_aux=poke_aux.sig 
        print()
        print(f'El entrenador con mas torneos ganados es {mayor.info}')
        print(f'Pokemon de mas nivel de {mayor.info} es {mayor_poke.info.nombre}')              
        print()

    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('Pokemons:')
            aux.sublista.barrido()
            aux = aux.sig
            print()

    # def barrido_porcentaje_victorias(self):
    #     aux = self.__inicio
    #     while(aux is not None):
    #         total = aux.info.batallas_ganadas + aux.info.batallas_perdidas
    #         if(aux.info.batallas_ganadas / total >= 0.79):
    #             print(aux.info)
    #         aux = aux.sig

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
        if dato:
            self.__tamanio -= 1 

        return dato

    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None
   
    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
                break
            aux = aux.sig
        return 
    
    def barrido_entrenador_porcentaje_ganados(self):
        aux = self.__inicio
        while(aux is not None):
            porcentaje=(aux.info.batallas_ganadas*100)/(aux.info.batallas_ganadas+aux.info.batallas_perdidas)
            if(porcentaje > 79):
                print(f'{aux.info}: {round(porcentaje,2)}%') #round para mostrar solo dos numeros despues de la coma
            aux = aux.sig

    def barrido_entrenadores_fyp_o_ayv(self):
        aux=self.__inicio
        while(aux is not None):
            poke_aux=aux.sublista.__inicio
            while(poke_aux is not None):
                if((poke_aux.info.tipo=='fuego' and poke_aux.info.subtipo=='planta') or(poke_aux.info.tipo=='agua' and poke_aux.info.subtipo=='volador')):
                    print(aux.info)
                    break           #break para que corte una vez que encuentre que tiene ese tipo de pokemon y no vuelva a repetir el nombre 
                poke_aux=poke_aux.sig
            aux=aux.sig
    
    def promedio_de_nivel_pokemons(self,pos):
        poke_aux=pos.sublista
        aux=poke_aux.__inicio
        promedio=0
        while(aux is not None):
            promedio=promedio+aux.info.nivel
            aux=aux.sig
        print(f'Promedio de nivel de los Pokemons de {pos.info.nombre}: {round(promedio/poke_aux.tamanio(),0)}')

    def quienes_tienen_a_este_pokemon(self,pokemon):
        aux=self.__inicio
        cont=0
        while(aux is not None):
            aux_poke=aux.sublista
            poke=aux_poke.__inicio
            while(poke is not None):
                if(poke.info.nombre==pokemon):
                    cont+=1
                    break    #para que no lo cuente de nuevo si está repetido
                poke=poke.sig
            aux=aux.sig 
        print(f'{cont} entrenadores tienen a {pokemon}')
        
    def barrido_entrenadores_poke_repetidos(self):
        aux=self.__inicio
        while(aux is not None):
            poke_lista=aux.sublista
            poke=poke_lista.__inicio
            poke_sig=poke.sig
            while(poke_sig is not None):
                if (poke.info.nombre==poke_sig.info.nombre):
                    print(aux.info.nombre)
                    break    #para que no vuelva al entrenador
                poke=poke.sig
                poke_sig=poke_sig.sig
            aux=aux.sig

    def determinados_pokemon_ty_te_wi(self):
        aux=self.__inicio
        while(aux is not None):
            aux_poke=aux.sublista
            poke=aux_poke.__inicio
            while(poke is not None):
                if(poke.info.nombre=='Tyrantrum' or poke.info.nombre=='Terrakion' or poke.info.nombre=='Wingull'):
                    print(f'El entrenador {aux.info.nombre} tiene un {poke.info.nombre}.')
                poke=poke.sig
            aux=aux.sig           
            
    def entrenador_y_pokemon_ingresados(self,entrenador,pokemon):
        aux=self.__inicio
        while(aux is not None):
            aux_poke=aux.sublista
            poke=aux_poke.__inicio
            while(poke is not None):
                
                poke=poke.sig
            aux=aux.sig           
            
    def pelicula_que_mas_recaudo(self):
        aux=self.__inicio
        mayor=aux.sig
        
        while(aux is not None):
            if (aux.info.recaudacion>mayor.info.recaudacion):
                mayor=aux
            aux=aux.sig
        print(f'La pelicula que mas recaudo fue {mayor.info.nombre}')
        print(f'Año de estreno: {mayor.info.anio_estreno}')
        print(f'Valoracion del publico: {mayor.info.valoracion_publico}/10')
        print(f'Dinero recaudado: {mayor.info.recaudacion}')

    def barrido_x_anio(self,anio):
        aux=self.__inicio
        control=False
        while(aux is not None):
            if (aux.info.anio_estreno==anio):
                print(aux.info.nombre)
                control=True
            aux=aux.sig    
        if(not control):
            print('No hay peliculas estrenadas ese año')

    def barrido_valoracio_publico(self):
        aux=self.__inicio
        control=False
        while(aux is not None):
            if(aux.info.valoracion_publico>=8):
                print(f'{aux.info.nombre} {aux.info.valoracion_publico}/10')
                control=True
            aux=aux.sig
        if(not control):
            print('No hubo buena valoracion de las peliculas de la lista.')

    def padawans_de(self,maestro=[]):
        aux=self.__inicio
        control=False   #para cuando no tenga alumnos el jedi
        while(aux is not None):
            if (maestro in aux.info.maestro):
                control=True
                print(aux.info.nombre)
            aux=aux.sig
        if not control:
            print('El Jedi no tubo padawans')

    def barrido_humanos(self):
        aux=self.__inicio
        while(aux is not None):
            if ('humano' in aux.info.especie):
                print(aux.info.nombre)
            aux=aux.sig
    def barrido_twi_lek(self):
        aux=self.__inicio
        while(aux is not None):
            if ("twi'lek" in aux.info.especie):
                print(aux.info.nombre)
            aux=aux.sig
    
    def barrido_comienza_con(self, inicial=[]):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] == inicial):
                print(aux.info.nombre)
            aux = aux.sig
    
    def barrido_sable_mas_de_uno(self):
        aux = self.__inicio
        while(aux is not None):
            if(len(aux.info.sable_luz)>1):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_amarillo_violeta(self):
        aux = self.__inicio
        while(aux is not None):
            if('amarillo' in aux.info.sable_luz or 'violeta' in aux.info.sable_luz):
                print(aux.info.nombre)
            aux = aux.sig
    
