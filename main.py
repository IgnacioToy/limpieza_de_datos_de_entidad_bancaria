# ===================================================================
# ANÁLISIS DE DATOS DE BANCO - TRADUCIDO AL ESPAÑOL
# ===================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lectura del archivo
ruta = 'data_banco.csv'
data = pd.read_csv(ruta)

# Mapeo de columnas
col_trad = {
    'age': 'edad', 'job': 'trabajo', 'marital': 'estado_civil', 'education': 'educacion',
    'default': 'morosidad', 'balance': 'saldo', 'housing': 'vivienda', 'loan': 'prestamo',
    'contact': 'contacto', 'day': 'dia', 'month': 'mes', 'duration': 'duracion',
    'campaign': 'campaña', 'pdays': 'dias_ult_contacto', 'previous': 'contactos_previos',
    'poutcome': 'resultado_previo', 'y': 'resultado'
}

data.rename(columns=col_trad, inplace=True)

# Mapeo de valores categóricos
fil_trad = {
    'trabajo': {
        'management': 'gerencia', 'technician': 'técnico', 'entrepreneur': 'empresario',
        'blue-collar': 'obrero', 'unknown': 'desconocido', 'retired': 'jubilado',
        'admin.': 'administrativo', 'services': 'servicios', 'self-employed': 'autónomo',
        'Management': 'gerencia', 'MANAGEMENT': 'gerencia', 'Self-employed': 'autónomo',
        'SELF-EMPLOYED': 'autónomo', 'Admin.': 'administrativo'
    },
    'estado_civil': {
        'married': 'casado', 'single': 'soltero', 'divorced': 'divorciado', 
        'div.': 'divorciado', 'Married': 'casado', 'Single': 'soltero',
        'Divorced': 'divorciado', 'Div.': 'divorciado'
    },
    'educacion': {
        'tertiary': 'superior', 'secondary': 'secundaria', 'primary': 'primaria', 
        'unknown': 'desconocido', 'sec.': 'secundaria', 'unk': 'desconocido',
        'Secondary': 'secundaria', 'Primary': 'primaria', 'Unknown': 'desconocido',
        'Sec.': 'secundaria', 'Unk': 'desconocido'
    },
    'morosidad': {'no': 'no', 'yes': 'sí', 'No': 'no', 'YES': 'sí'},
    'vivienda': {'no': 'no', 'yes': 'sí', 'No': 'no', 'YES': 'sí'},
    'prestamo': {'no': 'no', 'yes': 'sí', 'No': 'no', 'YES': 'sí'},
    'contacto': {
        'unknown': 'desconocido', 'telephone': 'teléfono', 'phone': 'teléfono',
        'mobile': 'celular', 'cellular': 'celular', 'Unknown': 'desconocido',
        'Telephone': 'teléfono', 'Phone': 'teléfono', 'Mobile': 'celular',
        'Cellular': 'celular'
    },
    'mes': {
        'jan': 'enero', 'feb': 'febrero', 'mar': 'marzo', 'apr': 'abril',
        'may': 'mayo', 'jun': 'junio', 'jul': 'julio', 'aug': 'agosto',
        'sep': 'septiembre', 'oct': 'octubre', 'nov': 'noviembre', 'dec': 'diciembre',
        'JAN': 'enero', 'FEB': 'febrero', 'MAR': 'marzo', 'APR': 'abril',
        'MAY': 'mayo', 'JUN': 'junio', 'JUL': 'julio', 'AUG': 'agosto',
        'SEP': 'septiembre', 'OCT': 'octubre', 'NOV': 'noviembre', 'DEC': 'diciembre'
    },
    'resultado_previo': {
        'unknown': 'desconocido', 'failure': 'fracaso', 'success': 'éxito',
        'other': 'otro', 'unk': 'desconocido', 'Unknown': 'desconocido',
        'Failure': 'fracaso', 'Success': 'éxito', 'Other': 'otro',
        'Unk': 'desconocido', 'UNK': 'desconocido'
    },
    'resultado': {'no': 'no', 'yes': 'sí', 'No': 'no', 'YES': 'sí'}
}

# Aplicar traducción de valores
data = data.replace(fil_trad)

# Información inicial del DataFrame
print(f"Dimensiones del DataFrame: {data.shape}")
print("\nPrimeras filas del DataFrame:")
print(data.head())

# Información general del DataFrame
print("\n=== INFORMACIÓN GENERAL DEL DATAFRAME ===")
data.info()

# Eliminar valores nulos
print(f"\nTamaño antes de eliminar nulos: {data.shape}")
data.dropna(inplace=True)
print(f"Tamaño después de eliminar nulos: {data.shape}")

# Conteo de subniveles en variables categóricas
cols_cat = ['trabajo', 'estado_civil', 'educacion', 'morosidad', 'vivienda',
            'prestamo', 'contacto', 'mes', 'resultado_previo', 'resultado']

print("\n=== CONTEO DE SUBNIVELES ===")
for col in cols_cat:
    print(f'Columna {col}: {data[col].nunique()} subniveles')

# Estadísticas descriptivas
print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(data.describe())

# Lista de columnas numéricas
cols_num = ['edad', 'saldo', 'dia', 'duracion', 'campaña', 
            'dias_ult_contacto', 'contactos_previos']

# Eliminar filas duplicadas
print(f"\nTamaño antes de eliminar duplicados: {data.shape}")
data.drop_duplicates(inplace=True)
print(f"Tamaño después de eliminar duplicados: {data.shape}")

