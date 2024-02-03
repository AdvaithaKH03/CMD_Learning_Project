def entry_prompt():
    print("Integers laws explanation program")

def law_1():
    name = "Closure Property"
    define_1 = "Defination = The product of two integers is always an integer"
    a = 2
    b = 4
    for_1 = a * b 
    return name, define_1, a, b, for_1

result_1, result_2, result_3, result_4, result_5 = law_1()


def law_2():
    name = "Commutative Property"
    define_1 = "Defination = The numbers on which we operate can be moved or swapped from their position without making any difference to the answer"
    a = 4
    b = 2
    for_1 = a * b 
    for_2 = b * a
    return name, define_1, a, b, for_1, for_2

result_6, result_7, result_8, result_9, result_10, result_11 = law_2()


def law_3():
    name = "Associative Property"
    define_1 = "Defination =  When you are adding or multiplying three or more numbers, the result will be the same regardless of how you group them"
    a = 4
    b = 2
    c = 6
    for_1 = (a * b) * c
    for_2 = b * (c * a) 
    return name, define_1, a, b, c, for_1, for_2

result_12, result_13, result_14, result_15, result_16, result_17, result_18 = law_3()

def law_4():
    name = "Distributive Property"
    define_1 = "Defination =  Distributive property means dividing the given operations on the numbers so that the equation becomes easier to solve."
    example_1 = "3( 2 + 4) = 3 (6) = 18"
    example_2 ="3( 2 + 4) = 3 x 2 + 3 x 4 = 6 + 12 = 18"
                    
    return name, define_1, example_1, example_2

result_19, result_20, result_21, result_22 = law_4()


