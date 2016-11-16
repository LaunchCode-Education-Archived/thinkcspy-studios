def launch_scrabble(words):
    points = 0
    for word in words:
        points += 1
        if (word[0] == 'q' and word[1] == 'u'):
            points += 10
        else:
            return 0
    return points
