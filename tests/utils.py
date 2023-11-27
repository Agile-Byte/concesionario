import pandas as pd
df_clientes_existente = {
    'nombre': ['Pablo', 'Jorge', 'Pedro'],
    'apellido': ['Garcia', 'Jorge', 'Pedro'],
    'dni': ['12345678A', '55589965G', '24523698F'],
    'presupuesto': [15000, 25000, 100000]
}
df_cliente = {
    'nombre': ['Pablo'],
    'apellido': ['Garcia'],
    'dni': ['12345678A'],
    'presupuesto': [15000]
}
df_no_cliente = {
    'nombre': ['Elena'],
    'apellido': ['Perez'],
    'dni': ['23455678A'],
    'presupuesto': [19000]
}
df_clientes_no_existente = {
    'nombre': ['Alberto', 'Jorge', 'Pedro'],
    'apellido': ['Alberto', 'Jorge', 'Pedro'],
    'dni': ['75698521A', '55589965G', '24523698F'],
    'presupuesto': [15000, 25000, 100000]
}
df_lista_coche = {
    'marca': ['Toyota', 'Audi', 'Renault'],
    'modelo': ['Yaris', 'A4', 'Pedro'],
    'num_puertas': [3, 5, 3],
    'precio': [10000, 77000, 15000]
}
df_albaran = {
    'Producto': ['Tijeras', 'Casco'],
    'Precio': [3, 20],
    'Cantidad': [2, 3]
}
df_albaran_neg = {
    'Producto': ['Tijeras', 'Casco'],
    'Precio': [3, 20],
    'Cantidad': [-5, 3]
}
df_albaran_max = {
    'Producto': ['Tijeras', 'Casco'],
    'Precio': [3, 20],
    'Cantidad': [45, 3]
}
df_stock_productos = {
    'Producto': ['Tijeras', 'Casco', 'Martillo'],
    'Precio': [3, 20, 23],
    'Cantidad': [2, 3, 2],
    'Total': [10, 15, 10],
    'Porcentaje': [0.5, 0.67, 0.20]
}
df_stock_productos_completo = {
    'Producto': ['Tijeras', 'Casco', 'Martillo'],
    'Precio': [3, 20, 23],
    'Cantidad': [10, 15, 10],
    'Total': [10, 15, 10],
    'Porcentaje': [1.0, 1.0, 1.0]
}
df_stock_expected = {
    'Producto': ['Casco', 'Martillo', 'Tijeras'],
    'Precio': [20, 23, 3],
    'Cantidad': [6, 2, 4],
    'Total': [15.0, 10.0, 10.0],
    'Porcentaje': [0.4, 0.2, 0.40]
}
df_promo = {
    'cod_param': ["promo_clientes"],
    'dat_alta': [pd.Timestamp('2000-01-01 00:00:00')],
    'dat_baja': [pd.Timestamp('2040-01-01 00:00:00')],
    'promo': [1],
    'value': [0.35]
}
