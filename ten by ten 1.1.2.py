from random import *

def rule():
    print("You can")
    
def draw_board(board):
    x, y = len(board), len(board[0])
    print('    ', end='')
    for a in range(x):
        print('  %s   ' %(a+1), end='')
    print()
    print('    ', end='')
    print('_____ '*x)
    for i in range(y):
        print('   |', end='')
        print('     |'*x)
        if i < 9:
            z = str(i+1) + ' '
        else:
            z = str(i+1)
        print('%s |' %(z),end='')
        for j in range(x):
            print('  %s  |' %(board[j][i]), end='')
        print()
        print('   |', end='')
        print('_____|'*x)

def block(n):
    part = [[' ']*5,[' ']*5,[' ']*5,[' ']*5,[' ']*5]
    if n == 1:
        part[2][2] = '●'
    elif n == 2:
        part[1][2] = '■'
        part[2][2] = '●'
    elif n == 3:
        part[1][2] = '■'
        part[2][2] = '●'
        part[3][2] = '■'
    elif n == 4:
        part[0][2] = '■'
        part[1][2] = '■'
        part[2][2] = '●'
        part[3][2] = '■'
    elif n == 5:
        part[0][2] = '■'
        part[1][2] = '■'
        part[2][2] = '●'
        part[3][2] = '■'
        part[4][2] = '■'
    elif n == 6:
        part[2][1] = '■'
        part[2][2] = '●'
    elif n == 7:
        part[2][1] = '■'
        part[2][2] = '●'
        part[2][3] = '■'
    elif n == 8:
        part[2][0] = '■'
        part[2][1] = '■'
        part[2][2] = '●'
        part[2][3] = '■'
    elif n == 9:
        part[2][0] = '■'
        part[2][1] = '■'
        part[2][2] = '●'
        part[2][3] = '■'
        part[2][4] = '■'
    elif n == 10:
        part[1][1] = '■'
        part[1][2] = '■'
        part[2][2] = '●'
    elif n == 11:
        part[2][1] = '■'
        part[2][2] = '●'
        part[3][1] = '■'
    elif n == 12:
        part[2][2] = '●'
        part[3][2] = '■'
        part[3][3] = '■'
    elif n == 13:
        part[1][3] = '■'
        part[2][2] = '●'
        part[2][3] = '■'
    elif n == 14:
        part[1][1] = '■'
        part[1][2] = '■'
        part[2][1] = '■'
        part[2][2] = '●'
    elif n == 15:
        part[1][1] = '■'
        part[1][2] = '■'
        part[1][3] = '■'
        part[2][2] = '○'
        part[2][3] = '■'
        part[3][3] = '■'
    elif n == 16:
        part[1][1] = '■'
        part[1][2] = '■'
        part[1][3] = '■'
        part[2][1] = '■'
        part[2][2] = '○'
        part[3][1] = '■'
    elif n == 17:
        part[1][1] = '■'
        part[2][1] = '■'
        part[2][2] = '○'
        part[3][1] = '■'
        part[3][2] = '■'
        part[3][3] = '■'
    elif n == 18:
        part[1][3] = '■'
        part[2][2] = '○'
        part[2][3] = '■'
        part[3][1] = '■'
        part[3][2] = '■'
        part[3][3] = '■'
    elif n == 19:
        part[1][1] = '■'
        part[1][2] = '■'
        part[1][3] = '■'
        part[2][1] = '■'
        part[2][2] = '●'
        part[2][3] = '■'
        part[3][1] = '■'
        part[3][2] = '■'
        part[3][3] = '■'
    return part

def create_part():
    n1 = randint(1,19)
    n2 = randint(1,19)
    n3 = randint(1,19)
    return n1, n2, n3

