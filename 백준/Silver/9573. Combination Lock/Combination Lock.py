n = int(input())


def get_range(x):
    return [((x + i - 1) % n) + 1 for i in range(-2, 3)]


fa, fb, fc = map(int, input().split())
ma, mb, mc = map(int, input().split())


combs = set()
for a in get_range(fa):
    for b in get_range(fb):
        for c in get_range(fc):
            combs.add((a, b, c))

for a in get_range(ma):
    for b in get_range(mb):
        for c in get_range(mc):
            combs.add((a, b, c))


print(len(combs))
