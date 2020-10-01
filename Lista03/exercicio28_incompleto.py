# Uma companhia de seguros possui um numero indeterminado de corretores. 
# A companhia paga para o salario de cada corretor na forma de
# comissao, calculada de acordo com a venda mensal do corretor. 
# Essa comissao e de 35% do valor da venda, se esse valor for maior que R$3000,00; 
# 20% do valor da venda, se esse valor estiver entre R$ 1500,00 e R$ 3000,00; 
# e 13% do valor da venda, se este valor estiver abaixo de R$1500,00.

# Mostre o salario (comissao) de cada corretor;
# Calcule e mostre o total de vendas da companhia;
# Calcule e mostre o total geral de salarios (comissoes) pagos aos corretores.

while True:
    valVenda = int(input('Insira o valor da venda: '))
    
    if valVenda < 1500:
        comissao = valVenda - (valVenda * 13 / 100)
        print(f'O valor da comissao é: {valVenda - comissao}')
    elif  valVenda > 1500 and val < 3000:
        comissao = valVenda - (valVenda * 20 / 100)
        print(f'O valor da comissao é: {valVenda - comissao}')
    elif valVenda > 3000:
        comissao = valVenda - (valVenda * 35 / 100)
        print(f'O valor da comissao é: {valVenda - comissao}')
    
    