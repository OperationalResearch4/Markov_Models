'''
UNIVERSIDAD DE CARABOBO
FACULTAD DE CIENCIAS Y TECNOLOGÍA
DEPARTAMENTO DE MATEMÁTICA
INVESTIGACIÓN DE OPERACIONES IV

ESTUDIANTE: LUIS ALEJANDRO RIVAS MALDONADO
CÉDULA: 15.653.801

Este programa determina la solución óptima del modelo de programación
lineal (problema 19.3-3, capítulo 19, página 868) del libro de texto 
Introducción a la Investigación de Operaciones, Hillier-Lieberman 9na
edición.
'''

import pulp as p

Lp_prob = p.LpProblem('Problem', p.LpMinimize)

# VARIABLES DE DECISIÓN
y01 = p.LpVariable("y01", lowBound = 0)
y02 = p.LpVariable("y02", lowBound = 0)
y11 = p.LpVariable("y11", lowBound = 0)
y12 = p.LpVariable("y12", lowBound = 0)

# FUNCIÓN OBJETIVO
Lp_prob += 14*y01 + 14*y11 + 75*y12

# RESTRICCIONES
Lp_prob += y01 + y02 + y11 + y12 == 1
Lp_prob += y01 + y02 - ((7/8)*y01 + (1/8)*y02 + (7/8)*y11 + (1/8)*y12) == 0
Lp_prob += y11 + y12 - ((1/8)*y01 + (7/8)*y02 + (1/8)*y11 + (7/8)*y12) == 0
Lp_prob += y01 >= 0
Lp_prob += y02 >= 0
Lp_prob += y11 >= 0
Lp_prob += y12 >= 0

status = Lp_prob.solve()
print()
print("*****************************")
print("*****************************")
print("La solución óptima es:")
print("y01 =", p.value(y01), "\ny02 =", p.value(y02), "\ny11 =", p.value(y11), 
      "\ny12 =", p.value(y12), "\nZ =", p.value(Lp_prob.objective))
print("*****************************")
print("*****************************")
