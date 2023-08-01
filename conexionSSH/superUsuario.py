import time
import paramiko
from getpass import getpass

'''------------------------CONEXION POR SSH--------------------------------'''
HOST = '20.127.146.152'
USER = 'azureuser'
if __name__ == '__main__':

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Se indica a paramiko conexion con credenciales propias ssh o pass -> evita el knownhosts

        password = getpass('Ingrese su contraseña: ')
        client.connect(HOST, username=USER, password=password)

        session = client.get_transport().open_session()
        if session.active:

            #----ultimo video ----
            session.set_combine_stderr(True) #Recibir mensaje de error/exito en un mismo string
            session.get_pty() #Peticion para una pseudoterminal

            session.exec_command('sudo ls -la')

            stdin = session.makefile('wb')
            stdout = session.makefile('rb')

            stdin.write(password + '\n' )

            result = stdout.read().decode()

            print(result)

        client.close()

    except paramiko.SSHException as e:
        print('Autenticacion fallida')
