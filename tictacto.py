
list  = ['|1|','|2|','|3|','|4|','|5|','|6|','|7|','|8|','|9|']
len_list = []
firstplayer = True
marker = '|X|'
winortie = 0

def DrawBoared():
    for i in range(0,len(list)):
        if i==2 or i==5 or i==9:
            print(list[i],end='\n')
            print('-----------')
        else:
            print(list[i],end=' ')
    print('\n')

def GetPlayerInput():
    global firstplayer
    global marker
    global winortie
    global len_list
    global list
    while True:
        if firstplayer:
            print('First Player Enter where You want "X" To be Positioned?')
            player_input = int(input())
            len_list.append(player_input)
            for i in range(0,len(list)):
                list[abs(player_input-1)] = marker
            firstplayer=False
            marker = '|O|'
        else:
            print('2nd Player Enter where You want "O" To be Positioned?')
            player_input = int(input())
            len_list.append(player_input)
            for i in range(0,len(list)):
                list[abs(player_input-1)] = marker
            firstplayer=True
            marker = '|X|'
        DrawBoared()
        winortie = check()
        if winortie:
            if winortie == 1:
                print("1st Player Win !")
            if winortie == 2:
                print("2nd Player Win !")
            if winortie == 3:
                print("A Tie Win !")
            print('Do You Want To Play Agine press "y to conine or any thing else to quite"')
            if input() == 'y':
                list  = ['|1|','|2|','|3|','|4|','|5|','|6|','|7|','|8|','|9|']
                # list  = ['| |','| |','| |','| |','| |','| |','| |','| |','| |']
                len_list = []
                firstplayer = True
                marker = '|X|'
                winortie = 0
                DrawBoared()
            else:
                break

def check():
    if (list[0]==list[1]==list[2])or (list[3]==list[4]==list[5]) or (list[6]==list[7]==list[9]) or (list[0]==list[4]==list[8]) or (list[2]==list[4]==list[6]) or (list[0]==list[3]==list[6])or (list[1]==list[4]==list[7])or (list[2]==list[5]==list[8]):
        if not firstplayer:
            return 1
        else:
            return 2
    elif len(len_list) == 9:
        return 3











if __name__ == '__main__':
    DrawBoared()
    GetPlayerInput()
