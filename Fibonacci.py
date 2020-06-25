def main():

    # Get user input as integer, basic error handling
    while True:
        try:
            length = int(input("Please enter Fibonacci length: "))
            break
        except:
            print("Please enter a number.")

    sequence = gen_fib_seq(length)
    print(sequence)


def gen_fib_seq(length):

    # Possible cases, length 1 returns [1]
    if length == 1:
        seq = [1]

    # Length 2 returns [1, 1]
    elif length == 2:
        seq = [1, 1]

    # Generate anything longer than 2
    else:
        seq = [1, 1]

        for x in range(length - 2):
            seq.append(seq[x] + seq[-1])

    return seq


main()
