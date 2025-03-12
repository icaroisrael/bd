peso = float(input("Digite seu peso"))
altura = float(input("Digite sua altura"))
imc = peso / (altura * altura)
if(imc <18.5):
    print("Desnutrido", imc)
elif(imc <=24.5):
    print("Normal ", imc)
elif(imc < 29.9):
    print("Sobre peso ", imc)
else:
    print("Obeso", imc)
