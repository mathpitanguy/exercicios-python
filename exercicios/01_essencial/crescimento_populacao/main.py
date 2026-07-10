def resposta(populacao_a, taxa_a, populacao_b, taxa_b):
    populacao_a = 80000
    populacao_b =  200000
    taxa_a =  1.03
    taxa_b = 1.015   
    anos = 0
    
    while pop_A < pop_B:
        populacao_a = populacao_a * taxa_a
        populacao_b = populacao_b * taxa_b
        anos += 1 
    
    return (anos)
