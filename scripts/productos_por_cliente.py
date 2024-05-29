import pandas as pd

input_cols_clientes = [1,2]
input_cols_compras = [2,3,5]

df_clientes = pd.read_excel('../data/alimentos cárnicos - data.xlsx', sheet_name='Clientes', header=2, usecols=input_cols_clientes) # Se lee el archivo de Excel con la hoja de clientes
df_compras = pd.read_excel('../data/alimentos cárnicos - data.xlsx', sheet_name='Compras', header=2, usecols=input_cols_compras) # Se lee el archivo de Excel con la hoja de compras

clients_name = [name for name in df_clientes["Nombre"]] # Se obtienen los nombres de los clientes
clients_id = [id for id in df_clientes["Cliente_Id"]] # Se obtienen los IDs de los clientes
clients_products = {} # Diccionario para almacenar los productos de los clientes
cant_aux = 0 # Variable auxiliar para almacenar la cantidad de productos

for id in clients_id: # Se recorren los IDs de los clientes
    client = 0 # Variable para recorrer los productos de cada cliente
    obj_cant_aux = df_compras[df_compras["Cliente_Id"] == id]["Cantidad"].reset_index(drop=True) # Se obtiene la cantidad de productos de cada cliente
    for product in df_compras[df_compras["Cliente_Id"] == id]["Producto"]: # Se recorren los productos de cada cliente
        if obj_cant_aux[client] >= cant_aux: # Se compara la cantidad de productos con la cantidad auxiliar, para determinar el producto más comprado. Si el producto actual es mayor o igual al producto anterior, se actualiza la cantidad auxiliar y se almacena el producto
            cant_aux = obj_cant_aux[client]
            clients_products[id] = product
        client += 1
    cant_aux = 0

print("\n--- Productos por cliente ---\n") # Se imprime la información de los productos por cliente

for client in clients_products: # Se recorren los productos de los clientes
    print(f"El producto más comprado por el cliente {clients_name[clients_id.index(client)]} identificado/a con {int(client)} es {clients_products[client]}.") # Se imprime el producto más comprado por cada cliente, junto con su nombre e ID

print("\n--- Fin del programa ---\n")