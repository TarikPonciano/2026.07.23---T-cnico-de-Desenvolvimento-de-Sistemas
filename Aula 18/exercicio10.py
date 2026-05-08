# 10. Ranking de vendas com múltiplas operações
# Uma loja registrou o nome e o total de vendas de 5 vendedores em duas listas paralelas. O aluno deve: (a) exibir o ranking completo; (b) encontrar o melhor vendedor pelo maior valor; (c) calcular a média de vendas da equipe; (d) exibir apenas os vendedores acima da média; (e) verificar se algum vendedor atingiu a meta de R$ 5.000 usando any(). Todo o processamento deve usar for, enumerate() e as funções max(), min(), sum() e len().

vendedores = ["Johnny", "Sarah", "Joaquim", "Manel", "Maicão"]

faturamentos = [2500, 3500, 3700, 4900, 5500]

melhor_vendedor = ""
maior_faturamento = 0

print("VENDEDOR | FATURAMENTO R$")
for i in range(len(vendedores)):
    print(f"{vendedores[i]} - R${faturamentos[i]:,.2f}")

    if faturamentos[i] > maior_faturamento:
        maior_faturamento = faturamentos[i]
        maior_vendedor = vendedores[i]

print(f"Melhor Vendedor: {maior_vendedor} - R$ {maior_faturamento:,.2f}")
print()

media_faturamento = sum(faturamentos)/len(faturamentos)

print(f"Média de Faturamento: R$ {media_faturamento:,.2f}")

print()
print("Vendedores acima da média")
print("VENDEDOR | FATURAMENTO R$")
for i in range(len(vendedores)):
    if faturamentos[i] > media_faturamento:
        print(f"{vendedores[i]} - R${faturamentos[i]:,.2f}")


print()
print("Vendedores acima de R$ 5000,00")
print("VENDEDOR | FATURAMENTO R$")

for i in range(len(vendedores)):
    if faturamentos[i] > 5000:
        print(f"{vendedores[i]} | R$ {faturamentos[i]:,.2f}")