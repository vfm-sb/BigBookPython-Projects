# Carrot in a Box - Instructions

This is a simple and silly bluffing game for two human players.
* Each player has a box.
* One box has a carrot in it, and each player wants to have the carrot.
* The first player looks in their box and then tells the second player they either do or don’t have the carrot.
* The second player gets to decide whether to swap boxes or not.

<br>

## The Program in Action

```
Carrot in a Box, by Al Sweigart al@inventwithpython.com
--snip--
Human player 1, enter your name: Alice
Human player 2, enter your name: Bob
HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
   Alice           Bob

Alice, you have a RED box in front of you.
Bob, you have a GOLD box in front of you.
Press Enter to continue...
--snip--
When Bob has closed their eyes, press Enter...
Alice here is the inside of your box:

   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 (carrot!)
   Alice           Bob
Press Enter to continue...
--snip--
```

<br>

## How It Works

This program relies on the second player closing their eyes so they don’t see the contents of the first player’s box. 

In order to keep the second player from seeing the box contents after this step, we need to find a way to clear the screen.

> Use `os.system("clear")`

<br>
<hr>
<br>

## Application Mockup

```python
"""
Carrot in a Box
A silly bluffing game between two human players.
Based on the game from the show, 8 Out of 10 Cats.
"""
```

1. The first player looks into their box.
    1. The second player must close their eyes during this.
2. The first player then says "There is a carrot in my box" or "There is not a carrot in my box".
3. The second player then gets to decide if they want to swap boxes or not.

```
Carrot in a Box from "8 Out of 10 Cats"

Rules:
* Enter Player Names.
* The First Player Looks Into Their Box.
* The Second Player Must Close Their Eyes During This!
* The First Player Says:
    * There is a Carrot in My Box
    * There is not a Carrot in My Box
* The Second Player Decides If They Want to Swap or Not!

Press Enter to Begin...
```

```
Enter Name of Player 1:
Enter Name of Player 2:

"""
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
"""
```