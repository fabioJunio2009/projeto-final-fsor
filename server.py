import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria o objeto socket: socket.AF_INET é pra indicar que a comunicação é em ipv4 e sock_stream indica que o socket será em tcp

# ciclo: socket() -> bind() -> listen() -> accept() -> recv/sendall()

servidor.bind(("127.0.0.1", 5000)) # bind é o que decide o endereço ip e a porta
servidor.listen(5) # servidor pronto para conexões com clientes
cliente, endereco = servidor.accept() # cliente:  o socket retornado por accept(), que representa a conexão aceita.

print("Cliente conectado:", endereco)
print("Socket de escuta:", servidor)
print("Socket da conexão:", cliente)

# listen() prepara o socket para receber conexões; accept() aceita uma delas e entrega um novo socket para a comunicação. São operações diferentes sobre objetos com funções diferentes.

cliente.close()
servidor.close()