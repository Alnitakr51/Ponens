# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 07:10:22 2023

@author: Gadiel Jimenez
"""

def modus_ponens(p, q):
    """

    Args:
        p (bool): La premisa p.
        q (bool): La consecuencia q.

    Returns:
        bool: El resultado de la inferencia.
    """
    if p:
        if p is True and q is True:
            return True  # Si p es verdadero y q es verdadero, la inferencia es verdadera
        else:
            return False  # Si p es verdadero pero q no es verdadero, la inferencia es falsa
    else:
        return True  # Si p es falso, la inferencia es verdadera ya que no hay condición que incumplir

# Definición de la premisa y la consecuencia
premisa_p = True
consecuencia_q = False

# Aplicación de Modus Ponens
resultado_inferencia = modus_ponens(premisa_p, consecuencia_q)

# Mostrar el resultado
if resultado_inferencia:
    print("Se cumple el Modus Ponens: q es verdadero.")
else:
    print("No se cumple el Modus Ponens: q es falso.")
