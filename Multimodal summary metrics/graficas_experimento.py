# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 20:06:16 2025

@author: demia
"""

import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
df = pd.read_csv('datos_originales.csv')

# Tomamos solo las columnas numéricas de interés
df_picos = df[['Terror', 'Destreza', 'Workout']]

# 1) Boxplot
plt.figure(figsize=(6,4))
df_picos.boxplot()
plt.title('Distribución de picos SCR por género')
plt.ylabel('Picos SCR (Peak Count)')
plt.savefig('boxplot_picos_scr.png', dpi=300)
plt.close()

# 2) Barplot de medias ± desvest
means = df_picos.mean()
stds  = df_picos.std()
plt.figure(figsize=(6,4))
plt.bar(means.index, means.values, yerr=stds.values, capsize=5)
plt.title('Media ± Desviación estándar de picos SCR por género')
plt.ylabel('Picos SCR (µS)')
plt.savefig('barplot_media_scr.png', dpi=300)
plt.close()

print("Gráficas guardadas: 'boxplot_picos_scr.png' y 'barplot_media_scr.png'")
