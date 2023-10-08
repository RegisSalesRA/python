# Dada uma lista de palavras, encontre a palavra mais curta na lista.


lista = ["Aceven","Kraws","StractusSoul","Jonbared","Luk"]

lambada_achar_curta = lambda lista: sorted(lista,key=len)[0]
print(lambada_achar_curta(lista))

