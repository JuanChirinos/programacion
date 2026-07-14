
peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}


# 2. Funciones de Operación del Sistema

def cupos_genero(genero):
    total_cupos = 0
    genero_buscado = genero.strip().lower()
    
    for cod, info in peliculas.items():
        if info[1].strip().lower() == genero_buscado:
            if cod in cartelera:
                total_cupos += cartelera[cod][1]
                
    print(f"El total de cupos disponibles es: {total_cupos}")


def busqueda_precio(p_min, p_max):
    resultados = []
    for cod, info_cart in cartelera.items():
        precio, cupos = info_cart[0], info_cart[1]
        if p_min <= precio <= p_max and cupos > 0:
            if cod in peliculas:
                titulo = peliculas[cod][0]
                resultados.append((titulo, cod))
                
    if not resultados:
        print("No hay películas en ese rango de precios.")
    else:
        resultados.sort(key=lambda x: x[0].lower())
        lista_formateada = [f"{t}--{c}" for t, c in resultados]
        
        print(f"Las películas encontradas son: {', '.join(lista_formateada)}")


def actualizar_precio(codigo, nuevo_precio):
    cod_upper = codigo.strip().upper()
    if cod_upper in cartelera:
        cartelera[cod_upper][0] = nuevo_precio
        return True
    return False


def eliminar_pelicula(codigo):
    cod_upper = codigo.strip().upper()
    if cod_upper in peliculas and cod_upper in cartelera:
        del peliculas[cod_upper]
        del cartelera[cod_upper]
        return True
    return False


# 3. Funciones de Validación (Opción 4 — Agregar Película)

def validar_codigo(codigo):
    if not isinstance(codigo, str):
        return False
    cod_clean = codigo.strip().upper()
    if cod_clean == "" or cod_clean in peliculas or cod_clean in cartelera:
        return False
    return True

def validar_titulo(titulo):
    if not isinstance(titulo, str):
        return False
    return titulo.strip() != ""

def validar_genero(genero):
    if not isinstance(genero, str):
        return False
    return genero.strip() != ""

def validar_duracion(duracion):
    try:
        dur = int(duracion)
        return dur > 0
    except (ValueError, TypeError):
        return False

def validar_clasificacion(clasificacion):
    if not isinstance(clasificacion, str):
        return False
    
    return clasificacion.strip().upper() in ['A', 'B', 'C']

def validar_idioma(idioma):
    if not isinstance(idioma, str):
        return False
    return idioma.strip() != ""

def validar_es_3d(es_3d):
    if not isinstance(es_3d, str):
        return False
    return es_3d.strip().lower() in ['s', 'n']

def validar_precio(precio):
    try:
        p = int(precio)
        return p > 0
    except (ValueError, TypeError):
        return False

def validar_cupos(cupos):
    try:
        c = int(cupos)
        return c >= 0
    except (ValueError, TypeError):
        return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    cod_upper = codigo.strip().upper()
    if cod_upper in peliculas or cod_upper in cartelera:
        return False
    
    dur_int = int(duracion)
    precio_int = int(precio)
    cupos_int = int(cupos)
    es_3d_bool = True if es_3d.strip().lower() == 's' else False
    
    # MEJORA: Se guarda la clasificación formateada en mayúscula
    peliculas[cod_upper] = [titulo.strip(), genero.strip(), dur_int, clasificacion.strip().upper(), idioma.strip(), es_3d_bool]
    cartelera[cod_upper] = [precio_int, cupos_int]
    return True


# 4. Programa Principal (Flujo e Interfaz de Menú)

def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
        
        opcion = input("Ingrese opción: ").strip()
        print() 
        
        if opcion == '1':
            genero = input("Ingrese género a consultar: ")
            cupos_genero(genero)
            
        elif opcion == '2':
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    if p_min < 0:
                        print("El precio debe ser mayor o igual a cero.")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            
            while True:
                try:
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_max < 0:
                        print("El precio debe ser mayor o igual a cero.")
                        continue
                    if p_max < p_min:
                        print("El precio máximo debe ser mayor o igual al precio mínimo.")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
                    
            busqueda_precio(p_min, p_max)

        elif opcion == '3':
            while True:
                codigo = input("Ingrese código de película: ")
                
                while True:
                    try:
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                        if nuevo_precio > 0:
                            break
                        else:
                            print("El precio debe ser un número entero mayor que cero.")
                    except ValueError:
                        print("Debe ingresar valores enteros")
                
                if actualizar_precio(codigo, nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                
                otro = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if otro != 's':
                    break

        elif opcion == '4':
            # MEJORA UX: Validar el código AL PRINCIPIO del flujo de captura
            codigo = input("Ingrese código de película: ")
            if not validar_codigo(codigo):
                if codigo.strip() == "":
                    print("Error: El código no puede estar vacío ni contener solo espacios.")
                else:
                    print("El código ya existe")
                continue # Regresa directamente al menú principal sin pedir el resto de datos
            
            # Si el código es válido, procedemos con los demás datos
            titulo = input("Ingrese título: ")
            genero = input("Ingrese género: ")
            duracion = input("Ingrese duración (minutos): ")
            clasificacion = input("Ingrese clasificación: ")
            idioma = input("Ingrese idioma: ")
            es_3d = input("¿Es 3D? (s/n): ")
            precio = input("Ingrese precio: ")
            cupos = input("Ingrese cupos: ")
            
            todo_valido = True
            
            if not validar_titulo(titulo):
                print("Error: El título no debe estar vacío ni contener solo espacios.")
                todo_valido = False
                
            if todo_valido and not validar_genero(genero):
                print("Error: El género no debe estar vacío ni contener solo espacios.")
                todo_valido = False
                
            if todo_valido and not validar_duracion(duracion):
                print("Error: La duración debe ser un número entero mayor que cero.")
                todo_valido = False
                
            if todo_valido and not validar_clasificacion(clasificacion):
                print("Error: La clasificación debe ser exactamente 'A', 'B' o 'C'.")
                todo_valido = False
                
            if todo_valido and not validar_idioma(idioma):
                print("Error: El idioma no debe estar vacío ni contener solo espacios.")
                todo_valido = False
                
            if todo_valido and not validar_es_3d(es_3d):
                print("Error: Para la opción 3D se debe ingresar exactamente 's' o 'n'.")
                todo_valido = False
                
            if todo_valido and not validar_precio(precio):
                print("Error: El precio debe ser un número entero mayor que cero.")
                todo_valido = False
                
            if todo_valido and not validar_cupos(cupos):
                print("Error: Los cupos deben ser un número entero mayor o igual a cero.")
                todo_valido = False
                
            if todo_valido:
                if agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
                    print("Película agregada")
                else:
                    print("El código ya existe")

        elif opcion == '5':
            codigo = input("Ingrese código de película: ")
            if eliminar_pelicula(codigo):
                print("Película eliminada")
            else:
                print("El código no existe")

        elif opcion == '6':
            print("Programa finalizado.")
            break
            
        else:
            print("Debe seleccionar una opción válida")


if __name__ == '__main__':
    main()