from globalFunctions import readInputFile
import sys

directions = {
    'U': (1, 0),
    'D': (-1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def manhattam_distance(point):
    return abs(point[0]) + abs(point[1])

def draw_path(pos, command):
    positions = []
    dir = directions.get(command[0])
    for step in range(1, int(command[1:]) + 1):
         positions.append((pos[0] + step * dir[0], pos[1] + step * dir[1]))
    return positions

def save_path(path):
    pos = (0,0)
    positions = [(0, 0)]
    for command in path:
        positions.extend(draw_path(pos, command))
        pos = positions[-1]
    return positions

def solvePart1():
    inp = readInputFile('../Resources/Day3Input')
    wire_a = save_path(inp[0].strip().split(','))
    wire_b = save_path(inp[1].strip().split(','))
    intersections = set(wire_a) & set(wire_b)
    intersections.remove((0,0))
    md = sys.maxsize
    for cross in intersections:
        md = min(md, manhattam_distance(cross))
    return md

def solvePart2():
    inp = readInputFile('../Resources/Day3Input')
    wire_a = save_path(inp[0].strip().split(','))
    wire_b = save_path(inp[1].strip().split(','))
    intersections = set(wire_a) & set(wire_b)
    intersections.remove((0,0))
    signal_delay = sys.maxsize
    for cross in intersections:
        signal_delay = min(signal_delay, wire_a.index(cross) + wire_b.index(cross))
    return signal_delay

print solvePart1()
print solvePart2()