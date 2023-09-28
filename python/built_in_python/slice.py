"""
Em Python, slice() não é uma função independente, mas sim um tipo de objeto usado para criar fatias (slices) de sequências como strings, listas, tuplas e outros tipos iteráveis. O objeto de fatia é criado usando a sintaxe inicio:fim:passo, onde:

inicio: Índice de início da fatia (inclusive).
fim: Índice de término da fatia (exclusivo).
passo (opcional): Intervalo entre os elementos da fatia (padrão é 1).
Aqui estão alguns exemplos de como criar e usar objetos de fatia:

"""


seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
minha_fatia = slice(2, 7)


resultado = seq[minha_fatia]
print(resultado)  # Saída: [2, 3, 4, 5, 6]


minha_fatia_com_passo = slice(1, 8, 2)
resultado_com_passo = seq[minha_fatia_com_passo]
print(resultado_com_passo)  # Saída: [1, 3, 5, 7]
