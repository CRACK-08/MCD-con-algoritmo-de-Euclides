# INSTRUCCIONES:
# Corregir la implementación del algoritmo de Euclides

# 1.- Damos valores iniciales
print ( "Valores iniciales" )
A  =  270
B  =  192
imprimir ( A )
imprimir ( B )
# 2.- Ciclo del algoritmo
para  i  en el  rango ( 5 ):
  print ( "Iteración"  +  str ( i ))
  R  =  A  %  B
  imprimir ( "R ="  +  str ( R ))

  A  =  B
  B  =  R
  imprimir ( "A ="  +  str ( A ))
  imprimir ( "B ="  +  str ( B ))
# Resultados (asignar el resultado del MCD a la variable M)
print ( "El MCD es ="  +  str ( M ))