# Generar gráficas individuales para variables numéricas
fig, ax = plt.subplots(nrows=7, ncols=1, figsize=(8, 30))
fig.subplots_adjust(hspace=0.8)

for i, col in enumerate(cols_num):
    sns.boxplot(x=col, data=data, ax=ax[i], color='skyblue')
    ax[i].set_title(f'Distribución de {col}', fontsize=12, pad=20)
    ax[i].set_xlabel('')
    ax[i].tick_params(axis='x', rotation=45)
    ax[i].axvline(data[col].median(), color='red', linestyle='--', linewidth=1.5)
    
plt.suptitle('Análisis de Variables Numéricas', y=1.02, fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('analisis_variables_numericas.png', dpi=300, bbox_inches='tight')
plt.show()

# Eliminar edades mayores a 100 años
print(f"\nTamaño antes de eliminar edades > 100: {data.shape}")
data = data[data['edad'] <= 100]
print(f"Tamaño después de eliminar edades > 100: {data.shape}")

# Eliminar duraciones negativas
print(f"\nTamaño antes de eliminar duraciones < 0: {data.shape}")
data = data[data['duracion'] > 0]
print(f"Tamaño después de eliminar duraciones < 0: {data.shape}")

# Eliminar contactos previos mayores a 100
print(f"\nTamaño antes de eliminar contactos_previos > 100: {data.shape}")
data = data[data['contactos_previos'] <= 100]
print(f"Tamaño después de eliminar contactos_previos > 100: {data.shape}")

# Graficar los subniveles de cada variable categórica (antes de unificar)
cols_cat_es = ['trabajo', 'estado_civil', 'educacion', 'morosidad', 'vivienda',
               'prestamo', 'contacto', 'mes', 'resultado_previo', 'resultado']

fig, ax = plt.subplots(nrows=10, ncols=1, figsize=(12, 35))
fig.subplots_adjust(hspace=1.2)

for i, col in enumerate(cols_cat_es):
    sns.countplot(x=col, data=data, ax=ax[i], palette='viridis')
    ax[i].set_title(f'Distribución de {col} (antes de unificar)', fontsize=14, pad=20)
    ax[i].set_xlabel('')
    ax[i].set_ylabel('Frecuencia', fontsize=12)
    ax[i].tick_params(axis='x', rotation=30)
    
    for p in ax[i].patches:
        ax[i].annotate(f'{int(p.get_height())}', 
                      (p.get_x() + p.get_width() / 2., p.get_height()),
                      ha='center', va='center', 
                      xytext=(0, 5), 
                      textcoords='offset points',
                      fontsize=10)

plt.suptitle('Análisis de Variables Categóricas (antes de unificar)', fontsize=18, y=1.01)
plt.tight_layout()
plt.savefig('analisis_categoricas_antes_unificar.png', dpi=300, bbox_inches='tight')
plt.show()

# Unificar a minúsculas
for column in data.columns:
    if column in cols_cat_es:
        data[column] = data[column].str.lower()

# Generar gráficas después de minúsculas
fig, ax = plt.subplots(nrows=10, ncols=1, figsize=(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(cols_cat_es):
    sns.countplot(x=col, data=data, ax=ax[i])
    ax[i].set_title(f'Distribución de {col} (minúsculas)')
    ax[i].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.savefig('analisis_categoricas_minusculas.png', dpi=300, bbox_inches='tight')
plt.show()

# Unificación de categorías
print("\n=== UNIFICACIÓN DE CATEGORÍAS ===")

# trabajo: unificar admin. y administrativo
print("\nValores únicos antes de unificar 'trabajo':")
print(data['trabajo'].unique())
data['trabajo'] = data['trabajo'].str.replace('admin.', 'administrativo', regex=False)
print("\nValores únicos después de unificar 'trabajo':")
print(data['trabajo'].unique())

# estado_civil: unificar div. y divorciado
print("\nValores únicos antes de unificar 'estado_civil':")
print(data['estado_civil'].unique())
data['estado_civil'] = data['estado_civil'].str.replace('div.', 'divorciado', regex=False)
print("\nValores únicos después de unificar 'estado_civil':")
print(data['estado_civil'].unique())

# educacion: unificar sec. y secundaria, unk y desconocido
print("\nValores únicos antes de unificar 'educacion':")
print(data['educacion'].unique())
data['educacion'] = data['educacion'].str.replace('sec.', 'secundaria', regex=False)
data.loc[data['educacion']=='unk','educacion'] = 'desconocido'
print("\nValores únicos después de unificar 'educacion':")
print(data['educacion'].unique())

# contacto: unificar telephone y phone
print("\nValores únicos antes de unificar 'contacto':")
print(data['contacto'].unique())
data.loc[data['contacto']=='phone','contacto'] = 'teléfono'
data.loc[data['contacto']=='mobile','contacto'] = 'celular'
print("\nValores únicos después de unificar 'contacto':")
print(data['contacto'].unique())

# resultado_previo: unificar unk y desconocido
print("\nValores únicos antes de unificar 'resultado_previo':")
print(data['resultado_previo'].unique())
data.loc[data['resultado_previo']=='unk','resultado_previo']='desconocido'
print("\nValores únicos después de unificar 'resultado_previo':")
print(data['resultado_previo'].unique())

# Guardar el DataFrame limpio
data.to_csv('data_banco_limpio.csv', index=False)
print("\n=== PROCESO COMPLETADO ===")
print(f"Datos limpios guardados en 'data_banco_limpio.csv'")
print(f"Dimensiones finales del DataFrame: {data.shape}")