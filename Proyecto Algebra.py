# Edwin Mateo Camacho Tierradentro
# Universidad Distrital
# Febrero 2026

import numpy as np

def solicitar_ventas(producto):
    while True:
        entrada = input(f"Ingrese las ventas del {producto} separadas por comas (ej: 10,12,15,8): ")

        # Validación básica de símbolos
        if any(c.isalpha() for c in entrada):
            print("Error: No se permiten letras.")
            continue

        if entrada.count(",") != 3:
            print("Error: Debe ingresar exactamente 4 valores separados por comas.")
            continue

        try:
            valores = [float(x.strip()) for x in entrada.split(",")]

            # Validar cantidad
            if len(valores) != 4:
                print("Error: Debe ingresar exactamente 4 números.")
                continue

            # Validar negativos
            if any(v < 0 for v in valores):
                print("Error: No se permiten valores negativos.")
                continue

            return valores

        except ValueError:
            print("Error: Entrada inválida. Solo se permiten números.")


# Solicitar datos
ventas_A = solicitar_ventas("Producto A")
ventas_B = solicitar_ventas("Producto B")
ventas_C = solicitar_ventas("Producto C")

# Crear matriz NumPy
ventas = np.array([ventas_A, ventas_B, ventas_C])

# Cálculos
total_por_producto = np.sum(ventas, axis=1)
total_por_mes = np.sum(ventas, axis=0)
promedio_general = np.mean(ventas)
producto_mayor = np.argmax(total_por_producto)

# Mostrar resultados
print("\n--- RESULTADOS ---")
print("Total por producto:", total_por_producto)
print("Total por mes:", total_por_mes)
print("Promedio general:", promedio_general)

print("Producto con mayores ventas:", producto_mayor)
