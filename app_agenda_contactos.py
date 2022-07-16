import os

CARPETA = 'agenda_contactos/contactos/'  # constante no se puede modificar
EXTENSION = '.txt'

# Contactos


class Contacto:
    def __init__(self, nombre, apellido, telefono, email, categoria):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.categoria = categoria


def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra el menu de opciones
    mostrar_menu()

    # Preguntar al usuario que opcion desea realizar

    preguntar = True
    while preguntar:
        opcion = input('--Ingrese una opcion--\r\n')
        # opcion = int(opcion)

        # Ejectuar las opciones
        if opcion == '1':
            agregar_contacto();
            preguntar = False;
        elif opcion == '2':
            editar_contacto();
            preguntar = False;
        elif opcion == '3':
            mostrar_contactos();
            preguntar = False;
        elif opcion == '4':
            buscar_contacto();
            preguntar = False;
        elif opcion == '5':
            eliminar_contacto();
            preguntar = False;
        elif opcion == '0':
            print('Gracias por utilizar la aplicacion')
            preguntar = False;
        else:
            mostrar_menu()
            print('Opcion no valida')

def eliminar_contacto():
    nombre = input("Nombre del contacto que deseas eliminar: \r\n")
    
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado correctamente')
    except FileNotFoundError:
        print('El contacto no existe')
    #Reiniciar app
    app();
    
def buscar_contacto():
    nombre_buscar = input("Nombre del contacto que deseas buscar: \r\n")

    try:
        with open(CARPETA + nombre_buscar + EXTENSION, 'r') as contacto:
            for linea in contacto:
                #Imprime los contenidos del archivo
                print(linea.rstrip());
            #Imprime un separador
            print('\r\n');
    except FileNotFoundError:
        print('El contacto no existe')
    app();

def mostrar_contactos():
    archivos = os.listdir(CARPETA);
    
    archivos_txt = [archivo for archivo in archivos if archivo.endswith(EXTENSION)];
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo, 'r') as contacto:
            for linea in contacto:
                #Imprime los contenidos del archivo
                print(linea.rstrip());
            #Imprime un separador
            print('\r\n');
    app();

def editar_contacto():
    print("Escribe el nombre del contacto que deseas editar: \r")
    nombre_anterior = input("Nombre del contacto que deseas editar: \r\n")

    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # Resto de los campos
            nombre_contacto = input('Agregar el Nuevo Nombre:\r\n ')
            apellido_contacto = input('Agregar el Nuevo Apellido:\r\n ')
            telefono_contacto = input('Agregar el Telefono:\r\n ')
            email_contacto = input('Agregar el Email:\r\n ')
            categoria_contacto = input('Agregar la nueva Categoria:\r\n ')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, apellido_contacto, telefono_contacto, email_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Apellido: ' + contacto.apellido + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Email: ' + contacto.email + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # Mostrar mensaje de exito
            print('Contacto editado correctamente')
    else:
        print('El contacto no existe')
        
    # renombrar el archivo   
    os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION);
    app();

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto: \r\n')
    nombre_contacto = input('Nombre del Contacto:\r\n ')

    # Revisar si el archivo existe
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # Resto de los campos
            apellido_contacto = input('Apellido del Contacto:\r\n ')
            telefono_contacto = input('Telefono del Contacto:\r\n ')
            email_contacto = input('Email del Contacto:\r\n ')
            categoria_contacto = input('Categoria del Contacto:\r\n ')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, apellido_contacto, telefono_contacto, email_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Apellido: ' + contacto.apellido + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Email: ' + contacto.email + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # Mostrar mensaje de exito
            print('-------------------------')
            print('Contacto agregado correctamente')
    else:
        print('El contacto ya existe')
    # Reiniciar la app
    app()


def mostrar_menu():
    print('-------------------------')
    print('1. Agregar contacto')
    print('2. Editar Contacto')
    print('3. Ver Contacto')
    print('4. Buscar contacto')
    print('5. Eliminar contacto')
    print('0. Salir')


def crear_directorio():
    # Si no existe
    if not os.path.exists(CARPETA):
        # crear el directorio
        os.makedirs(CARPETA)
    # else:
    #     print('El directorio ya existe')

# Revisar si el contacto existe


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()
