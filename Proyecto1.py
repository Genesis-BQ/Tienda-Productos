import os
tamaño = 3
productos = []
class ventas:
    #Configuración de la clase
    def __init__(self):
        self.nombre = ""
        self.precio = ""
        self.cantidad = ""
        self.codigo = ""
        self.color = ""

    #Creación de metodos
    def getNombre(self):
        return self.nombre
    def getprecio(self):
        return self.precio
    def getcantidad(self):
        return self.cantidad
    def getCodigo(self):
        return self.codigo
    def getcolor(self):
        return self.color

    #metodo para calcular la compra de un producto    
    def mostrarVenta(self):
        print("\nCodigo: "+self.getCodigo()+"\nNombre: "+self.getNombre()+"\nColor: "+self.getcolor()+"\nPrecio: "+str(self.getprecio())+"\nCantidad: "+str(self.getcantidad())+"\nTotal a pagar: "+str(int(self.getcantidad())*int(self.getprecio())))

    #Metodod para agregar un producto
    def registrar(self):
        while True:
            self.codigo=input("Ingrese el codigo del producto: ")
            self.nombre=input("Por favor ingrese el nombre del producto: ")
            self.color = input("Ingrese colores disponibles:")
            self.cantidad= input("Por favor ingrese cantidad: ")
            self.precio=input("Por favor ingrese el precio del producto: ")
            op = input("Desea agregar otro producto (s/n)")
            if op.lower()=="n":
                break
        

    #Metodo de retiro del producto
    def retiro(self):
        self.codigo=input("Ingrese el codigo del producto: ")
        self.nombre=input("Por favor ingrese el nombre del producto: ")
        self.color = input("Ingrese colores disponibles:")
        self.cantidad= input("Por favor ingrese cantidad: ")
        self.precio=input("Por favor ingrese el precio del producto: ")

    #Configuracion del archivo
    def guardar(self):
        if not os.path.exists('SHEIN.txt'):
            archivo= open('SHEIN.txt','w')
            archivo.write(f"{self.codigo};{self.nombre};{self.color};{self.cantidad};{self.precio}\n")
        else:
            archivo= open('SHEIN.txt','a')
            archivo.write(f"{self.codigo};{self.nombre};{self.color};{self.cantidad};{self.precio}\n")
        archivo.close()

    #Consular en el archivo
    def consultar(self,codigo):
        archivo= open('SHEIN.txt', 'r')
        Listaproductos = archivo.readlines()
        archivo.close()
        for p in Listaproductos:
            producto = p.split(";")
            if codigo == producto[0]:
                print(f"{producto[0]} {producto[1]} {producto[2]} {producto[3]} {producto[4]}")
                break
    
    #Modificar en el archivo
    def modificar(self,codigo,nuevovalor,posicion):
        cont = 1
        archivo= open('SHEIN.txt', 'r')
        Listaproductos = archivo.readlines()
        archivo.close()
        archivo = open('SHEIN.txt','a')
        for p in Listaproductos:
            producto = p.split(";")
            if codigo == producto[0]:
                producto[posicion] = nuevovalor
                self.Eliminar(cont)
                break
            cont+=1
        archivo.close()
        archivo = open('SHEIN.txt','a')
        archivo.write(f"{producto[0]};{producto[1]};{producto[2]};{producto[3]};{producto[4]}\n")
        archivo.close()   

    
    #Eliminar un producto
    def Eliminar(self,posicion):
        archivo = open('SHEIN.txt','r')
        productos = archivo.readlines()
        archivo.close()
        archivo= open('SHEIN.txt','w')
        producto = productos[posicion-1]
        productos.remove(producto)
        for p in productos:
            if p.strip() == "":
                continue
            else :
                archivo.write(p)
        archivo.close()    
    #Metedo lectura de producto
    def leerProducto(self):
        try:
            cont=1
            arch = open('SHEIN.txt', "r")
            x=arch.readline()
            print("------------------------------------------------------------------------------")
            while x:
                if x.strip() == "":
                    break
                print(f"{cont}.", end=" ")
                palabras = x.split(";")
                for p in palabras:
                    if p != palabras[4]:
                        print(f"{p}", end="\t")
                    else:
                        print(f"{p}")
                x = arch.readline()
                cont+=1
            print("------------------------------------------------------------------------------")
        except FileNotFoundError:
            print()
            print("no hay productos registrados aún")
#Sobre Carga de operadores de los precios
    def _lt_(self,otro):
        return self.precio < otro.precio
    
    def __eq__(self,otro):
        return self.precio == otro.precio
    
    def _gt_(sefl,otro):
        return sefl.precio > otro.precio
