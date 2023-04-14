import wikipedia

# Establecer el idioma a español
wikipedia.set_lang("es")

while True:
    busqueda = input("Ingresa el término que deseas buscar en Wikipedia: ")
    if busqueda.lower() == 'q':
        # Salir del bucle si el usuario ingresa 'q' para salir
        break

    try:
        resultado = wikipedia.page(busqueda)
        print(resultado.summary)
        # Mostrar mensaje para volver a preguntar
        print("\nConsulta exitosa. Puedes ingresar otro término de búsqueda o 'q' para salir.")
    except wikipedia.DisambiguationError as e:
        print("El término de búsqueda es ambiguo. Por favor, especifica más.")
        print("Opciones sugeridas: ")
        for option in e.options:
            print("- " + option)
    except wikipedia.PageError:
        print("No se encontró una página en Wikipedia para el término de búsqueda ingresado.")
