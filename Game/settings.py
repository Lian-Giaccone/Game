import sqlite3

SCREEN = 1200, 700
FPS = 60 

def crear_tabla():
    with sqlite3.connect("Datos de Usuario.db") as conexion:
        try:
            sentencia = ''' create table usuarios
                            (
                            id integer primary key autoincrement,
                            nombre text,
                            score real
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla usuarios")
        except sqlite3.OperationalError:
            print("La tabla usuarios ya existe")

def data_user(name, score):
    with sqlite3.connect("Datos de Usuario.db") as conexion:
        try:
            conexion.execute("insert into usuarios(nombre, score) values (?,?)", (name, score))
            conexion.commit() # Actualiza los datos realmente en la tabla
        except:
            print("Error")

def show_data():
    list = []
    flag = True
    with sqlite3.connect("Datos de Usuario.db") as conexion:
        cursor=conexion.execute("SELECT nombre, score FROM usuarios")
        for row in cursor:
            mensage_final = ""
            dic = {}
            if flag == True:
                POS_Y = 100
                flag = False

            else:
                POS_Y = POS_Y + 80
            #data = list(row)
            #print(row)

            if len(row) > 0:
                for element in row:
                    mensage = "{0}".format(element)
                    mensage_final = mensage_final + mensage
                dic["data"] = [mensage_final]
                dic["pos_txt"] = [POS_Y]
                list.append(dic)

            else:
                list = []

    return list