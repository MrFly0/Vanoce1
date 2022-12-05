def get_points(oponent, us):
    points={"draw": 3, "lose":0, "win":6, "X":1, "Y":2, "Z":3}

    if oponent == 'A': #Rock
        if us == 'X': #Rock
            #draw
            sum = points['draw'] + points['X']
        elif us == 'Y': #Paper
            #lose
            sum = points['win'] + points['Y']
        elif us == 'Z': #Scissors
            #win
            sum = points['lose'] + points['Z']

    elif oponent == 'B': #Paper
        if us == 'X': #Rock
            #win
            sum = points['lose'] + points['X']
        elif us == 'Y': #Paper
            #draw
             sum = points['draw'] + points['Y']
        elif us == 'Z': #Scissors
            #lose
            sum = points['win'] + points['Z']

    elif oponent == 'C': #Scissors
        if us == 'X': #Rock
            #lose
            sum = points['win'] + points['X']
        elif us == 'Y': #Paper
            #win
            sum = points['lose'] + points['Y']
        elif us == 'Z': #Scissors
            #draw
            sum = points['draw'] + points['Z']
    return sum



with open('input.txt') as f:  #Opens file and reads data to string "lines"
    lines = f.readlines()

total_sum = 0
for match in lines:
    oponent = match[0]
    us = match[2]
    total_sum += get_points(oponent, us)

print(total_sum)