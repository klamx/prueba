import sqlite3
from sqlite3.dbapi2 import Error

con = sqlite3.connect("plus.db")

PREGUNTAS = []
OBJETOS = []
RESPUESTAS = []


def traer_preguntas(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM PREGUNTAS")
    return cursorObj.fetchall()


def traer_objetos(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM OBJETOS")
    return cursorObj.fetchall()


def traer_respuetas(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM RESPUESTAS")
    return cursorObj.fetchall()


def hacer_preguntas(preguntas, dict):
    cursorObj = con.cursor()
    respuestas = []
    respuesta = ""
    keys = dict.keys()

    print("Responda [si/no]:", end="\n")
    for x in range(len(preguntas)):
        respuesta = input(preguntas[x][1] + " ")
        if respuesta == "si":
            cursorObj.execute(
                'SELECT pregunta_id FROM PREGUNTAS WHERE enunciado = "{0}"'.format(
                    preguntas[x][1]
                )
            )
            id_pregunta = cursorObj.fetchone()
            # print("preguntas", id_pregunta)

            # ------------ mal ---------------
            for key in keys:
                dict[key] += 1

            respuestas.append([1, id_pregunta[0], respuesta])

        if respuesta == "no":
            cursorObj.execute(
                'SELECT pregunta_id FROM PREGUNTAS WHERE enunciado = "{0}"'.format(
                    preguntas[x][1]
                )
            )
            id_pregunta = cursorObj.fetchone()
            # print("preguntas", id_pregunta)

            respuestas.append([1, id_pregunta[0], respuesta])
    print(dict)
    print(respuestas)

    return respuestas, dict


def llenar_diccionario(objetos):
    dict = {}
    for obj in objetos:
        dict[obj[1]] = 0
    return dict


def nuevo_objeto(respuestas, nombre):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO OBJETOS (nombre) VALUES("{0}")'.format(nombre))
    con.commit()
    cursorObj.execute(
        'SELECT objeto_id FROM OBJETOS WHERE nombre = "{0}"'.format(nombre)
    )
    id = cursorObj.fetchone()
    for item in range(len(respuestas)):
        respuestas[item][0] = id
        cursorObj.execute(
            """INSERT INTO RESPUESTAS (objeto_id, pregunta_id, respuesta) VALUES (?,?,?)""",
            (
                str(respuestas[item][0]),
                str(respuestas[item][1]),
                str(respuestas[item][2]),
            ),
        )

        con.commit()


if __name__ == "__main__":
    PREGUNTAS = traer_preguntas(con)
    OBJETOS = traer_objetos(con)
    RESPUESTAS = traer_respuetas(con)
    dict = llenar_diccionario(OBJETOS)
    respuestas_usuario, dict = hacer_preguntas(PREGUNTAS, dict)

    preguntar_por_objeto = input(
        "El objeto es " + max(dict, key=dict.get) + "? [si/no]: "
    )
    if preguntar_por_objeto == "no":
        nombre_objeto = input("Que objeto es? ")
        nuevo_objeto(respuestas_usuario, nombre_objeto)
