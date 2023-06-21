import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)
class CalculaGanador:

    def leerdatos(self):
        data = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append( fila)
        return data

    def calcularganador(self, data):
        votosxcandidato = {}
        for fila in data:
            if not fila[4] in votosxcandidato:
                votosxcandidato[fila[4]] = 0
            if fila[5] == '1':
                votosxcandidato[fila[4]] = votosxcandidato[fila[4]] + 1
        for candidato in votosxcandidato:
            print('candidato: ' + candidato + ' votos validos: ' + str(votosxcandidato[candidato]))
        max_votos = max(votosxcandidato.values())
        ganadores = [candidato for candidato, votos in votosxcandidato.items() if votos == max_votos]
        return ganadores

c = CalculaGanador()
data = c.leerdatos()
print(c.calcularganador(data))