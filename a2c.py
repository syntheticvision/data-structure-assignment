import pygame
import sys
import math
import player1
import player2
import a2_parta
import a2_partb
import a1_partd
import a1_partc
import game
import time


# Timer for player
turn_start_time = time.time()
time_limit = 10

current_player = 0
status = ["", ""]
current_time = time.time()

if current_time - turn_start_time > time_limit:
    status[1] = f"Player {current_player + 1} ran out of time!"
    current_player = (current_player + 1) % 2
    turn_start_time = time.time()

# Score tracking
scores = {1: 0, 2: 0}
winner = 1
scores[winner] += 1

# Add an undo function
undo_stack = []
def undo(self):
    if self.undo_stack:
        self.set(self.undo_stack.pop())
        self.turn -= 1
        return True
    return False







