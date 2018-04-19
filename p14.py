# https://projecteuler.net/problem=14

# idea: reverse the start, start with n = 1, chain as n * 2 or (n - 1) / 3
import timeit

start = timeit.default_timer()

chain_persists = True
chain_limit = 1000000
finished_chain = []

for x in range(1, chain_limit):
    chain = [x]
    chain_persists = True
    while chain_persists:
        # print "len: ", len(chain), "chain: ", chain
        if chain[-1] == 1:
            # print "chain ending: ", chain
            chain_persists = False
            if len(chain) > len(finished_chain):
                finished_chain = chain
        if chain[-1] % 2 == 0 and chain_persists:
            chain.append(chain[-1] / 2)
        elif chain[-1] % 2 == 1 and chain_persists:
            chain.append(chain[-1] * 3 + 1)

stop = timeit.default_timer()
print "start_value_chain: ", finished_chain[0], "exec time: ", stop - start
# print "finished_chain: ", finished_chain