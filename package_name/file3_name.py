def metade(preço = 0, formato = False):
    if formato == True:
        return moeda(preço/2)
    else:
        return preço/2

def dobro(preço = 0, formato = False):
    if formato == True:
        return moeda(preço * 2)
    else:
        return preço * 2

def aumentar(preço = 0, taxa = 0, formato = False):
    if formato == True:
        return moeda(((preço * taxa)/100) + preço)
    else:
        return ((preço * taxa)/100) + preço
    
def diminuir(preço = 0, taxa = 0, formato = False):
    if formato == True:
        return moeda(preço - ((preço * taxa)/100))
    else:
        return preço - ((preço * taxa)/100)
    
def moeda(preço = 0, uniteMonetaire = 'R$'):
    return f'{uniteMonetaire}{preço:>.2f}'.replace('.', ',')