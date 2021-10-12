#!/usr/bin/env python
from random import random
import numpy

def absolute(*x) -> float:
    res = 0
    for xi in x:
        res += abs(xi)
    return res

class Particle:
    """Clase que representa cada partícula dentro del espacio de búsqueda"""
    def __init__(self, choiseMax: float, choiseMin: float):
        # Se inicializan los valores
        self.position = ( choiseMin + ( random() * 100 ) ) % choiseMax
        self.cost = absolute(self.position)
        self.velocity = 0
        # Se inicializan los mejores locales con los valores iniciales para pos y cos
        self.best = { "position": self.position, "cost": self.cost }

    def __repr__(self) -> str:
        """Muestra un string con todos los atributos de la clase"""
        return f"(pos: {self.position}, cost: {self.cost}, vel: {self.velocity}), best: ({self.best})\n"

# Parámetros del PSO
choiseMin = -10
choiseMax = 10
popSize = 50
maxIter = 1000
# Coeficiente de inercia
w = 1
# Relación de amortiguación del peso de la inercia
wAmort = 0.99
# Coeficiente de aceleración personal
c1 = 2
# Coeficiente de aceleración social
c2 = 2
# Mejor partícula a nivel global
globalBest = { "position": float("inf"), "cost": float("inf") }
particles = [ Particle(choiseMax, choiseMin) for _ in range(popSize) ]

for i in particles:
    if i.cost < globalBest["cost"]:
        globalBest = i.best

for iter in range( maxIter ):
    for i in range( popSize ):
        particles[i].velocity = w * particles[i].velocity + \
            c1 * random() * (particles[i].best["position"] - particles[i].position) + \
            c2 * random() * (globalBest["position"] - particles[i].position)
        particles[i].position = particles[i].position + particles[i].velocity
        particles[i].cost = absolute(particles[i].position)
        # Si el costo es el menor local hasta el momento
        if abs( particles[i].cost ) < abs( particles[i].best["cost"] ):
            particles[i].best = { "position": particles[i].position, "cost": particles[i].cost }
        # Si el costo es el menor global hasta el momento
        if abs( particles[i].best["cost"] ) < abs( globalBest["cost"] ):
            globalBest = particles[i].best
    w *= wAmort
    print(globalBest, w)
