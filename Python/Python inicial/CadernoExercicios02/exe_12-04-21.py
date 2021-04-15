from math import pi
diametro = float(input("Diâmetro(mm): "))
altura = float(input("Altura(mm): "))

def calculoVolumeCopo(diametro, altura):
    raio = diametro/2
    volume_cm = raio**2 * pi /100

    volume_mililitros = volume_cm / 1000



    return print(round(volume_cm, 2), "mm³. ", round(volume_mililitros, 2), 'Litros' )


calculoVolumeCopo(diametro, altura)

