import snap7
from snap7.util import*

#Configuração do SNAP7 e tenta a conexão com CLP. IP, Rack, Slot
client = snap7.client.Client()
try:
    client.connect('192.168.0.200', 0, 1)
except:
    print ("Falha de conexão")
   

#Função de leitura e escrita. Carrega os endereços da DB, incrementa 1 e depois salva no mesmo endereço
def leitura_escrita():
    comm=client.get_connected()
    if comm:
        data = client.db_read(4, 0, 20)
        print(get_word(data,0))
        print(get_word(data,2))
        print(get_word(data,4))
        print(get_word(data,6))
        print(get_word(data,8))
        print(get_word(data,10))
        print(get_word(data,12))
        print(get_word(data,14))
        print(get_word(data,16))
        print(get_word(data,18))
   
        dataW = bytearray(20)
        snap7.util.set_int(dataW, 0, get_word(data,0)+1)
        snap7.util.set_int(dataW, 2, get_word(data,2)+1)
        snap7.util.set_int(dataW, 4, get_word(data,4)+1)
        snap7.util.set_int(dataW, 6, get_word(data,6)+1)
        snap7.util.set_int(dataW, 8, get_word(data,8)+1)
        snap7.util.set_int(dataW, 10, get_word(data,10)+1)
        snap7.util.set_int(dataW, 12, get_word(data,12)+1)
        snap7.util.set_int(dataW, 14, get_word(data,14)+1)
        snap7.util.set_int(dataW, 16, get_word(data,16)+1)
        snap7.util.set_int(dataW, 18, get_word(data,18)+1)
        client.db_write(4, 0, dataW)   
    else:
        print("erro na conexão")


#Função ciclíca do Script, executa a cada 1 segundo
try:
    while True:  
        leitura_escrita()
        time.sleep(1)
       
except:
    print ("Falha de Leitura")
   
    
