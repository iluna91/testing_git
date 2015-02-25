"""
Merge function for 2048 game. http://www.codeskulptor.org/#user39_NTx8Jn50VL_0.py  key:5j3H5rs4uq
"""
def adjust_line(line):
    """
    Function that adjust the line to the left
    """
    _line_slide = [ 0 for _item in line]
    _line_index = 0
    for _item in range(len(line)):
        if line[_item] != 0:
            _line_slide[_line_index] = line[_item]
            _line_index += 1
    return _line_slide

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line = adjust_line(line)
    for _item in range(len(line) - 1):
        if line[_item] == line[_item + 1]:
            line[_item] *= 2
            line[_item + 1] = 0
            line = adjust_line(line)
        elif line[_item + 1] == 0:
            break
    return line

