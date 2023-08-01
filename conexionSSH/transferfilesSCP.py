#Con paramiko podemos hacer transferencias de archivos por el protocolo SFTP
import scp
import time
import paramiko
from getpass import getpass

'''------------------------CONEXION POR SSH - Transferencia SCP--------------------------------'''
HOST = '20.127.146.152'
USER = 'azureuser'
if __name__ == '__main__':

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Se indica a paramiko conexion con credenciales propias ssh o pass -> evita el knownhosts

        password = 'Azurepassword1#'#getpass('Ingrese su contraseña: ')
        client.connect(HOST, username=USER, password=password)

        scp_client = scp.SCPClient(client.get_transport())

        #enviar un archivo
        scp_client.put('conexionSSH/README.md', #local_path
                       'folder_rpa/README2.md' #remote_path
                       )
        
        scp_client.get('folder_rpa/README2.md', #remote_path
                        'conexionSSH/README3.md') #local_path

        scp_client.close()
        client.close()

    except paramiko.SSHException as e:
        print('Autenticacion fallida')
