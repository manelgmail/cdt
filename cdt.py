def calcular_caida_tension():
    print("🧮 CÁLCULO DE CAÍDA DE TENSIÓN EN CABLES")

    # Entrada de datos
    L = float(input("Ingrese la longitud del cable (m): "))   
    W = float(input("Ingrese Wattios (W): "))
    COS = float(input("Ingrese valor COS: "))
    
    # Calcular intensidad 
    I = W / (230 * COS)

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
        rho = 0.0178

    # Calcular Sección    
    S = (2 * rho * L * I * COS) / 2.3
    
    # Cálculo de la caída de tensión
    Vd = (2 * rho * L * I * COS) / S
    
    # Lista de secciones normalizadas (en mm²)
    secciones_normalizadas = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240]

    # Buscar la sección normalizada más cercana mayor o igual a S
    S_normalizada = next((s for s in secciones_normalizadas if s >= S), None)

    # Mostrar resultado
    print(f"\n🔌 Caída de tensión: {Vd:.2f} V")
    print(f" Sección calculada: {S:.2f} mm2")
    if S_normalizada:
        print(f" Sección normalizada: {S_normalizada} mm2")
    else:
        print("⚠️ No se encontró una sección normalizada adecuada.")

    # Opcional: porcentaje de caída respecto a 220V
    volt_nominal = 220
    porcentaje = (Vd / volt_nominal) * 100
    print(f"📉 Porcentaje respecto a {volt_nominal}V: {porcentaje:.2f}%")

# Ejecutar el programa
calcular_caida_tension()
