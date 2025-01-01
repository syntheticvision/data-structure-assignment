# Main Author: Ashkan Rahimpour Harris, Babak Ghafourigivi
# Main Reviewer: Shayan Ramenzanzadeh

import a1_partd

def copy_board(board):
    return [row.copy() for row in board]

def evaluate_board(board, player):

    """
    Evaluate the game board from the perspective of the given player
    A high score is good for the player, and a low score is bad
    board: The game board represented as a 2D list
    player: The player to evaluate for (+1 or -1)

    Returns a numerical score representing the favorability of the board for the player
    """
    total_score = 0
    opponent = -player

    all_gems = [cell for row in board for cell in row if cell != 0]
    if all(cell > 0 for cell in all_gems):
        return float('inf') if player == 1 else float('-inf')
    if all(cell < 0 for cell in all_gems):
        return float('-inf') if player == 1 else float('inf')

    for row in board:
        for cell in row:
            if cell * player > 0:
                total_score += abs(cell)
            elif cell * opponent > 0:
                total_score -= abs(cell)

    return total_score

class GameTree:
    """
    Represents the game tree for a minimax-based game-playing AI
    The tree evaluates potential moves and selects the best one for the current player
    """

    class Node:
        """
        Represents a node in the game tree, corresponding to a specific board state
        """
        def __init__(self, board, depth, player, tree_height=4):
            self.board = copy_board(board)
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []
            self.value = None

        def add_child(self, child_node):
            self.children.append(child_node)

    def __init__(self, board, player, tree_height=4):
        """
        Initialize the game tree
        board: Initial game board
        player: The current player (+1 or -1)
        tree_height: Maximum depth of the game tree (default is 4)
        """
        self.player = player
        self.board = copy_board(board)
        self.tree_height = tree_height
        self.root = self.Node(self.board, 0, player, tree_height)
        self.build_tree(self.root)
    
    def make_move(self, row, col):
        """
        Apply a move to the game board and update the game tree
        row, col: Position to place the player's piece
        """

        self.undo_stack.push(copy_board(self.board))
        self.board[row][col] = self.player
        self.player = -self.player
        self.root = self.Node(self.board, 0, self.player, self.tree_height)
        self.build_tree(self.root)

    def undo_last_move(self):
        """
        Undo the last move by restoring the previous board state
        """
        previous_state = self.undo_stack.pop()
        if previous_state:
            self.board = previous_state
            self.player = -self.player
            self.root = self.Node(self.board, 0, self.player, self.tree_height)
            self.build_tree(self.root)
    
    def build_tree(self, node):
        """
        Recursively build the game tree starting from a given node
        node: The node to expand
        """

        if node.depth < self.tree_height:
            overflow_list = a1_partd.get_overflow_list(node.board)
            if overflow_list:
                for row, col in overflow_list:
                    new_board = copy_board(node.board)
                    new_board[row][col] = node.player
                    child_node = self.Node(new_board, node.depth + 1, -node.player, self.tree_height)
                    node.add_child(child_node)
                    self.build_tree(child_node)

    def minimax(self, node, depth, maximizing_player):
        """
        Perform the minimax algorithm to evaluate the best move
        node: The current node to evaluate
        depth: Remaining depth to search
        maximizing_player: True if maximizing player's turn, False otherwise

        Returns the evaluation score of the node
        """

        if depth == 0 or not node.children:
            node.value = evaluate_board(node.board, self.player)
            return node.value
        if maximizing_player:
            max_eval = float('-inf')
            for child in node.children:
                eval = self.minimax(child, depth - 1, False)
                max_eval = max(max_eval, eval)
            node.value = max_eval
            return max_eval
        else:
            min_eval = float('inf')
            for child in node.children:
                eval = self.minimax(child, depth - 1, True)
                min_eval = min(min_eval, eval)
            node.value = min_eval
            return min_eval

    def get_move(self):
        """
        Determine the best move for the current player using the minimax algorithm
        
        Returns a tuple (row, col) representing the best move
        """
        self.minimax(self.root, self.tree_height, True)
        max_eval = float('-inf')
        best_move = (0, 1)
        for child in self.root.children:
            if child.value > max_eval:
                max_eval = child.value
                best_move = self.find_move(self.board, child.board)
        return best_move

    def find_move(self, board1, board2):
        """
        Compare two boards and find the move that changes one to the other

        board1: Original board
        board2: Board after a move

        Returns a tuple (row, col) of the move position
        """
        for row in range(len(board1)):
         for col in range(len(board1[0])):
            if board1[row][col] != board2[row][col]:
                return row, col
         return (0, 0)

    def clear_tree(self):
        self.root = None
