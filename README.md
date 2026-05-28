# sistema_diagnostico_glucosa
Sistema que calcula la media entre varias medidas de la glucosa (mg/dL) y evalúa si el valor calculado se encuentra en un rango normal o si el paciente presenta hipoglucemia o hiperglucemia.
## 📚 Referencias Clínicas

Los rangos de referencia utilizados para la evaluación diagnóstica en este sistema corresponden a mediciones de **glucosa en sangre en ayunas**. Los valores están basados en las guías clínicas de instituciones médicas de referencia:

* **Mayo Clinic - Diagnóstico de la Prediabetes y Diabetes:** [https://www.mayoclinic.org/es/diseases-conditions/prediabetes/diagnosis-treatment/drc-20355284](https://www.mayoclinic.org/es/diseases-conditions/prediabetes/diagnosis-treatment/drc-20355284)
* **NIDDK (Institutos Nacionales de la Salud, EE.UU.):** [https://www.niddk.nih.gov/health-information/informacion-de-la-salud/diabetes/informacion-general/que-es/resistencia-insulina-prediabetes](https://www.niddk.nih.gov/health-information/informacion-de-la-salud/diabetes/informacion-general/que-es/resistencia-insulina-prediabetes)

*Nota técnica:* Para simplificar la lógica de evaluación en este proyecto académico, el algoritmo agrupa cualquier resultado de 100 mg/dL o superior (que clínicamente abarcaría tanto la prediabetes como la diabetes) bajo el estado general de "hiperglucemia".
