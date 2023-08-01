#Con paramiko podemos hacer transferencias de archivos por el protocolo SFTP

import time
import paramiko
from getpass import getpass

'''------------------------CONEXION POR SSH - Transferencia SFTP--------------------------------'''
HOST = '20.127.146.152'
USER = 'azureuser'
if __name__ == '__main__':

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Se indica a paramiko conexion con credenciales propias ssh o pass -> evita el knownhosts

        password = getpass('Ingrese su contraseña: ')
        client.connect(HOST, username=USER, password=password)

        sftp_client = client.open_sftp() #retorna un objeto sftp para enviar/recibir archivos

        '''Enviar archivos
        sftp_client.put(
            'conexionSSh/README.md', #localPath
            'folder_rpa/README.md') #remotePath
        '''

        #Recibir archivos
        sftp_client.get(
            'folder_rpa/Azure.xml', #Remotepath
            'Azure.xml' #localPath
        )

        sftp_client.close()
        client.close()

    except paramiko.SSHException as e:
        print('Autenticacion fallida')
