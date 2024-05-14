class persona ():   # se crea la clase persona

    def __init__(self, nombre, apellido):  # funcion init con los atributos de la clase persona
        self.nombre= nombre 
        self.apellido= apellido
    

class Cliente(persona): # clase hija se pasa el parametro persona para saber que se va a heredar atributos
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):   # funcion con los atributos de cliente 
        super().__init__(nombre, apellido)  # llama los atributos de la clase persona que esta heredando 
        self.numero_cuenta= numero_cuenta
        self.balance = balance

    def __str__(self) :  #  funcion muestra los datos del cliente 
        return f"cliente: {self.nombre} {self.apellido} con cuenta {self.numero_cuenta} y saldo {self.balance}" #imprime en pantalla
    
    def depositar(self, monto_deposito):  #funcion para depositar
        self.balance += monto_deposito    # valos que se tienemas el agregado
        print(f"deposito aceptado tu saldo es{self.balance} ")  #se muestra el valor actual 
    
    def retirar (self, monto_retiro):  #funcion para retirar 
        
        if  self.balance >= monto_retiro:  # condicion 
            self.balance -= monto_retiro # resta el retiro del balance 
            print(f"retiraste te {self.balance} quedan ")  # imprime lo que queda
           
        else :  # si el balance es menor no se puede retirar
             print("no tienes saldo ")
            

def crear_cliente ():   #funcion para crear el cliente 
    nombre_cl = input("agrega tu nombre")
    apellido_cl = input("agrega apellido")
    numero_cuenta = input("agrega la cuenta")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta )# pasamos las variables creadas al parametro de la clase cliente 
    return cliente
    
def inicio():  # iniciamos el programa
    mi_cliente = crear_cliente()   #pasamos la funcion crear_cliente a la variable mi_cliente
    print(mi_cliente) # llamamos la funcionpara que se cree el cliente 
    opcion = 0

    while opcion != "s" or "S": #mientras que la opcion marcada sea diferente a s o S se va a ejecutar el codigo
        print(" elije uan opcion: depositar (d) , retirar (r), o salir (s)")
        opcion = input()

        if opcion == "d" or "D":
            monto_dep= int(input("deposito"))
            mi_cliente.depositar(monto_dep)
        elif opcion == "r" or "R":
             monto_ret= int(input("retirar"))
             mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    print("gracias ")
        

inicio()              


    

