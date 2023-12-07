def generate_pascals_triangle(numRows):
    if numRows == 0:
        return []
    
    pascals_triangle = [[1]]
    
    for i in range(1, numRows):
        prev_row = pascals_triangle[-1]
        new_row = [1]
        
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)
        pascals_triangle.append(new_row)
    
    return pascals_triangle


test_cases = [5, 1]

for numRows in test_cases:
    result = generate_pascals_triangle(numRows)
    print(f"Pascal's triangle for numRows = {numRows}:")
    print(result)
    print()





