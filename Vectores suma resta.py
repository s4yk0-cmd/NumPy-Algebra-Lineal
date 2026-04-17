import numpy as np
import matplotlib.pyplot as plt

def suma_vectores(A, B):
    return A + B

def resta_vectores(A, B):
    return A - B

def producto_escalar(A, B):
    return np.dot(A, B)

suma_ejercicios = [
    (np.array([2, 3]), np.array([4, 1])),
    (np.array([-1, 5]), np.array([3, -2])),
    (np.array([0, 4]), np.array([5, 0])),
    (np.array([6, -3]), np.array([-2, 7])),
    (np.array([1, 1]), np.array([2, 3]))
]

print("SUMA DE VECTORES")
for i, (A, B) in enumerate(suma_ejercicios, 1):
    print(f"{i}: {A} + {B} = {suma_vectores(A,B)}")

print("\nRESTA DE VECTORES")
for i, (A, B) in enumerate(suma_ejercicios, 1):
    print(f"{i}: {A} - {B} = {resta_vectores(A,B)}")

producto_ejercicios = [
    (np.array([2, 3]), np.array([4, -1])),
    (np.array([-1, 5]), np.array([3, 2])),
    (np.array([6, 2]), np.array([3, 7])),
    (np.array([1, -2]), np.array([-3, 4])),
    (np.array([5, 2]), np.array([5, 2]))
]

print("\nPRODUCTO ESCALAR")
for i, (A, B) in enumerate(producto_ejercicios, 1):
    print(f"{i}: {A} · {B} = {producto_escalar(A,B)}")

A = np.array([2, 3])
B = np.array([4, 1])
R = suma_vectores(A, B)

plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(A[0], A[1], B[0], B[1], angles='xy', scale_units='xy', scale=1, color='green')
plt.quiver(0, 0, R[0], R[1], angles='xy', scale_units='xy', scale=1, color='red')
plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.grid()
plt.title("Suma de vectores (Método del triángulo)")