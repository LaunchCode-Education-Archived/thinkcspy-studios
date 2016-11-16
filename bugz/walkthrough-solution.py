def launch_scrabble(words):
    points = 0
    for word in words:
        if (word[0] == 'q'):
            if (word[1] == 'u'):
                points += 10
            else:
                return 0
        else:
            points += 1
    return points
