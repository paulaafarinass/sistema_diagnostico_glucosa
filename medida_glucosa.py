from calcular_glucosa import calculo_glucosa
from informe_medico import generar_informe
datos_paciente={"Nombre":"", "Medidas":[]}
while True:
    print("(1): Introducir datos del paciente")
    print("(2): Salir del menú")
    print("(3): leer los datos de un archivo")
    seleccion=input("Selecciona una opción: 1, 2 o 3: ")
    if seleccion=="1":
        lista_medidas=[]
        paciente=input("Introduce el nombre del paciente: ")
        datos_paciente["Nombre"]=paciente
        contador=0
        while contador<3:
            try:
                medida=float(input("Introduce el valor de la medida (mg/dL): "))
                lista_medidas.append(medida)
                contador+=1
            except ValueError:
                print("Dato no válido, se debe introducir un valor numérico decimal o entero")
        datos_paciente["Medidas"]=lista_medidas
        media=sum(lista_medidas)/len(lista_medidas)
        resultado_diagnostico=calculo_glucosa(media)
        print(resultado_diagnostico)
        informe=generar_informe(paciente,media,resultado_diagnostico)
        print(informe)
    elif seleccion=="2":
        print("Se ha salido del menú")
        break
    elif seleccion=="3":
        try:
            with open("glucosa.txt","r") as archivo: #read lee todo el archivo hasta el final y ya no se puede trabajar con él
                nombre=archivo.readline().strip() #readline lee una sola línea y mueve el puntero a la siguiente
                datos_paciente["Nombre"]=nombre
                lista_medidas=[]
                for linea in archivo:
                    valor_sin_espacios=linea.strip()
                    valor_numero=float(valor_sin_espacios)
                    lista_medidas.append(valor_numero)
                datos_paciente["Medidas"]=lista_medidas
                media=(sum(lista_medidas))/(len(lista_medidas))
                resultado_diagnostico=calculo_glucosa(media)
                print(resultado_diagnostico)
                informe=generar_informe(nombre,media,resultado_diagnostico)
                print(informe)
        except FileNotFoundError:
            print("El archivo no existe")
        except ValueError:
            print("Alguno de los datos presenta un formato incorrecto")            
    else:
        print("Opción no valida")
        
        



