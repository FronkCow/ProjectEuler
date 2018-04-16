# https://projecteuler.net/problem=14

# idea: reverse the start, start with n = 1, chain as n * 2 or (n - 1) / 3

chain_exists = True
chain_limit = 5
finished_chain = []

list_chains = [[1]]
n = 1
while chain_exists:
    for x in range(0, len(list_chains)):
        print "len + " + str(len(list_chains))
        if list_chains[x][-1] * 2 > chain_limit and list_chains[x][-2] > chain_limit:
            print "here"
            finished_chain = list_chains.pop(x)
        else:
            list_chains[x].append(2 * list_chains[x][-1])

        if len(list_chains) == 0:
            chain_exists = False

        print x
        next_value = (list_chains[x][-1] - 1) / 3.0
        print next_value

        if next_value > 1 and next_value.is_integer():
            list_chains.append(list_chains[x] + [int(next_value)])

        print list_chains

print finished_chain