def main():
    #Configuración del menu
    salir = False
    clase = ventas()
    os.system("cls")
    while not salir:
        print("-------------------------------SHEIN--------------------------------------")
        print ("Bienvenidos SHEIN")
        print ("1. Ingresar nuevo Producto")
        print ("2. Lista de Producto")
        print ("3. Consulta de producto ")
        print ("4. Modifición de producto ")
        print ("5. Retiro de producto ")
        print ("6. Eliminación de producto ")
        print ("7. salir del programa")
        print("-------------------------------SHEIN--------------------------------------")
        opc=int(input("Seleccione una opcion: "))
        if opc==1:
            print("-------------------------------SHEIN--------------------------------------")
            print("Regristro de productos")
            clase.registrar()
            clase.guardar()
            print("Los datos registrados con éxito")
            print("-------------------------------SHEIN--------------------------------------")
        elif opc==2:
            print("-------------------------------SHEIN--------------------------------------")
            print("Lista de productos")
            clase.leerProducto()
            print("Gracias por ver los productos en SEHIN.")
            print("-------------------------------SHEIN--------------------------------------")
        elif opc==3:
            print("-------------------------------SHEIN--------------------------------------")
            print("Consula de productos")
            codigo = input("Digite el codigo: ")
            clase.consultar(codigo)
            print("La consulta se realizo con exito")
            print("-------------------------------SHEIN--------------------------------------")
        elif opc==4:
            print("-------------------------------SHEIN--------------------------------------")
            print("Modificación de productos")
            while True:
                    continuar= True
                    try:
                        print("Menu de cambios")
                        print("1. Modificar Nombre del producto")
                        print("2. Modificar color")
                        print("3. Modificar cantidad")
                        print("4. Modificar precio")
                        print("5. salir")
                        dec= int(input("Digite el numero de la opcion: "))
                        match dec:
                            case 1:
                                clase.leerProducto()
                                while continuar == True:
                                    print("Modicar Nombre del Producto")
                                    codigo = input("digite el codigo del producto: ")
                                    nValor= input("Digite el nuevo valor: ")
                                    seguro = input("esta seguro? (s/n): ")
                                    if seguro.lower() == "s":
                                        clase.modificar(codigo,nValor,1)
                                        continuar = False
                            case 2:
                                clase.leerProducto()
                                while continuar == True:
                                    print("Modificar color")
                                    codigo = input("digite el codigo del producto: ")
                                    nValor= input("Digite el nuevo valor: ")
                                    seguro = input("esta seguro? (s/n): ")
                                    if seguro.lower() == "s":
                                        clase.modificar(codigo,nValor,2)
                                        continuar=False
                            case 3:
                                clase.leerProducto()
                                while continuar == True:
                                    print("Modificar cantidad")
                                    codigo = input("digite el codigo del producto: ")
                                    nValor= input("Digite el nuevo valor: ")
                                    seguro = input("esta seguro? (s/n): ")
                                    if seguro.lower() == "s":
                                        clase.modificar(codigo,nValor,3)
                                        continuar=False
                            case 4:
                                clase.leerProducto()
                                while continuar == True:
                                    print("Modificar precio")
                                    codigo = input("digite el codigo del producto: ")
                                    nValor= input("Digite el nuevo valor: ")
                                    seguro = input("esta seguro? (s/n): ")
                                    if seguro.lower() == "s":
                                        clase.modificar(codigo,nValor,4)
                                        continuar=False
                            case 5:
                                os.system("clear")
                                break
                    except ValueError:
                        print()
                        print("Error al modificar")
                        print()
            print("La modificación se realizo con exito.")
            print("-------------------------------SHEIN--------------------------------------")  
        elif opc==5:
            print("-------------------------------SHEIN--------------------------------------")
            print("Retiro de productos")
            clase.guardar()
            print("El pedido se realizado con éxito")
            print("Gracias por comprar en SHEIN, esperamos que hayas disfrutado tu compra.")
            print("-------------------------------SHEIN--------------------------------------")  
        elif opc==6:
            print("-------------------------------SHEIN--------------------------------------")
            print("Eliminación de productos")
            clase.leerProducto()
            posicion = int(input("Digite la posicion a eliminar: "))
            clase.Eliminar(posicion)
            print("El producto se elimino con éxito")
            print("-------------------------------SHEIN--------------------------------------")            
        elif opc==7:
            salir = True
        else:
            print("Opcion invalida")
    print("Saliendo del programa")
main()