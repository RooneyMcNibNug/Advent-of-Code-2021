def get_file():
    with open("input.txt", "r") as f:
        return [(c.split()[0], int(c.split()[1])) for c in f.read().splitlines()]


input = get_file()

def forward(pos, n):
    pos[0] += n

def down(pos, n):
    pos[1] += n

def up(pos, n):
    pos[1] -= n

commands = {
    "forward" : forward,
    "down" : down,
    "up" : up
}


pos = [0, 0]

for step in input:
    commands[step[0]](pos, step[1])

print(f"position [x, y] => ({pos[0]}, {pos[1]})")
print(f"Solution [mult] <{pos[0]*pos[1]}>")