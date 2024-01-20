from weasyprint import HTML

def convertir_html_a_pdf(html_file, pdf_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    HTML(string=html_content).write_pdf(pdf_file)

    print(f'Se ha generado el archivo PDF en: {pdf_file}')

# Nombre del archivo HTML de entrada (en la misma carpeta que el script)
archivo_html = 'file.html'

# Nombre del archivo PDF de salida (también en la misma carpeta)
archivo_pdf = 'salida.pdf'

# Llama a la función para convertir HTML a PDF
convertir_html_a_pdf(archivo_html, archivo_pdf)
