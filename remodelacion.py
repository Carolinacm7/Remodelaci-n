"""  Jairo va al banco a pedir unprestamos, el necesita cincuenta millones para reformar la casa
 ($50.000.000) en el banco le ofrecen una tasa del 0,80% mensual a cuarenta y ocho meses (48).
 
 1. realiza un programa que permita saber cuál es la cuota a pagar cada mes.
 2. realiza la proyección de cuota saldo mensual.
 3. Muestra la proyección mensual de Fecha, cuotaNo., Capital, Interes, Total_cuota,
  y por último Saldo adeudado.
 
 Tip 1: el credito es a cuota fija mensual.
 Tip 2: Formula para sacar la cuota mensual
        Cuota = (Monto x (TEM x (1 + TEM) ^ n)) / ((1 + TEM) ^ n) - 1)
		siendo: Monto (valor a ser prestado), n (numero de meses), TEM (Tasa Efectiva Mensual)
 """
 #definicion de constantes 

from datetime import date
from dateutil.relativedelta import relativedelta

Tem=0.008
monto=50000000
n=48
#



capital = monto / n
cuotamensual = float((monto*(Tem*(1+Tem)**n))/(((1+Tem)**n)-1))
interes = cuotamensual - capital

saldo=cuotamensual*n

hoy = date.today()


print(("Fecha        cuotaNo.       Capital      Interes    Total_cuota     Saldo adeudado"))
for numero_cuota in range(1, n+1):
    ###    
    saldo=saldo-cuotamensual
    if saldo <= 0:
        saldo = 0

    fecha = hoy + relativedelta(months=+numero_cuota)
    
    print(fecha,"    ",round(numero_cuota,2),"       ",round(capital,2)," ",round( interes,2) ," ",round(cuotamensual,2),"     ",round(saldo,2))


    



