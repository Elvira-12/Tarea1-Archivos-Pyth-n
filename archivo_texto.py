archivo_texto.py
# Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    file.write("Hoy empecé mi tarea de programación en Python.\n")
    file.write("Estoy aprendiendo a crear y leer archivos de texto.\n")
    file.write("Copilot me está ayudando paso a paso y me siento más segura.\n")

# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
