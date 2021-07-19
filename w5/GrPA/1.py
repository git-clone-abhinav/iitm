def perfect_number(num):
    if num == 1 :
        return False
    divisors = [i for i in range(2,num) if num % i == 0]
    return sum(divisors) == num-1