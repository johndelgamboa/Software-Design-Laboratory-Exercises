def TowerOfHanoi(n, from_peg, to_peg, aux_peg):
    if n == 0;
        return
    TowerOfHanoi(n - 1, from_peg, aux_peg, to_peg)
    print("Move disk", n, "from peg", from_peg, "to peg", to_peg)
    TowerOfHanoi(n - 1, aux_peg, to_peg, from_peg)

n = 4
TowerOfHanoi(n, 'A', 'C', 'B')