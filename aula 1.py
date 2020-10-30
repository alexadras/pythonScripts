# Jogo da velha


# declaração
a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = ' ' # tabuleiro 
player = False   # true = X
                # false = O 


#loop geral
while True :

  
    # out
    
    print('\tA B C \n',
          f'1\t{a1}|{b1}|{c1}\n',
          '\t-+-+-\n',
          f'2\t{a2}|{b2}|{c2}\n',
          '\t-+-+-\n',
          f'3\t{a3}|{b3}|{c3}\n')


    # Ganhou ou empatou?
      # Verificação vertical              HORIZONTAL                                                           DIAGONAL
    if a1 == a2 == a3 != ' ' or b1 == b2 == b3 != ' ' or c1 == c2 == c3 != ' ' or a1 == b1 == c1 != ' '  or a2 == b2 == c2 != ' ' or a3 == b3 == c3 != ' ' or a1 == b2 == c3 != ' ' or c1 == b2 == a3 != ' ':
        if player:
            print ("X >ganhou chap chap ")
        else:
            print ("O > ganhou chap chap ")

        break

    elif a1 !=  ' ' and a2 !=  ' ' and a3 !=  ' ' and b1 !=  ' ' and b2 !=  ' ' and b3 !=  ' ' and c1 !=  ' ' and c2 !=  ' ' and c3 !=  ' ' :
        print ('deu veia !!!!!!!!!!!!!')
        break

     # troca da vez
    player = not player 



    #in
    if player:
        pos = input ('X: ')
        
        if pos.upper() == 'A1' and a1 == ' ':
            a1 = 'X'
        elif pos.upper() == 'A2' and a2 == ' ':
            a2 = 'X'
        elif pos.upper() == 'A3' and a3 == ' ':
            a3 = 'X'
        elif pos.upper() == 'B1' and b1 == ' ':
            b1 = 'X'
        elif pos.upper() == 'B2' and b2 == ' ':
            b2 = 'X'
        elif pos.upper() == 'B3' and b3 == ' ':
            b3 = 'X'
        elif pos.upper() == 'C1' and c1 == ' ':
            c1 = 'X'
        elif pos.upper() == 'C2' and c2 == ' ':
            c2 = 'X'
        elif pos.upper() == 'C3' and c3 == ' ':
            c3 = 'X'
        else:
            print('Posição INVÁLIDA!\nEntre com outra posição')
            player = not player

    else :
        pos = input ('O: ')

        if pos.upper() == 'A1' and a1 == ' ':
            a1 = 'O'
        elif pos.upper() == 'A2' and a2 == ' ':
            a2 = 'O'
        elif pos.upper() == 'A3' and a3 == ' ':
            a3 = 'O'
        elif pos.upper() == 'B1' and b1 == ' ':
            b1 = 'O'
        elif pos.upper() == 'B2' and b2 == ' ':
            b2 = 'O'
        elif pos.upper() == 'B3' and b3 == ' ':
            b3 = 'O'
        elif pos.upper() == 'C1' and c1 == ' ':
            c1 = 'O'
        elif pos.upper() == 'C2' and c2 == ' ':
            c2 = 'O'
        elif pos.upper() == 'C3' and c3 == ' ':
            c3 = 'O'
        else:
            print('Posição INVÁLIDA!\nEntre com outra posição')
            player = not player


#fim do codigo 


    
