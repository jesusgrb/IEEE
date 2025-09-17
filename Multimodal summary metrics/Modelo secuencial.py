# -*- coding: utf-8 -*-
"""
Created on Tue May 20 13:54:49 2025

@author: demia
"""

# -*- coding: utf-8 -*-
"""
Modelo secuencial para predecir valores continuos basados en variables categóricas
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, InputLayer
import matplotlib.pyplot as plt
import os

# Configuración de matplotlib - usando 'Agg' para evitar problemas de interfaz
# Esto evita la necesidad de un backend interactivo que podría causar congelamiento
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo

# 1. Función para cargar los datos
def cargar_datos(ruta_excel=None):
    """Carga datos desde un archivo Excel."""
    if ruta_excel is None or not os.path.exists(ruta_excel):
        try:
            from tkinter import Tk, filedialog
            root = Tk()
            root.withdraw()
            print('Selecciona tu archivo Excel:')
            ruta_excel = filedialog.askopenfilename(
                filetypes=[('Excel files', '*.xlsx *.xls')]
            )
            if not ruta_excel:
                raise FileNotFoundError('No se seleccionó ningún archivo.')
        except Exception as e:
            print(f"Error al abrir diálogo: {e}")
            ruta_excel = input("Introduce la ruta completa del archivo Excel: ")
    
    try:
        df = pd.read_excel(
            ruta_excel,
            sheet_name='Hoja1',
            engine='openpyxl'
        )
        # Limpia nombres de columnas
        df.columns = df.columns.str.strip()
        print("Archivo cargado:", ruta_excel)
        print("Columnas disponibles:", df.columns.tolist())
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

# 2. Función para preparar datos
def preparar_datos(df):
    """Prepara características y variable objetivo."""
    # Definir la variable objetivo como el promedio de las tres mediciones
    df['Picos'] = df[['Terror', 'Destreza', 'Workout']].mean(axis=1)
    y = df['Picos'].values
    
    # Características de entrada
    X = df[['Terror', 'Destreza', 'Workout']].values
    
    # Escalado de características
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # División en entrenamiento/validación
    X_train, X_val, y_train, y_val, idx_train, idx_val = train_test_split(
        X_scaled, y, df.index, test_size=0.3, random_state=42
    )
    
    print("Usuarios en validación:", df.loc[idx_val, 'Respondent Name'].tolist())
    
    return X_train, X_val, y_train, y_val, idx_train, idx_val, scaler

# 3. Función para construir el modelo
def build_sequential_model(input_dim):
    """Construye un modelo secuencial para regresión."""
    model = Sequential([
        InputLayer(input_shape=(input_dim,)),
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1, activation='linear')
    ])
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss='mse',
        metrics=['mae']
    )
    return model

# 4. Función para entrenar el modelo
def entrenar_modelo(model, X_train, y_train, X_val, y_val, epochs=1000, batch_size=16):
    """Entrena el modelo y devuelve el historial."""
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        verbose=1
    )
    return history

# 5. Función para guardar gráficos en archivos
def guardar_graficos(history, y_val, y_pred):
    """Guarda los gráficos como archivos PNG."""
    # Curva de pérdida
    plt.figure(figsize=(10, 6))
    plt.plot(history.history['loss'], label='train_loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.title('Curva de pérdida (MSE)')
    plt.xlabel('Época')
    plt.ylabel('Loss')
    plt.legend()
    plt.tight_layout()
    plt.savefig('curva_perdida.png')
    plt.close()
    
    # Curva de MAE
    plt.figure(figsize=(10, 6))
    plt.plot(history.history['mae'], label='train_mae')
    plt.plot(history.history['val_mae'], label='val_mae')
    plt.title('Curva de MAE')
    plt.xlabel('Época')
    plt.ylabel('MAE')
    plt.legend()
    plt.tight_layout()
    plt.savefig('curva_mae.png')
    plt.close()
    
    # Real vs Predicho
    plt.figure(figsize=(10, 6))
    plt.scatter(y_val, y_pred, alpha=0.7)
    plt.plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'r--')
    plt.title('Real vs Predicho: GSR (Picos)')
    plt.xlabel('Valor real de Picos')
    plt.ylabel('Predicción de Picos')
    plt.tight_layout()
    plt.savefig('real_vs_predicho.png')
    plt.close()
    
    # Distribución
    plt.figure(figsize=(10, 6))
    plt.hist(y_val, bins=15, alpha=0.6, label='Reales')
    plt.hist(y_pred, bins=15, alpha=0.6, label='Predichos')
    plt.title('Distribución de Picos (Reales vs Predichos)')
    plt.xlabel('Picos')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.tight_layout()
    plt.savefig('distribucion_picos.png')
    plt.close()
    
    print("Gráficos guardados como archivos PNG en el directorio actual")

# Función principal
def main():
    # Cargar datos
    try:
        excel_path = 'Multimodal summary metrics (Excel).xlsx'
        df = cargar_datos(excel_path)
        if df is None:
            return
        
        # Preparar datos
        X_train, X_val, y_train, y_val, idx_train, idx_val, scaler = preparar_datos(df)
        
        # Construir modelo
        model = build_sequential_model(X_train.shape[1])
        model.summary()
        
        # Entrenar modelo
        history = entrenar_modelo(model, X_train, y_train, X_val, y_val)
        
        # Evaluar en validación
        test_loss, test_mae = model.evaluate(X_val, y_val, verbose=0)
        print(f"MSE en validación: {test_loss:.4f}")
        print(f"MAE en validación: {test_mae:.4f}")
        
        # Guardar modelo
        model.save('modelo_categorias_continuo.h5')
        print("Modelo guardado como 'modelo_categorias_continuo.h5'")
        
        # Predicciones
        y_pred = model.predict(X_val).flatten()
        
        # Guardar gráficos
        guardar_graficos(history, y_val, y_pred)
        
        # Estadísticas descriptivas y CSV de predicciones
        desc = pd.DataFrame({
            'User': df.loc[idx_val, 'Respondent Name'].values, 
            'Real': y_val, 
            'Predicho': y_pred
        })
        print("\nEstadísticas descriptivas:")
        print(desc.describe())
        desc.to_csv('predicciones_picos.csv', index=False)
        print("Predicciones guardadas en 'predicciones_picos.csv'")
        
        # Adicionalmente, guardamos un resumen del modelo y datos
        with open('resumen_modelo.txt', 'w') as f:
            f.write(f"Número de muestras: {len(df)}\n")
            f.write(f"Muestras en entrenamiento: {len(X_train)}\n")
            f.write(f"Muestras en validación: {len(X_val)}\n")
            f.write(f"MSE en validación: {test_loss:.4f}\n")
            f.write(f"MAE en validación: {test_mae:.4f}\n")
        
        print("Resumen del modelo guardado en 'resumen_modelo.txt'")
        
    except Exception as e:
        print(f"Error en la ejecución: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()