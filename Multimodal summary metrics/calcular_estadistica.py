# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 19:45:55 2025

@author: demia
"""

import pandas as pd

# 1. Carga el CSV
df = pd.read_csv('datos_originales.csv')

# 2. Selecciona solo las columnas numéricas de picos
# (aquí asumimos que las columnas relevantes se llaman exactamente 'Terror', 'Destreza', 'Workout')
columnas = ['Terror', 'Destreza', 'Workout']

# 3. Calcula estadística descriptiva básica
resumen = df[columnas].agg(['mean', 'median', 'std', 'min', 'max']).T
resumen['rango'] = resumen['max'] - resumen['min']
resumen = resumen.rename(columns={
    'mean': 'Media',
    'median': 'Mediana',
    'std': 'DesvStd',
    'min': 'Mínimo',
    'max': 'Máximo'
})

# 4. Guarda la tabla en un CSV para incorporarlo a LaTeX si lo deseas
resumen.to_csv('estadistica_descriptiva.csv')

print(resumen)
