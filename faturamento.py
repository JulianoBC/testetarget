## Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
##• O menor valor de faturamento ocorrido em um dia do mês;
##• O maior valor de faturamento ocorrido em um dia do mês;
##• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

##IMPORTANTE:
##a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
##b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; 


## Em python,
faturamento = [3333, 1200, 800, 1500, 444, 1300, 1100, 667, 700, 1600, 111, 1250, 1050]

menor = faturamento[0]
maior = faturamento[0]

soma = 0

for valor in faturamento:
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
    soma += valor
    
media = soma / len(faturamento)
mediaRedondada = round(media, 2)
    
    
dias_acima_da_media = 0

for valor in faturamento:
    if valor > media:
        dias_acima_da_media += 1
        
print("O menor valor de faturamento ocorrido em um dia do mês foi:R$", menor)
print("O maior valor de faturamento ocorrido em um dia do mês foi:R$", maior)
print("O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi:", dias_acima_da_media)
print("a média foi:R$",mediaRedondada)