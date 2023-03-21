
# Binary to Gray Code b2g(n)
# Gray Code to Binary g2b(n)

b2g = lambda n: n ^ (n>>1)

def g2b(N):
    bN = [int(b) for b in bin(N)[2:]]
    gc = [0]
    for b in bN:
        gc.append(gc[-1] ^ b)
    return int("".join([str(c) for c in gc]), 2)


# G2B = lambda G: [int(bin(G)[0])] + [int(G[n])^int(bin(G[n+1])) for n in range(bit_length(G))-1]

# G2B = lambda G: [int(bin(G)[2])] + [int(m) ^ int(n) for m, n in zip(bin(G)[2:-1], bin(G)[3:])]



    
