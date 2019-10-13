k = 10

sums_of_first_k_odds = [ sum(range(1, 2*i+2, 2)) for i in range(k)]

perfect_squares = sums_of_first_k_odds

print(perfect_squares)

perfect_squares.insert(0,0)

print(sums_of_first_k_odds)