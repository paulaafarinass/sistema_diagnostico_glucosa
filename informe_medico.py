def generar_informe(nombre,medida,diagnostico):
    nombre_a=f"paciente.{nombre}.txt"
    with open(nombre_a,"w") as archivo:
        archivo.write(f"Nombre del paciente: {nombre}\n")
        archivo.write(f"Nivel de glucosa medio: {medida}\n")
        archivo.write(f"Estado: {diagnostico}\n")
        informe_creado=f"Informe creado como: {nombre_a}"

    return informe_creado
                      
        