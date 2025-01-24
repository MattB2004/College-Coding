def solve_puzzle(board, index = 0, visited = None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""

    # 1) Base case: have you found a valid solution?

    # 2) Find all valid next-steps

    # 3) Recursively explore next-steps, returning True if any valid solution is found
    return helper(board, index, visited)

def helper(board, index = 0, visited = None):
        if index == len(board) - 1:
            return True
        
        if visited == None:
            visited = set()
        
        next_moves = set()

        visited.add(index)

        cw = (index + board[index]) % len(board)

        ccw = (index - board[index]) % len(board)

        if cw not in visited:
            next_moves.add(cw)

        if ccw not in visited:
            next_moves.add(ccw)

        if (cw in visited) and (ccw in visited):
            return False


        
        return any(helper(board, i, visited) for i in next_moves)