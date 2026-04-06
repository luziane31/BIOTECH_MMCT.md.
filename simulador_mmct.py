# Simulador de Interrupção Informacional MMCT
# Protocolo: Retinose Pigmentar (Gene RHO / P23H)
# Autoria: Dra. Tech (Luziane Silva)

def calcular_indice_d(q_mutado, q_saudavel):
    # Parâmetros conforme seu dossiê
    K = 2        # Fator de segurança
    Im = 1.2     # Intensidade da informação mutada
    Tr = 0.8     # Fator de reversão temporal
    Ca = 1       # Carga da antipartícula (pósitron)
    
    # Cálculo de B (Antipartículas)
    B = abs(q_mutado - q_saudavel) * K
    
    # Cálculo de D (Índice de Duplicação)
    D = (Im * Tr) - (B * Ca)
    return B, D

# --- Execução da Simulação ---
q_m = -1.5 # Valor quântico da mutação P23H
q_s = -2.5 # Valor quântico saudável

posicons, indice_d = calcular_indice_d(q_m, q_s)

print(f"--- RESULTADO DA SIMULAÇÃO MMCT ---")
print(f"Pósitrons necessários por elétron mutado: {posicons}")
print(f"Índice de Duplicação Final (D): {indice_d:.2f}")

if indice_d <= 0:
    print("STATUS: SUCESSO. Transmissão da mutação BLOQUEADA.")
else:
    print("STATUS: FALHA. Transmissão ativa.")

