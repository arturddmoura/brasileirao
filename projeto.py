import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

time = input("Deseja informações de que time? ")
ano_input = input("Você quer dados de que ano? ")

path_jogos = "https://github.com/juvenalfonseca/python/blob/master/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-jogos.csv?raw=true"

df_jogos = pd.read_csv(path_jogos, delimiter = ";")

categoria = ["Mandante", "Visitante", "Vencedor"]
visitante = df_jogos["Visitante"] == time
mandante = df_jogos["Mandante"] == time
vencedor = df_jogos["Vencedor"] == time

empate = df_jogos["Vencedor"] == "-"
ano = df_jogos["Data"].str.contains(ano_input)

mandante_vitorias = df_jogos[mandante & vencedor & ano]
visitante_vitorias = df_jogos[visitante & vencedor & ano]

mandante_empates = df_jogos[mandante & empate & ano]
visitante_empates = df_jogos[visitante & empate & ano]

mandante_derrotas = df_jogos[(mandante == True) & (vencedor == False) & (ano == True)]
visitante_derrotas = df_jogos[(visitante == True) & (vencedor == False) & (ano == True)]
mandante_derrotas = mandante_derrotas.count() - mandante_empates.count()
visitante_derrotas = visitante_derrotas.count() - visitante_empates.count()

dados_tabela = {"Dados": ["Vitórias Mandante", "Vitórias Visitante", "Empates Mandante", "Empates Visitante", "Mandante Derrotas", "Visitante Derrotas"],
        "Número": [mandante_vitorias["Data"].count(), visitante_vitorias["Data"].count(), mandante_empates["Data"].count(), visitante_empates["Data"].count(), 
        mandante_derrotas["Data"], visitante_derrotas["Data"]]}
df_tabela = pd.DataFrame(dados_tabela)

x = np.arange(6)
plt.bar(x, height=[df_tabela["Número"][0], df_tabela["Número"][1], df_tabela["Número"][2], df_tabela["Número"][3], df_tabela["Número"][4], df_tabela["Número"][5]])
plt.xticks(x, ["Vitórias\nMandante", "Vitórias\nVisitante", "Empates\nMandante", "Empates\nVisitante", "Derrotas\nMandante", "Derrotas\nVisitante"])
plt.title(f"Campanha de {ano_input} do {time} no Brasileirão")

plt.show()