def show_part(part1, part2, part3):
    x, y = 5, 5
    print('1                                   2                                   3')
    print(' ', end = '')
    print('_____ '*x, end = '')
    print('      ', end = '')
    print('_____ '*x, end = '')
    print('      ', end = '')
    print('_____ '*x)
    for i in range(y):
        print('|', end = '')
        print('     |'*x, end = '     ')
        print('|', end = '')
        print('     |'*x, end = '     ')
        print('|', end = '')
        print('     |'*x,)
        print('|', end = '')

        for j in range(x):
            print('  %s  |' %(part1[j][i]), end='')
        print('     |', end= '')
        for j in range(x):
            print('  %s  |' %(part2[j][i]), end='')
        print('     |', end= '')
        for j in range(x):
            print('  %s  |' %(part3[j][i]), end='')
        print()
        print('|', end = '')
        print('_____|'*x, end = '     ')
        print('|', end = '')
        print('_____|'*x, end = '     ')
        print('|', end = '')
        print('_____|'*x)

def choose_block(k_list, n1, n2, n3):
    k = 0
    playing = True
    try:
        while playing:
            while k not in range(1,4):
                while k not in k_list:
                    k = int(input('choose k (1-3)'))
            playing = False
            k_list.remove(k)
    except ValueError:
        print('choose k again')
        n = choose_block(k_list, n1, n2, n3)
    if k == 1:
        return n1
    elif k == 2:
        return n2
    elif k == 3:
        return n3
    else:
        return n
        

def put_part(n, part, board, x, y):
    if n in (15, 16, 17, 18):
        part[2][2] = ' '
    else:
        part[2][2] = '■'
    for i in range(5):
        for j in range(5):
            if part[i][j] != ' ':
                if x+(i-2) >= 0 and y+(j-2) >= 0 and x+(i-2) <= 9 and y+(j-2) <= 9:
                    board[x+(i-2)][y+(j-2)] = part[i][j]

def move_part(n, part, board):
    if n in (15, 16, 17, 18):
        part[2][2] = ' '
    else:
        part[2][2] = '■'
    x, y = 0, 0
    playing = True
    try:
        while playing:
            while x not in range(1,11):
                x = int(input('choose x (1-10)'))
            while y not in range(1,11):
                y = int(input('choose y (1-10)'))
            playing = False
            x, y = x-1, y-1
            for i in range(5):
                for j in range(5):
                    if part[i][j] != ' ':
                        if x+(i-2) < 0 or y+(j-2) < 0 or x+(i-2) > 9 or y+(j-2) > 9:
                            print('choose x and y again')
                            playing = True
                            x, y = 0, 0
                            break
                        elif x+(i-2) >= 0 and y+(j-2) >= 0 and x+(i-2) <= 9 and y+(j-2) <= 9:
                            if board[x+(i-2)][y+(j-2)] != ' ':
                                print('choose x and y again')
                                playing = True
                                x, y = 0, 0
                                break
                if playing:
                    break
    except ValueError:
        print('choose x and y again')
        x, y = move_part(n, part, board)
    return x, y
         
def remove_part(board):
  remove_line_x = []
  remove_line_y = []
  point = 0

  for i in range(len(board)):
    if board[i] == ['■','■','■','■','■','■','■','■','■','■']:
      remove_line_x.append(i)
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[j][i] == ' ':
        break
      if j == 9:
        remove_line_y.append(i)
        
  if remove_line_x != []:
    for x in remove_line_x:
      board[x] = [' ']*10
      point += 10
  if remove_line_y != []:
    for y in remove_line_y:
      for i in range(len(board[0])):
        board[i][y] = ' '
      point += 10
  return point

