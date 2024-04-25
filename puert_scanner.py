import socket #para manejar la red impor socket (socket seria el enlace para la red)

#valiable ip para que el usuario ingrese la ip a escanear
ip = input("ingrese la direccion IP a escanear: ")

#bucle for para escanear los puertos
#el total de puertos son 65535 pero no todos son de uso comun
#buscara el puerto del rango 1 al 65535
for puerto in range(1,65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                                                #(socket.AF_INET) especifica el protocolo IPv4 son las direcciones que se asignan cuando se registra un condominio
                                                                #12 caracteres de en cuatro bloques separados por un "." ej 212.227.142.131
                                                                #(socket.SOCK_STREAM) especifica el protocolo tcp, permite que dos anfitriones(host) se conecten e intercambien flujo de datos
    socket.setdefaulttimeout(5)
    resultado = sock.connect_ex((ip,puerto))#sock.connect_ex sirve para devolver un iindicador de error en lugar de generar una exepcion
    #verifica que el resultado sea 0 o error. 
    if resultado == 0:
        print("Puerto Abierto: " + str(puerto))
        sock.close()#cerramos el socket
        break
    else:
        print("Puerto Cerrado: " + str(puerto))

















