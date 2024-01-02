"""Extracción de Correos Electrónicos:

Crea una expresión regular que extraiga direcciones de correo electrónico de un texto. Asume que los correos electrónicos tienen el formato usuario@dominio.com."""
import re

regex_correo = re.compile(r'\b[a-z0-9.-:]+@[a-z0-9]+\.[a-z]{2,}\b')

texto_ejemplo = '{     "genero": "M",     "telefonoCelular": "+571123456789",     "ultimaCita": {         "horaCita": "10:00",         "fechaCita": "07-12-2023",         "telefonoCelular": null,         "nombreMedico": "Julia Eugenia Ramirez",         "nombreClinica": "1. Centro Médico Colsanitas Virtual Bogotá",         "nombreEspecialidad": "Medicina General",         "email": "pruea@sanitas.com",         "codigoClinica": "218903",         "codigoEspecialidad": "004",         "codigoMedico": "52040290",         "codigoCita": "626192-494246348",         "estado": "PENDING"     },     "email": "pruea@sanitas.com",     "numeroIdentificacion": "80421503",     "tipoIdentificacion": "C",     "nombre": "Robles Ortega, Jairo Enrique",     "planes": [         {             "codCia": "10",             "codPlan": "32",             "descripcion": "COLSANITAS PLAN DENTAL",             "contUsr": "10326"         },         {             "codCia": "10",             "codPlan": "10",             "descripcion": "INTEGRAL",             "contUsr": "1040107634"         },         {             "codCia": "30",             "codPlan": "10",             "descripcion": "REGIMEN CONTRIBUTIVO",             "contUsr": "54456"         }     ],     "codCia": "10",     "codPlan": "32",     "nombreUnidadAtencion": "LIBRE ELECCION MEDICINA BOGOTA",     "codigoUnidadAtencion": "2725",     "codigoOdontologo": "2615",     "nombreOdontologo": "LIBRE ELECCION ODONTOLOGIA BOGOTA",     "codigoCiudad": "11001",     "esUnidadAtencionPropia": false,     "nroTelefonoUnidadAtencion": null,     "dirUnidadAtencion": null,     "esCronico": false,     "fechaNacimiento": "23-12-1970",     "estado": "HABILITADO" }'

match = re.findall(regex_correo, texto_ejemplo)

conjunto = set(match)
print(conjunto)


for x in conjunto:
    print(x)

