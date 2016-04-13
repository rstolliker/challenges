from collections import defaultdict


with open("boomerang_constellations_example_input.txt", 'r') as inp, open("boomerang_output.txt", 'w') as outp:
    num_cases = int(inp.readline())
    for i in range(num_cases):
        total = 0
        # Take input
        all_stars = []
        num_pairs = int(inp.readline())
        for j in range(num_pairs):
            all_stars.append(tuple(int(s) for s in inp.readline().split()))

        # Calculate distances
        dists = dict()
        for star1 in all_stars:
            dists = defaultdict(int)
            for star2 in all_stars:
                if star2 != star1:
                    dists[(star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) **2] += 1

            for d in dists.values():
                total += d * (d - 1) / 2
        outp.write("Case#{}: {}\n".format(i, total))