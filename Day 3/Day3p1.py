from collections import Counter

#def get_file():
#    with open("input.txt", "r") as f:
#        return [(c.split()[0], int(c.split()[1])) for c in f.read().splitlines()]

with open("input.txt") as input:
    m = [a.strip() for a in input.readlines()]

gamma   = int("".join([Counter([x[i] for x in m]).most_common(1)[0][0] for i in range(len(m[0]))]) ,2) #most
epsilon = int("".join([Counter([x[i] for x in m]).most_common()[-1][0] for i in range(len(m[0]))]), 2) #least

print(f"Solution [gamma * epsilon]: {gamma * epsilon}")