def block_point(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 3
  elif n == 4:
    return 4
  elif n == 5:
    return 5
  elif n == 6:
    return 2
  elif n == 7:
    return 3
  elif n == 8:
    return 4
  elif n == 9:
    return 5
  elif n == 10:
    return 3
  elif n == 11:
    return 3
  elif n == 12:
    return 3
  elif n == 13:
    return 3
  elif n == 14:
    return 4
  elif n == 15:
    return 5
  elif n == 16:
    return 5
  elif n == 17:
    return 5
  elif n == 18:
    return 5
  elif n == 19:
    return 9

def game_start():
    start_text = ' '
    while start_text != 'yes' and start_text != 'no':
        print('Do you want to play? ("yes" or "no")')
        start_text = input()
    return start_text

def choose_act():
    act_text = ' '
    while start_text != 'yes' and start_text != 'no':
        print('Chose the act ("rule" or "play")')
        act_text = input()

def game_end(board, part):
    end_command = True
    end_count = 0
    for x in range(10):
        for y in range(10):
            playing = False
            for i in range(5):
                for j in range(5):
                    if part[i][j] != ' ':
                        if x+(i-2) < 0 or y+(j-2) < 0 or x+(i-2) > 9 or y+(j-2) > 9:
                            playing = True
                            end_count += 1
                            break
                        elif x+(i-2) >= 0 and y+(j-2) >= 0 and x+(i-2) <= 9 and y+(j-2) <= 9:
                            if board[x+(i-2)][y+(j-2)] != ' ':
                                playing = True
                                end_count += 1
                                break
                if playing:
                    break
    if end_count >= 100:
        end_command = False
    return end_command

def distinction_playing(k_list, playing1, playing2, playing3):
    playing = True
    if 1 not in k_list:
        if 2 not in k_list:
            if 3 in k_list:
                playing = playing3
        else:
            if 3 not in k_list:
                playing = playing2
            else:
                playing = playing2 or playing3
    else:
        if 2 not in k_list:
            if 3 not in k_list:
                playing = playing1
            else:
                playing = playing1 or playing3
        else:
            if 3 not in k_list:
                playing = playing1 or playing2
            else:
                playing = playing1 or playing2 or playing3
    return playing

def play_again():
    again_text = ' '
    while again_text != 'yes' and again_text != 'no':
        print('Do you want to play again? ("yes" or "no")')
        again_text = input()
    return again_text

def playing_game(the_board, total_point):
    k_list = [1, 2, 3]
    draw_board(the_board)
    n1, n2, n3 = create_part()
    part1 = block(n1)
    part2 = block(n2)
    part3 = block(n3)
    show_part(part1, part2, part3)
    
    playing1 = game_end(the_board, part1)
    playing2 = game_end(the_board, part2)
    playing3 = game_end(the_board, part3)
    playing = distinction_playing(k_list, playing1, playing2, playing3)
    while playing:
        n = choose_block(k_list, n1, n2, n3)
        part = block(n)
        x, y = move_part(n, part, the_board)
        put_part(n, part, the_board, x, y)
        put_point = block_point(n)
        total_point += put_point
        line_point = remove_part(the_board)
        total_point += line_point
        break
    print(total_point)

    draw_board(the_board)
    playing1 = game_end(the_board, part1)
    playing2 = game_end(the_board, part2)
    playing3 = game_end(the_board, part3)
    playing = distinction_playing(k_list, playing1, playing2, playing3)
    while playing:
        n = choose_block(k_list, n1, n2, n3)
        part = block(n)
        x, y = move_part(n, part, the_board)
        put_part(n, part, the_board, x, y)
        put_point = block_point(n)
        total_point += put_point
        line_point = remove_part(the_board)
        total_point += line_point
        break
    print(total_point)

    draw_board(the_board)
    playing1 = game_end(the_board, part1)
    playing2 = game_end(the_board, part2)
    playing3 = game_end(the_board, part3)
    playing = distinction_playing(k_list, playing1, playing2, playing3)
    while playing:
        n = choose_block(k_list, n1, n2, n3)
        part = block(n)
        x, y = move_part(n, part, the_board)
        put_part(n, part, the_board, x, y)
        put_point = block_point(n)
        total_point += put_point
        line_point = remove_part(the_board)
        total_point += line_point
        break
    print(total_point)
    
    return total_point, playing

while True:
    start_text = game_start()
    if start_text == 'no':
        break

    the_board = [[' ']*10,[' ']*10,[' ']*10,[' ']*10,[' ']*10,[' ']*10,[' ']*10,[' ']*10,[' ']*10,[' ']*10]
    total_point = 0
    playing = True
    
    while playing:
        total_point, end_command = playing_game(the_board, total_point)

        if end_command:
            pass
        else:
            break

    again_text = play_again()
    if again_text == 'no':
        break
