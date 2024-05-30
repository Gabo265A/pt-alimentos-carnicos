import pandas as pd

def main():
    input_cols_clientes = [1,2]
    input_cols_compras = [2,6]
    clients_bill = {} # Diccionario para almacenar los gastos de los clientes

    df_clientes = obtener_excel('Clientes', input_cols_clientes) # Se lee el archivo de Excel con la hoja de clientes
    df_compras = obtener_excel('Compras', input_cols_compras) # Se lee el archivo de Excel con la hoja de compras

    clients_name = obtener_datos_clientes("Nombre", df_clientes) # Se obtienen los nombres de los clientes
    clients_id = obtener_datos_clientes("Cliente_Id", df_clientes) # Se obtienen los IDs de los clientes

    obtener_gastos_por_cliente(clients_id, clients_bill, df_compras) # Se obtienen los gastos de cada cliente

    mostrar_gastos(clients_bill, clients_name, clients_id) # Se obtienen los gastos de cada cliente

def obtener_excel(sheet_name, input_cols):
    return pd.read_excel('./data/alimentos cárnicos - data.xlsx', sheet_name=sheet_name, header=2, usecols=input_cols) # Leer el archivo de Excel con las columnas especificadas

def mostrar_gastos(clients_bill, clients_name, clients_id):
    print("\n--- Productos por cliente ---\n") # Se imprime la información de los productos por cliente

    for client in clients_bill: # Se recorren los productos de los clientes
        print(f"Los gastos del cliente {clients_name[clients_id.index(client)]} identificado/a con el ID {int(client)} es ${'{:,.2f}'.format(clients_bill[client])}") # Se imprime el producto más comprado por cada cliente, junto con su nombre e ID

    input("\nPresione Enter para continuar...")

def obtener_datos_clientes(sheet_name, df):
    return [value for value in df[sheet_name]] # Retornar los valores de las columnas del dataframe

def obtener_gastos_por_cliente(clients_id, clients_bill, df):

    bills_aux = 0 # Variable auxiliar para almacenar los gastos de cada cliente

    for id in clients_id: # Se recorren los IDs de los clientes
        client = 0 # Variable para recorrer los gastos de cada cliente
        obj_bill_aux = df[df["Cliente_Id"] == id]["Total"].reset_index(drop=True) # Se obtiene la cantidad de gastos de cada cliente
        for total in obj_bill_aux: # Se recorren los gastos de cada cliente
            bills_aux += total # Se suman los gastos de cada cliente
        clients_bill[id] = bills_aux
        client += 1
        bills_aux = 0
