def gen_values(n):
    for i in range(n):
        yield i


def prime_gen(n):
    for prime in range(n):
        if prime < 2:
            continue
        is_prime = True

        for i in range(2, int(prime ** 0.5) + 1):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            yield prime


def main():
    gen_object = gen_values(10)
    # Here when we call the function it doesn't return directly the value
    # instead it returns a generator object:
    print(gen_object)
    # this gen object is like a machine that knows how to produce values
    # But it doesn't produce any value untill we ask it to

    # So to acess these values we need to ask for them using the function:
    print(next(gen_object))
    # This functions allows the main program to control where to begin
    # and where to resumes the execution, it's like : it gets us
    # the first value then pushes the the starting point to the next value
    # So we can say it makes the program executes the code untill it reaches
    # the key word yield, returns it and wait untill it's called again, so
    # It executes untill the it finds another yield key word and return it

    for _ in range(9):
        print(next(gen_object), end=' ')

    print()
    # if we dont know where to stop, we can cause a stopiteration error,
    # That's why we have a way that detects automatically where to stiop :
    # We can just iterate directly on the returned values like this:
    for value in gen_values(10):
        print(value, end=' ')

    print()

    for prime in prime_gen(10):
        print(prime, end=' ')

    print()

    # if it happens that we want to store all the values of the gen_object,
    # So that we can access them later, we can just cast the gen object to
    # a list :
    primes = list(prime_gen(10))
    print(primes)


main()
