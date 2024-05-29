import pandas as pd
import datetime as dt

input_cols = [1,2,4] # Columna client_id, nombre y fecha registro
current_date = dt.datetime.now().date() # Fecha actual

df = pd.read_excel('../data/alimentos cárnicos - data.xlsx', sheet_name='Clientes', header=2, usecols=input_cols) # Se lee el archivo de Excel

dates = pd.to_datetime(df["Fecha_registro"], format='%d/%m/%Y', errors='coerce').dropna().sort_values(ascending=True) # Se convierten las fechas a formato datetime y se eliminan los valores nulos

client = 0
clients_name = [name for name in df["Nombre"]] # Se obtienen los nombres de los clientes
clienst_id = [id for id in df["Cliente_Id"]] # Se obtienen los IDs de los clientes
new_clients = [] # Lista para almacenar los clientes nuevos
old_clients = [] # Lista para almacenar los clientes antiguos

for date in dates:
    if current_date - date.date() < dt.timedelta(days=30): # Se compara la fecha actual con la fecha de registro
        new_clients.append(f"Cliente {clients_name[client]} identificado/a con {int(clienst_id[client])} se registró hace menos de 30 días.") # Si la diferencia es menor a 30 días, se añade a la lista de clientes nuevos
    else:
        old_clients.append(f"Cliente {clients_name[client]} identificado/a con {int(clienst_id[client])} se registró hace más de 30 días.") # Si la diferencia es mayor a 30 días, se añade a la lista de clientes antiguos
    client += 1

print("\n--- Clientes nuevos ---\n") # Se imprime la información de clientes nuevos
for client in new_clients:
    print(client)

print("\n--- Clientes antiguos ---\n") # Se imprime la información de clientes antiguos
for client in old_clients:
    print(client)

print("\n--- Fin del programa ---\n")