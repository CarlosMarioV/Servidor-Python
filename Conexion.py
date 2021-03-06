
__author__ = 'Carlos Mario'
import mysql.connector
from mysql.connector import MySQLConnection, Error

from DTO import *

# Variable con la configuracion de la conexion
config_mysql = {
    'user': 'root', #Nombre de usuario
    'password': '2016',#La contraseña de la base de datos
    'host': 'localhost',#127.0.0.1 #El host que va a utilizar.
    'database': 'veterinariaEYC',#Nombre de la base de datos, en este caso es un ejemplo de ella misma
}

# conectamos al servidor MySql
conexion_mysql = mysql.connector.connect(**config_mysql)

#Cursor de conexion.
cursor = conexion_mysql.cursor()

#Ejecutando una consulta de la base DB
#cursor.execute("select * from city")
#Cerramos la variable encargada de las consultas y la conexion
cursor.close()
conexion_mysql.close()

def listar(nombreTabla):
    conexion_mysql = mysql.connector.connect(**config_mysql)
    cursor = conexion_mysql.cursor()
    cursor.execute("Select * from "+ nombreTabla().getClase())
    listaElementos = []
    for (nombre, descripcion, foto) in cursor:
        nuevo = nombreTabla()
        nuevo.setNombre(nombre)
        nuevo.setDescripcion(descripcion)

        decodificada = foto.decode('utf8')
        nuevo.setFoto(decodificada)
        listaElementos.append(nuevo)
    cursor.close()
    conexion_mysql.close()
    return listaElementos

def listarDosis():
    conexion_mysql = mysql.connector.connect(**config_mysql)
    cursor = conexion_mysql.cursor()
    cursor.execute("Select * from Dosis")
    listaElementos = []
    for (id,animal,medicamento,enfermedad,minPeso,maxPeso,dosis) in cursor:
        nuevo = Dosis()
        nuevo.setID(id)
        nuevo.setAnimal(animal)
        nuevo.setMedicamento(medicamento)
        nuevo.setEnfermedad(enfermedad)
        nuevo.setRangoPeso(minPeso,maxPeso)
        nuevo.setDosis(dosis)
        listaElementos.append(nuevo)
    cursor.close()
    conexion_mysql.close()
    return listaElementos

def listarPrescripciones():
    conexion_mysql = mysql.connector.connect(**config_mysql)
    cursor = conexion_mysql.cursor()
    cursor.execute("Select * from Prescripcion")
    listaElementos = []
    for (id,usuario, animal, enfermedad, peso, idDosis) in cursor:
        nuevo = Prescripcion()
        nuevo.setID(id)
        nuevo.setUsuario(usuario)
        nuevo.setAnimal(animal)
        nuevo.setEnfermedad(enfermedad)
        nuevo.setPeso(peso)
        nuevo.setDosis(idDosis)
        listaElementos.append(nuevo)
    cursor.close()
    conexion_mysql.close()
    return listaElementos

#Recorre la consulta hecha, los campos recibidos se transforma en lo que son ejemplo un int, viene aka como un int.
for (Campo1, Campo2, Campo3,Campo4, Campo5) in cursor:
    print("Campo1: ", Campo1, ", Campo2: " + Campo2 + ", Campo3: " + Campo3 + ",Campo4: " + Campo4 + ",Campo5: ",Campo5)



def obtenerUsuarioBD():
    conexion_mysql = mysql.connector.connect(**config_mysql)
    cursor = conexion_mysql.cursor()
    cursor.execute("Select * from usuario")
    listaUsuarios = []
    for (login, contrasena, nombre, permiso, foto) in cursor:
        nuevo = Usuario()
        nuevo.setLogin(login)
        nuevo.setPassword(contrasena)
        nuevo.setNombre(nombre)
        nuevo.setPermiso(permiso)
        nuevo.setFoto(foto)
        listaUsuarios.append(nuevo)
    cursor.close()
    conexion_mysql.close()
    return listaUsuarios

#************************************************

def insertarUsuarioBD(login, contrasena, nombre, permiso,foto):
    #prepare update query and data
    query = "INSERT INTO usuario(login, contrasena, nombre, permiso, foto)VALUES(%s,%s,%s,%s,%s)"

    args = (login, contrasena, nombre, permiso,foto)
    error = "¡Exito!"
    try:
        conexion_mysql = mysql.connector.connect(**config_mysql)
        cursor = conexion_mysql.cursor()
        cursor.execute(query, args)
        conexion_mysql.commit()
    except Error as e:
        error = e
    finally:
        cursor.close()
        conexion_mysql.close()
    return error

def ModificarBD(nombretabla,nuevaDesc, nuevaFoto,nombre):
    query = ""
    if (nombretabla == "Animal"):
        query = "update Animal "
    elif (nombretabla == "Enfermedad"):
        query = "update Enfermedad "
    elif (nombretabla == "Medicamento"):
        query = "update Medicamento "
    query += "set descripcion = %s,foto = %s Where nombre = %s"
    args = (nuevaDesc,nuevaFoto,nombre)
    error = "Exito!"
    try:
        conexion_mysql = mysql.connector.connect(**config_mysql)
        cursor = conexion_mysql.cursor()
        cursor.execute(query, args)
        error = cursor.rowcount
        conexion_mysql.commit()
    except Error as e:
        error = e
    finally:
        cursor.close()
        conexion_mysql.close()
    return error

def ModificarUsuarioBD(nuevaPass, nuevoNombre,nuevoPermiso,nuevaFoto,nombre):
    query = "update Usuario set contrasena = %s,nombre = %s,permiso = %s,foto = %s Where login = %s"
    args = (nuevaPass,nuevoNombre,nuevoPermiso,nuevaFoto,nombre)
    error = "Exito!"
    try:
        conexion_mysql = mysql.connector.connect(**config_mysql)
        cursor = conexion_mysql.cursor()
        cursor.execute(query, args)
        error = cursor.rowcount
        conexion_mysql.commit()
    except Error as e:
        error = e
    finally:
        cursor.close()
        conexion_mysql.close()
    return error

def ModificarDosisBD(animal,medicamento,enfermedad,minPeso,maxPeso,dosis,id):
    query = "update Dosis set animal = %s,medicamento = %s,enfermedad = %s," \
            "minPeso = %s, maxPeso = %s, dosis = %s Where id = %s"
    args = (animal,medicamento,enfermedad,minPeso,maxPeso,dosis,id)
    error = "Exito!"
    try:
        conexion_mysql = mysql.connector.connect(**config_mysql)
        cursor = conexion_mysql.cursor()
        cursor.execute(query, args)
        error = cursor.rowcount
        conexion_mysql.commit()
    except Error as e:
        error = e
    finally:
        cursor.close()
        conexion_mysql.close()
    print(error)
    return error

def ModificarPrescripcionBD(usuario, animal, enfermedad,peso, idDosis, id):
    query = "update Prescripcion set usuario = %s, animal = %s, enfermedad = %s," \
            "peso = %s, idDosis = %s Where id = %s"
    args = (usuario, animal, enfermedad,peso, idDosis, id)
    error = "Exito!"
    try:
        conexion_mysql = mysql.connector.connect(**config_mysql)
        cursor = conexion_mysql.cursor()
        cursor.execute(query, args)
        error = cursor.rowcount
        conexion_mysql.commit()
    except Error as e:
        error = e
    finally:
        cursor.close()
        conexion_mysql.close()
    print(error)
    return error

