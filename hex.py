from random import choice

ADJACENCIES = [
    (0,2),   # N
    (1,1),   # NE
    (1,-1),  # SE
    (0,-2),  # S
    (-1,-1), # SW
    (-1,1)   # NW
]

def neighbors(base):
    basey = base[0]
    basex = base[1]
    return [(basey+y,basex+x) for y,x in ADJACENCIES]

def minmax(iterable):
    first = True
    for element in iterable:
        if first:
            low = element
            high = element
            first = False
        else:
            if element < low:
                low = element
            if element > high:
                high = element
    return (low,high)

def printout(hexes):
    lowest_x,highest_x = minmax(x for y,x in hexes)
    lowest_y,highest_y = minmax(y for y,x in hexes)

    text = ""
    for x in range(lowest_x,highest_x+1):
        line = ""
        for y in reversed(range(lowest_y,highest_y+1)):
            if (y,x) in hexes:
                line += "O"
            elif (y+x)%2==0:
                line += "."
            else:
                line += " "
            line += "  "
        text += line+"\n"
    print(text)

def printout_key(hexes, key):
    return map(lambda cell: hexes[cell][key],hexes.keys())

def generate(area):
    land_hexes = [(0,0)]
    for i in range(area-1):
        boundary = [cell for cell in sum(map(neighbors, land_hexes), []) if cell not in land_hexes]
        land_hexes.append(choice(boundary))
    return land_hexes

def generate_grid_with_contents(min_x,max_x,min_y,max_y):
    hexes = {}
    for x in range(min_x,max_x+1):
        for y in range(min_y,max_y+1):
            if (x+y) % 2 == 0:
                hexes[(x,y)] = { "algae": 1 }
    return hexes

printout(filter_grid(generate_grid_with_contents(0,10,0,10), "algae"))
