def factorial(num):
    if num == 1:
        return 1
    else:
        # recursive call to the function
        return (num*factorial(num-1))