import matplotlib.pyplot as plt
import numpy as np

# Dataset URL: https://terrabrasilis.dpi.inpe.br/app/dashboard/deforestation/biomes/amazon/increments

# dados do dataset
estados = ('Pará', 'Mato Grosso', 'Amazonas', 'Rondônia', 'Acre')
indice = np.arange(len(estados))
km = [52.39284, 23.63737, 16.76110, 16.30490, 6.82038]

# gráfico de Barras
plt.bar(indice, np.array(km) * 1000)
plt.xticks(indice, estados)
plt.ylabel('Áreas (km²)')
plt.title('Incrementos de Desmatamento Acumulado 2024')
plt.show()

# Gráfico de setores
colors = ['purple', 'green', 'yellow', 'blue', 'red']
patches, texts, autotexts = plt.pie(km, colors=colors, autopct='%1.1f%%',
startangle=90)
plt.legend(patches, estados, loc="lower right")
plt.title('Porcentagem de Incrementos de Desmatamento Acumulado 2024')
plt.axis('equal')
plt.show()

# Dados
x = [2019, 2020, 2021, 2022, 2023]  # Valores no eixo x
y1 = [4459, 4617, 5084, 4528, 2883]  # Primeira série de dados
y2 = [1826, 1777, 1920, 1981, 1905]  # Segunda série de dados
y3 = [1556, 1419, 2164, 3047, 1309]  # Terceira série de dados
y5 = [1392, 1304, 1641, 1448, 794]  # Terceira série de dados
y4 = [706, 660, 892, 1005, 462]  # Terceira série de dados

# Gráfico de Linhas
plt.plot(x, y1, marker='s', linestyle='-', color='darkgreen', label='Pará')
plt.plot(x, y2, marker='s', linestyle='-', color='yellow', label='Mato Grosso')
plt.plot(x, y3, marker='s', linestyle='-', color='green', label='Amazonas')
plt.plot(x, y4, marker='s', linestyle='-', color='blue', label='Rondônia')
plt.plot(x, y5, marker='s', linestyle='-', color='lightblue', label='Acre')

plt.title('Evolução dos Incrementos de Desmatamento por Estado')
plt.xlabel('Ano')
plt.ylabel('Áreas (km²)')
plt.legend()
plt.grid(True)
plt.show()