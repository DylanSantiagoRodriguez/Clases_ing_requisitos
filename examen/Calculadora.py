class Calculadora:
    def sumar(self, num_uno, num_dos):
        return num_uno + num_dos

    def restar(self, num_uno, num_dos):
        return num_uno - num_dos

    def multiplicar(self, num_uno, num_dos):
        return num_uno * num_dos

    def dividir(self, num_uno, num_dos):
        if num_dos != 0:
            return num_uno / num_dos
        else:
            return "Error: No se puede dividir por cero."

num_uno = int(input("Ingrese el primer número(entero): "))
num_dos = int(input("Ingrese el segundo número(entero): "))

alcculadora_calc = Calculadora()
uso=("¿Que operacion desea realizar?(suma, resta, multiplicacion, division o todas):")
if uso == "suma":
    resultado_suma = alcculadora_calc.sumar(num_uno, num_dos)
    print("Suma: ",resultado_suma)
elif uso == "resta":
    resultado_resta = alcculadora_calc.restar(num_uno, num_dos)
    print("Resta: ",resultado_resta)
elif uso == "multiplicacion":
    resultado_multiplicacion = alcculadora_calc.multiplicar(num_uno, num_dos)
    print("Multiplicación: ",resultado_multiplicacion)
elif uso == "division":
    resultado_division = alcculadora_calc.dividir(num_uno, num_dos)
    print("División: ",resultado_division)
elif uso =="todas":  
    resultado_suma = alcculadora_calc.sumar(num_uno, num_dos)
    resultado_resta = alcculadora_calc.restar(num_uno, num_dos)
    resultado_multiplicacion = alcculadora_calc.multiplicar(num_uno, num_dos)
    resultado_division = alcculadora_calc.dividir(num_uno, num_dos)

    print("Suma: ",resultado_suma)
    print("Resta: ",resultado_resta)
    print("Multiplicación: ",resultado_multiplicacion)
    print("División: ",resultado_division)
else:
    print("Opcion incorrecta")
