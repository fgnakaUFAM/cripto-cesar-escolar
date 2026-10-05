#CIFRA DE CESAR
opcao = int(input())

if opcao == 1:

    original = input()
    chave = int(input())
    cifrada = ""
    if chave > 26:
        chave = chave % 26
        
    for letra in original:
        asciiLetra = ord(letra)
        deslocamenteChave = asciiLetra  + chave
        if deslocamenteChave >  122:
            deslocamenteChave = deslocamenteChave - 123 + 97
        cifrada += chr(deslocamenteChave)
        
        
    print(cifrada)    
    
elif opcao == 2:
    cifrada = input()
    chave = int(input())
    original = ""
    if chave > 26:
        chave = chave % 26
        
    for letra in cifrada:
        asciiLetra = ord(letra)
        deslocamenteChave = asciiLetra  -  chave
        if deslocamenteChave < 97 :
            deslocamenteChave = deslocamenteChave + 123 - 97
        original += chr(deslocamenteChave)
        
        
    print(original)
    
elif opcao == 3:
    cifrada = input()

    for chave in range(1,25):    
        original = ""
        
        for letra in cifrada:
            asciiLetra = ord(letra)
            deslocamenteChave = asciiLetra  -  chave
            if deslocamenteChave < 97 :
                deslocamenteChave = deslocamenteChave + 123 - 97
            original += chr(deslocamenteChave)
            
        
        print(original)
    
