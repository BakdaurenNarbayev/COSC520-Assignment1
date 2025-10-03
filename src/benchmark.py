# Comparison of LCP approaches

# Install pandas module to run
# pip install pandas

# use command "python benchmark.py <method> <operation> <max_exp>" to run
# method: linear_search, binary_search, hash_table, bloom_filter, cuckoo_filter
# operation: check, add
# max_exp: positive integer number that corresponds to maximum number of inputs (10^max_exp)
# e.g., python benchmark.py bloom_filter add 5

# OR use command "python benchmark.py -plot <operation>" to plot runtime
# operation: check, add
# e.g., python benchmark.py -plot add

from utils.string_generation import generate_strings
from utils.plot_generation import generate_plots

import sys
import timeit
import pandas as pd

def run_benchmark(method, operation, max_exp):
    # sizes to test
    sizes = [10 ** i for i in range(1, max_exp + 1)]  # 10, 100, 1 000, 10 000, 100 000, 1 000 000

    results = []

    for n in sizes:
        # Setup code that attempts addition of n generated strings
        setup_code = ""
        test_code = ""

        if method == "linear_search":
            setup_code = (
                "from methods.lcp_linear_search import LCPLinearSearch\n"
                "from __main__ import generate_strings\n"
                "linear_search = LCPLinearSearch()\n"
                f"current_test = generate_strings({n})\n"
                "for item in current_test:\n"
                "\tlinear_search.add(item)\n"
            )
            test_code = f"linear_search.{operation}(generate_strings(1)[0])\n"

        elif method == "binary_search":
            setup_code = (
                "from methods.lcp_binary_search import LCPBinarySearch\n"
                "from __main__ import generate_strings\n"
                "binary_search = LCPBinarySearch()\n"
                f"current_test = generate_strings({n})\n"
                "for item in current_test:\n"
                "\tbinary_search.add(item)\n"
            )
            test_code = f"binary_search.{operation}(generate_strings(1)[0])\n"

        elif method == "hash_table":
            setup_code = (
                "from methods.lcp_hash_table import LCPHashTable\n"
                "from __main__ import generate_strings\n"
                f"hash_table = LCPHashTable({n}//4)\n"
                f"current_test = generate_strings({n})\n"
                "for item in current_test:\n"
                "\thash_table.add(item)\n"
            )
            test_code = f"hash_table.{operation}(generate_strings(1)[0])\n"

        elif method == "bloom_filter":
            setup_code = (
                "from methods.lcp_bloom_filter import LCPBloomFilter\n"
                "from __main__ import generate_strings\n"
                f"bloom_filter = LCPBloomFilter({n}, 0.05)\n"
                f"current_test = generate_strings({n})\n"
                "for item in current_test:\n"
                "\tbloom_filter.add(item)\n"
            )
            test_code = f"bloom_filter.{operation}(generate_strings(1)[0])\n"

        elif method == "cuckoo_filter":
            setup_code = (
                "from methods.lcp_cuckoo_filter import LCPCuckooFilter\n"
                "from __main__ import generate_strings\n"
                f"cuckoo_filter = LCPCuckooFilter({n}, 4, 12, 500)\n"
                f"current_test = generate_strings({n})\n"
                "for item in current_test:\n"
                "\tcuckoo_filter.add(item)\n"
            )
            test_code = f"cuckoo_filter.{operation}(generate_strings(1)[0])\n"

        else:
            raise ValueError(f"Unknown method: {method}")
        
        # Run benchmark
        times = []
        for run in range(10): # run ideally 10 times to get more accurate averaged results
            print(f"Size: {n}, starting run {run}")
            t = timeit.timeit(test_code, setup=setup_code, number=1000)
            times.append(t)

        avg_time = sum(times) / len(times)
        results.append({"Size": n, "Time": avg_time})

    # Save results
    filename = f"data/{method}-{operation}-{max_exp}_results.csv"
    pd.DataFrame(results).to_csv(filename, index=False)
    print(f"Saved results to {filename}")

def plot_results(operation):
    """
        Read all *_results.csv files and plot them
    """
    import glob

    csv_files = glob.glob("data/*_results.csv")
    if not csv_files:
        print("No CSV result files found. Run benchmarks first.")
        return
    
    dataset = {}

    for file in csv_files:
        method, _operation, _ = file.split("-", 2)
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
        title=f"{operation} Runtime Comparison"
    )

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "-plot":
        operation = sys.argv[2]
        plot_results(operation)
        sys.exit(0)

    if len(sys.argv) != 4:
        print("Usage: python benchmark.py <method> <operation> <max_exp>")
        print("Example: python benchmark.py binary_search check 4")
        print("Or:      python benchmark.py -plot <method>")
    
    method = sys.argv[1]        # "linear_search", "binary_search", etc.
    operation = sys.argv[2]     # "check" or "add"
    max_exp = int(sys.argv[3]) 

    run_benchmark(method, operation, max_exp)