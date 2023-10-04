import pandas as pd

# Especifica el nombre del archivo Excel y la hoja que deseas convertir
nombre_archivo_excel = r'C:\Users\tolis\OneDrive\Documentos\python\pythonTime\Leer_hojas_excel\GAW_Rutas_Simuladas.xlsx'
nombre_hoja_excel = 'Sftp'

# Lee la hoja del archivo Excel en un DataFrame
dataframe = pd.read_excel(nombre_archivo_excel, sheet_name=nombre_hoja_excel)

# Especifica el nombre del archivo CSV de salida
nombre_archivo_csv = r'C:\Users\tolis\OneDrive\Documentos\python\pythonTime\Leer_hojas_excel\archivo_csv.csv'

# Guarda el DataFrame como un archivo CSV
dataframe.to_csv(nombre_archivo_csv, index=False, sep = '|')

print(f'Se ha convertido la hoja "{nombre_hoja_excel}" del archivo Excel a "{nombre_archivo_csv}"')
