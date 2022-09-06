#Realiza la conexión a MySql y genera consulta de tabla
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='gituser',
    password = 'L0ok4tm3#1',
    database='BaseDeDatos'
)

cursor = conexion.cursor()

cursor.execute("Select * from Usuario");


resultado = cursor.fetchall()
print(resultado);

#sql_insertaUsuario = "insert into usuario (email, username, edad) values (%s, %s, %s)"
#values_usuario = ("micorreo2@hotmail.com", "miuser2", 45)
#cursor.execute(sql_insertaUsuario, values_usuario)
#cursor.execute("Select * from Usuario");
#resultado = cursor.fetchall()
print("Contador:" + str(cursor.rowcount))
