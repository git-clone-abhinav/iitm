def process():
    first = board_min()
    board_erase(first)

    if board_isEmpty():
        return first

    second = board_min()
    board_erase(second)

    delta = second - first
    board_write(delta)

    return process()