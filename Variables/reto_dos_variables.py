# Reto 2 - Planificando una Actividad (Grupos Pequeños):
"""Escenario Cotidiano: Imaginen que están planeando una pequeña actividad con sus amigos
para después del cole o el fin de semana (ir por un helado, jugar fútbol, estudiar juntos, ir al
parque).
En grupo, pónganse de acuerdo sobre una actividad."
Ahora, creen un nuevo archivo de Python (o borren lo anterior) y definan las siguientes
variables para planificar su actividad:
"""

# nombre_actividad (str): El nombre que le darán a la actividad (Ej: "Tarde de Fut","Helados Post-Cole").
# variable de tipo texto (string) se encierra entre comillas dobles o simples
nombre_actividad = "Tarde peliculas con los con mis estudiantes"

# numero_participantes (int): ¿Cuántas personas en total participarán (incluyéndose ustedes)?
# variable de tipo entera porque recibe un número positivo
numero_participantes = 32 

# costo_estimado_persona (float): ¿Cuánto calculan que gastará más o menos cada persona? (Ej: 2500.50 colones). Si es gratis, pueden poner 0.0.
# variable de tipo decimal (float) porque tiene un punto 
costo_estimado_persona = 2500.50 
# es_fin_de_semana (bool): ¿La actividad será en fin de semana (True) o entre semana (False)?
# variable de tipo booleana True (verdadero) o False (Falso)
es_fin_de_semana = True 
# lugar (str): ¿Dónde se realizará la actividad? (Ej: "Parque La Sabana", "Soda del Cole", "Casa de Ana").

lugar = "Casa de Miguel en Tucurrique"

# "Usen print() para mostrar la información de su plan de forma ordenada."

print("Mostrando los datos de la actividad: ")
print(nombre_actividad)
print(numero_participantes)
print(costo_estimado_persona)
print(es_fin_de_semana)
print(lugar)

#¡Extra! Si terminan rápido: Calculen el costo_total_estimado multiplicandonumero_participantes por costo_estimado_persona y muéstrenlo.
# Se crea una variable nueva costo_total_estimado, que almacena el resultado de multiplicar numero_participantes por costo_estimado_persona
costo_total_estimado = numero_participantes * costo_estimado_persona 
print("El costo total es: ", costo_total_estimado)