import pandas as pd

input_cols_clientes = [1,2]
input_cols_compras = [2,6]

df_clientes = pd.read_excel('../data/alimentos cárnicos - data.xlsx', sheet_name='Clientes', header=2, usecols=input_cols_clientes) # Se lee el archivo de Excel con la hoja de clientes
df_compras = pd.read_excel('../data/alimentos cárnicos - data.xlsx', sheet_name='Compras', header=2, usecols=input_cols_compras) # Se lee el archivo de Excel con la hoja de compras

clients_name = [name for name in df_clientes["Nombre"]] # Se obtienen los nombres de los clientes
clients_id = [id for id in df_clientes["Cliente_Id"]] # Se obtienen los IDs de los clientes
clients_bill = {} # Diccionario para almacenar los gastos de los clientes
bills_aux = 0 # Variable auxiliar para almacenar los gastos de cada cliente

for id in clients_id: # Se recorren los IDs de los clientes
    client = 0 # Variable para recorrer los gastos de cada cliente
    obj_bill_aux = df_compras[df_compras["Cliente_Id"] == id]["Total"].reset_index(drop=True) # Se obtiene la cantidad de gastos de cada cliente
    for total in obj_bill_aux: # Se recorren los gastos de cada cliente
        bills_aux += total # Se suman los gastos de cada cliente
    clients_bill[id] = bills_aux
    client += 1
    bills_aux = 0

print("\n--- Productos por cliente ---\n") # Se imprime la información de los productos por cliente

for client in clients_bill: # Se recorren los productos de los clientes
    print(f"Los gastos del cliente {clients_name[clients_id.index(client)]} identificado/a con {int(client)} es ${'{:,.2f}'.format(clients_bill[client])}") # Se imprime el producto más comprado por cada cliente, junto con su nombre e ID

print("\n--- Fin del programa ---\n")