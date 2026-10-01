import csv

with open('csv_aula.csv', 'r') as file:
    leitor_csv = csv.reader(file)
    for linha in leitor_csv:
        print(linha)