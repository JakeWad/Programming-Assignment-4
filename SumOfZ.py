def add(x):
    total = 0
    
    def add_numbers(x):
        nonlocal total
        total += x
        return add
    
    add_numbers(x)  # call the inner function to add x to total
    
    return add_numbers  # return the inner function to allow chaining

z = 0
add(1)
print(z)  # Output: 1

z = 0
add(1)(2)(3)(4)(5)
print(z)  # Output: 15

z = 0
add(2)(4)(6)(8)(10)
print(z)  # Output: 30

z = 0
add(3)(1)(5)(2)(7)
print(z)  # Output: 18
