# Studio: Bugz

## Concepts Used

Debugging some programs with common mistakes.

## Walkthrough

This is LaunchScrabble, a unique version of Scrabble! This function takes a list of words from a LaunchScrabble game and calculates the player's score. All words count as one point, but words that begin with 'q' are 10 points!

But since 'q' words are worth so many points, we want to make sure our players aren't cheating and making up words that start with 'q'. So for every word that begins with 'q', the program checks to make sure the following letter is 'u'. If we find an exception, for instance "qrie", negate all their points and give that cheater an overall score of 0!

See `walkthrough.py` for the code.

### Walkthrough Solution

Problems:
1. All words that do not begin with 'q' will automatically return 0
2.  q words add 11 to the total points

There are a couple ways to fix this (for instance, you could use nested conditionals or boolean logic to deal with the 'q' words), but one possible solution is `walkthrough-solution.py`.

## Studio

[Book Page Link](https://runestone.launchcode.org/runestone/static/thinkcspy/Studios/bugz.html)

Below are the answers:

- Exercise 1:
    - the variable `i` is used twice. Change the loop variable (and the associated `print` statement) to something else.

- Exercise 2:
    - the function returns `True` while iterating. So if the first person in the list is old enough to enter the bar, the function will eroneously return `True` immediately, even though subsequent people might be too young.

- Exercise 3:
    - the `else` is followed by a condition, so it should be an `elif`.
