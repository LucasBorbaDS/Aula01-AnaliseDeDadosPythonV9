import csv

with open('csv_aula.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)