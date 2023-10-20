def get_mmc_of_values(values: list):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = values[0]
    for value in values[1:]:
        result = (result * value) // gcd(result, value)
    
    return result

print(get_mmc_of_values(values=[2, 4, 5, 8, 12]))
