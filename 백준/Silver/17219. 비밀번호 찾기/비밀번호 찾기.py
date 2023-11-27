import sys
input = sys.stdin.readline
sites = []
passwords = []

m, n = map(int, input().split())
for i in range(m):
    key, ans = input().split()
    sites.append(key)
    passwords.append(ans)

pass_dict = dict(zip(sites, passwords))

# print(sites)
# print(passwords)
# print(pass_dict)
for i in range(n):
    print(pass_dict[input().replace('\n','')])
    