def validar_afiliado(documento, estado):
    """
    Valida si un afiliado de EPS está activo y tiene un documento válido.
    Parámetros:
        documento (str): Número de documento de identidad
        estado (str): Estado del afiliado (activo, suspendido, retirado)
    Retorna:
        tuple: (bool, str) - (es_valido, mensaje)
    """
    if not documento or len(str(documento)) < 5:
        return False, "Documento inválido"
    
    estados_validos = ["activo", "suspendido", "retirado"]
    if estado.lower() not in estados_validos:
        return False, "Estado no reconocido"
    
    if estado.lower() != "activo":
        return False, f"Afiliado no activo (estado: {estado})"
    
    return True, "Afiliado válido y activo"


# Ejemplo de uso
if __name__ == "__main__":
    print(validar_afiliado("1234567890", "activo"))
    print(validar_afiliado("123", "activo"))
    print(validar_afiliado("9876543210", "suspendido"))

