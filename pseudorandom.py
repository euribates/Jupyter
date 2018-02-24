def msm(seed):
    if seed == 0:
        return 0
    n = seed ** 2
    s = '{:08d}'.format(n)
    return int(s[-6:-2])

assert msm(540) == 2916
assert msm(2916) == 5030
assert msm(5030) == 3009
assert msm(3009) == 540

n = 2916
for i in range(4):
    n = msm(n)
print(n)
assert n == 2916

n = 1086
for i in range(32):
    n = msm(n)
print(n)


# for seed in range(1, 10000):
    # count = 1
    # n = msm(seed)
    # while n != seed and n != 0:
        # n = msm(n)
        # count += 1
        # if count > 9200:
            # break
    # if n == seed and count > 1:
        # print('Eureka: seed: {} count: {}'.format(seed, count))

