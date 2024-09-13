def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    
    normalize_visuais = set ([visuais.title() for visuais in visuais ])
   
    
    lista_final = sorted(normalize_visuais)
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)