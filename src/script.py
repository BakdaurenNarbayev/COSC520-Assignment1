###----------------------- Algorithms -----------------------###
'''
Each takes a sequence of strings in input order and 
returns a sequence of string (e.g., login) checking results.
For example, if input_sequence = [str1, str2, str3], 
where str1 and str2 are included as logins, but str3 is not, 
then the output sequence is [0, 0, 1].
'''

# Checkes if an input exists in a list linearly and 
# adds the input to the end of the list if it does not exist
def linear_search(input_sequence):
    # TODO: Implement efficiently
    included_input_sequence = [] # current list of included inputs
    output_sequence = [] # current output sequence, where 0 indicates new input inclusion, i.e. this input did not exist before in the list
    is_included = False # indicates if current input has already been included to the list

    for i in range(len(input_sequence)): # going through all inputs
        for j in range(len(included_input_sequence)): # for each input, check if it is already included
            is_included = False
            if (included_input_sequence[j] == input_sequence[i]): # if it is included, output for this input is 1
                is_included = True
                output_sequence.append(1)
                break

        if (not is_included): # if none of the included inputs so far is equal to current input, then add it to the list
            included_input_sequence.append(input_sequence[i])
            output_sequence.append(0)

    return output_sequence

def binary_search(input_sequence):
    # TODO: Implement efficiently
    # TODO: Do I need to consider other data structures?
    return None

def hashing(input_sequence):
    # TODO: Implement efficiently
    return None

def bloom_filter(input_sequence):
    # TODO: Implement efficiently
    return None

def Cuckoo_filter(input_sequence):
    # TODO: Implement efficiently
    return None



###----------------------- Comparison -----------------------###

def generate_strings():
    # TODO: 1 billion
    return None

def compare_algorithms():
    # TODO: Draw a plot as N grows
    # TODO: Many randomized runs?
    return None

def unit_test(algorithm):
    # TODO: More tests
    # TODO: Add runtime
    # TODO: Insertion, lookup, deletion
    # TODO: check Unit test module
    # Test #1
    test1 = [chr(ord("a") + i) for i in range(26)] # i.e., ["a", "b", "c", ..., "x", "y", "z"]
    if (algorithm == "linear_search"):
        if (linear_search(test1) == [0 for i in range(len(test1))]):
            print("Test #1 for " + algorithm + " is successful!")
        else :
            print("Test #1 for " + algorithm + " FAILED!")
    return None



###----------------------- Main -----------------------###

def main():
    # TODO: Run unit tests on algorithms
    unit_test("linear_search")

if __name__ == "__main__":
    main()