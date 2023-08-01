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
        '''
        #Forma Basica       
        stdin, stdout, stderr = client.exec_command('cd /home') #exec_command devuelve 3 objetos asignables a variables: standard input, output, error 
        time.sleep(1)
        result = stdout.read().decode() #leer la salida con read, dejarla bonita condecode
        print(result)
        client.close()
'''        

        #Canales -> Diseñados para ejecutar solo un comando, despues se cerrara de forma automatica
        session = client.get_transport().open_session()
        if session.active:
            session.exec_command('ls -la')
            result = session.recv(1024).decode()#Argumento es la cantidad de bytes que queremos ver
            print(result)
        client.close()

    except paramiko.SSHException as e:
        print('Autenticacion fallida')
