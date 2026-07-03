def resposta():
    pop_A = 80000
    pop_B =  200000
    fator_A =  1.03
    fator_B = 1.015   
    anos = 0
    
    while pop_A < pop_B:
        pop_A = pop_A * fator_A
        pop_B = pop_B * fator_B
        anos += 1 
    
    return (anos)