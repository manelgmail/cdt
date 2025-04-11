def calcular_caida_tension():
    print("🧮 CÁLCULO DE CAÍDA DE TENSIÓN EN CABLES")
    
    # Entrada de datos
    I = float(input("Ingrese la corriente (A): "))
    L = float(input("Ingrese la longitud del cable (m): "))
    A = float(input("Ingrese la sección del cable (mm^2): "))
    
    print("Tipo de material:")
    print("1 - Cobre")
    print("2 - Aluminio")
    M = int(input("Seleccione el material (1 o 2): "))
    
    # Resistividad según material
    if M == 1:
        rho = 0.0178  # ohm·mm²/m para cobre
    elif M == 2:
        rho = 0.0282  # ohm·mm²/m para aluminio
    else:
        print("Opción inválida. Asignando cobre por defecto.")
        rho = 0.0175

    # Cálculo de la caída de tensión
    Vd = (2 * rho * L * I) / A
    
    # Mostrar resultado
    print(f"\n🔌 Caída de tensión: {Vd:.2f} V")
    
    # Opcional: porcentaje de caída respecto a 220V
    volt_nominal = 220
    porcentaje = (Vd / volt_nominal) * 100
    print(f"📉 Porcentaje respecto a {volt_nominal}V: {porcentaje:.2f}%")

# Ejecutar el programa
calcular_caida_tension()
