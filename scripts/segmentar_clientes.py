import pandas as pd
import datetime as dt

def main():
    input_cols = [1,2,4] # Columna client_id, nombre y fecha registro
    current_date = dt.datetime.now().date() # Fecha actual
    new_clients = [] # Lista para almacenar los clientes nuevos
    old_clients = [] # Lista para almacenar los clientes antiguos

    df = obtener_excel('Clientes', input_cols) # Se lee el archivo de Excel con la hoja de clientes

    dates = obtener_fechas(df) # Se obtienen las fechas de registro de los clientes

    clients_name = obtener_datos_clientes("Nombre", df) # Se obtienen los nombres de los clientes
    clients_id = obtener_datos_clientes("Cliente_Id", df) # Se obtienen los IDs de los clientes

    verificar_fecha_registro(dates, current_date, clients_name, clients_id, new_clients, old_clients) # Se verifica la fecha de registro de los clientes

    mostar_clientes_nuevos_y_antiguos(new_clients, old_clients) # Se muestran los clientes nuevos y antiguos

def obtener_excel(sheet_name, input_cols):
    return pd.read_excel('./data/alimentos cárnicos - data.xlsx', sheet_name=sheet_name, header=2, usecols=input_cols) # Leer el archivo de Excel con las columnas especificadas

def obtener_fechas(df):
    return pd.to_datetime(df["Fecha_registro"], format='%d/%m/%Y', errors='coerce').dropna().sort_values(ascending=True) # Se convierten las fechas a formato datetime y se eliminan los valores nulos

def obtener_datos_clientes(sheet_name, df):
    return [value for value in df[sheet_name]] # Retornar los valores de las columnas del dataframe

def verificar_fecha_registro(dates, current_date, clients_name, clients_id, new_clients, old_clients):
    client = 0
    for date in dates:
        if current_date - date.date() < dt.timedelta(days=30): # Se compara la fecha actual con la fecha de registro
            new_clients.append(f"Cliente {clients_name[client]} identificado/a con el ID {int(clients_id[client])} se registró hace menos de 30 días.") # Si la diferencia es menor a 30 días, se añade a la lista de clientes nuevos
        else:
            old_clients.append(f"Cliente {clients_name[client]} identificado/a con el ID {int(clients_id[client])} se registró hace más de 30 días.") # Si la diferencia es mayor a 30 días, se añade a la lista de clientes antiguos
        client += 1

def mostar_clientes_nuevos_y_antiguos(new_clients, old_clients):
    print("\n--- Clientes nuevos ---\n") # Se imprime la información de clientes nuevos
    for client in new_clients:
        print(client)

    print("\n--- Clientes antiguos ---\n") # Se imprime la información de clientes antiguos
    for client in old_clients:
        print(client)

    input("\nPresione Enter para continuar...")
