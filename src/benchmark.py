# Comparison of LCP approaches

# Install pandas module to run
# pip install pandas

# use command "python benchmark.py <operation> <max_exp>" to run
# operation: check, add
# max_exp: positive integer number that corresponds to maximum number of inputs (10^max_exp)
# e.g., python benchmark.py add 5

# OR use command "python benchmark.py -plot <operation>" to plot runtime
# operation: check, add
# e.g., python benchmark.py -plot add

from utils.string_generation import generate_strings
from utils.plot_generation import generate_plots

import sys
import timeit
import random
import pandas as pd

def run_benchmark(operation, max_exp):
    # sizes to test
    sizes = [10 ** i for i in range(1, max_exp + 1)]  # 10, 100, 1 000, 10 000, 100 000, 1 000 000
    methods = ["Linear Search", "Binary Search", "Hash Table", "Bloom Filter", "Cuckoo Filter"]
    runs = 10 # number of runs for each size and method
    
    results = {}
    for method in methods:
        results[method] = []

    for n in sizes:
        times = {}
        for method in methods:
            times[method] = []

        for run in range(runs): # run ideally 10 times to get more accurate averaged results
            random.seed(run)

            # Generate strings once for this size
            generated_strings = generate_strings(n + 1000)
            current_test = generated_strings[: n]

            # For add benchmark, time adding all elements (new ones)
            new_items = generated_strings[n : n + 1000]

            if operation == "check":
                # For check tests, pick 500 items (or min(n, 500)) from current_test and new_items
                check_test = random.sample(current_test, min(n, 500))
                check_new_items = random.sample(new_items, min(n, 500))
                check_test.extend(check_new_items)

            for method in methods:
                if method == "Linear Search":
                    setup_code = (
                        "from methods.lcp_linear_search import LCPLinearSearch\n"
                        "from __main__ import generate_strings\n"
                        "linear_search = LCPLinearSearch()\n"
                        "for item in current_test:\n"
                        "\tlinear_search.add(item)\n"
                    )

                    if operation == "add":
                        # For add benchmark, time adding all elements (new ones)
                        test_code = "for item in new_items:\n\tlinear_search.add(item)\n"
                    else:
                        # For check benchmark, use pre-selected items
                        test_code = "for item in check_test:\n\tlinear_search.check(item)\n"

                elif method == "Binary Search":
                    setup_code = (
                        "from methods.lcp_binary_search import LCPBinarySearch\n"
                        "from __main__ import generate_strings\n"
                        "binary_search = LCPBinarySearch()\n"
                        "for item in current_test:\n"
                        "\tbinary_search.add(item)\n"
                    )

                    if operation == "add":
                        # For add benchmark, time adding all elements (new ones)
                        test_code = "for item in new_items:\n\tbinary_search.add(item)\n"
                    else:
                        # For check benchmark, use pre-selected items
                        test_code = "for item in check_test:\n\tbinary_search.check(item)\n"

                elif method == "Hash Table":
                    setup_code = (
                        "from methods.lcp_hash_table import LCPHashTable\n"
                        "from __main__ import generate_strings\n"
                        f"hash_table = LCPHashTable({n}//4)\n"
                        "for item in current_test:\n"
                        "\thash_table.add(item)\n"
                    )

                    if operation == "add":
                        # For add benchmark, time adding all elements (new ones)
                        test_code = "for item in new_items:\n\thash_table.add(item)\n"
                    else:
                        # For check benchmark, use pre-selected items
                        test_code = "for item in check_test:\n\thash_table.check(item)\n"

                elif method == "Bloom Filter":
                    setup_code = (
                        "from methods.lcp_bloom_filter import LCPBloomFilter\n"
                        "from __main__ import generate_strings\n"
                        f"bloom_filter = LCPBloomFilter({n}, 0.05)\n"
                        "for item in current_test:\n"
                        "\tbloom_filter.add(item)\n"
                    )

                    if operation == "add":
                        # For add benchmark, time adding all elements (new ones)
                        test_code = "for item in new_items:\n\tbloom_filter.add(item)\n"
                    else:
                        # For check benchmark, use pre-selected items
                        test_code = "for item in check_test:\n\tbloom_filter.check(item)\n"

                elif method == "Cuckoo Filter":
                    setup_code = (
                        "from methods.lcp_cuckoo_filter import LCPCuckooFilter\n"
                        "from __main__ import generate_strings\n"
                        f"cuckoo_filter = LCPCuckooFilter({n}, 4, 12, 500)\n"
                        "for item in current_test:\n"
                        "\tcuckoo_filter.add(item)\n"
                    )

                    if operation == "add":
                        # For add benchmark, time adding all elements (new ones)
                        test_code = "for item in new_items:\n\tcuckoo_filter.add(item)\n"
                    else:
                        # For check benchmark, use pre-selected items
                        test_code = "for item in check_test:\n\tcuckoo_filter.check(item)\n"

                else:
                    raise ValueError(f"Unknown method: {method}")
            
                # Run benchmark
                print(f"Method: {method} \t Size: {n} \t Run #{run}")
                t = timeit.timeit(
                    test_code, 
                    setup=setup_code, 
                    number=1, 
                    globals={"check_test": check_test, "new_items": new_items, "current_test": current_test}
                )
                times[method].append(t)

        for method in methods:
            avg_time = sum(times[method]) / runs
            results[method].append({"Size": n, "Time": avg_time})

    for method in methods:
        # Save results
        filename = f"data/{method}-{operation}-{max_exp}-results.csv"
        pd.DataFrame(results[method]).to_csv(filename, index=False)
        print(f"Saved results to {filename}")

def plot_results(operation):
    """
        Read all *_results.csv files and plot them
    """
    import glob

    csv_files = glob.glob("data/*-results.csv")
    if not csv_files:
        print("No CSV result files found. Run benchmarks first.")
        return
    
    dataset = {}

    for file in csv_files:
        method, _operation, _, _ = file.split("-", 3)
        _, method = method.split("\\", 1)
        if _operation != operation:
            continue
        df = pd.read_csv(file)
        dataset[method] = df

    if len(dataset) == 0:
        print("No CSV result files found. Run benchmarks for that method first or check correctness of method name.")
        return
    
    y = []
    labels = []
    for method in dataset:
        x = dataset[method]["Size"].to_list()
        y.append(dataset[method]["Time"].to_list())
        labels.append(method)

    generate_plots(
        x,
        y,
        labels,
        title=f"{operation.title()} Runtime Comparison"
    )

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python benchmark.py <operation> <max_exp>")
        print("Example: python benchmark.py binary_search check 4")
        print("Or:      python benchmark.py -plot <method>")
        sys.exit(1)
    
    if sys.argv[1] == "-plot":
        operation = sys.argv[2]
        plot_results(operation)
        sys.exit(0)
    
    operation = sys.argv[1] # "check" or "add"
    max_exp = int(sys.argv[2]) 

    run_benchmark(operation, max_exp)