def calculo_glucosa(medida):
    if medida>70 and medida<100:

        diagnostico=f"El paciente se encuentra en el rango normal (entre 70 mg/dL y 100 mg/dL)"

    elif medida<70:

        diagnostico=f"El paciente presenta hipoglucemia (menos de 70 mg/dL)"

    else:

        diagnostico=f"El paciente presenta hiperglucemia (más de 100 mg/dL)"

    return diagnostico