# Comparison of LCP approaches
# Install matplotlib module to run
# pip install matplotlib
# use command "python lcp_approaches" to run the unit tests

from lcp_string_generation import generate_strings

import timeit
import matplotlib.pyplot as plt

# sizes to test
sizes = [10 ** i for i in range(1, 5)]  # 10, 100, 1 000, 10 000, 100 000, 1 000 000

linear_search_check_times = []
binary_search_check_times = []
hash_table_check_times = []
bloom_filter_check_times = []
cuckoo_filter_check_times = []

linear_search_add_times = []
binary_search_add_times = []
hash_table_add_times = []
bloom_filter_add_times = []
cuckoo_filter_add_times = []

for n in sizes:
    # Setup code that attempts addition of n generated strings
    linear_search_setup_code = (
        "from lcp_linear_search import LCPLinearSearch\n"
        "from __main__ import generate_strings\n"
        "linear_search = LCPLinearSearch()\n"
        f"current_test = generate_strings({n})\n"
        "for item in current_test:\n"
        "\tlinear_search.add(item)\n"
    )

    binary_search_setup_code = (
        "from lcp_binary_search import LCPBinarySearch\n"
        "from __main__ import generate_strings\n"
        "binary_search = LCPBinarySearch()\n"
        f"current_test = generate_strings({n})\n"
        "for item in current_test:\n"
        "\tbinary_search.add(item)\n"
    )

    hash_table_setup_code = (
        "from lcp_hash_table import LCPHashTable\n"
        "from __main__ import generate_strings\n"
        f"hash_table = LCPHashTable({n}//4)\n"
        f"current_test = generate_strings({n})\n"
        "for item in current_test:\n"
        "\thash_table.add(item)\n"
    )

    bloom_filter_setup_code = (
        "from lcp_bloom_filter import LCPBloomFilter\n"
        "from __main__ import generate_strings\n"
        f"bloom_filter = LCPBloomFilter({n}, 0.05)\n"
        f"current_test = generate_strings({n})\n"
        "for item in current_test:\n"
        "\tbloom_filter.add(item)\n"
    )

    cuckoo_filter_setup_code = (
        "from lcp_cuckoo_filter import LCPCuckooFilter\n"
        "from __main__ import generate_strings\n"
        f"cuckoo_filter = LCPCuckooFilter({n}, 4, 12, 500)\n"
        f"current_test = generate_strings({n})\n"
        "for item in current_test:\n"
        "\tcuckoo_filter.add(item)\n"
    )

    # Measure check()
    linear_search_check = timeit.repeat("linear_search.check(generate_strings(1)[0])\n", setup=linear_search_setup_code, number=1000, repeat=10)
    binary_search_check = timeit.repeat("binary_search.check(generate_strings(1)[0])\n", setup=binary_search_setup_code, number=1000, repeat=10)
    hash_table_check = timeit.repeat("hash_table.check(generate_strings(1)[0])\n", setup=hash_table_setup_code, number=1000, repeat=10)
    bloom_filter_check = timeit.repeat("bloom_filter.check(generate_strings(1)[0])\n", setup=bloom_filter_setup_code, number=1000, repeat=10)
    cuckoo_filter_check = timeit.repeat("cuckoo_filter.check(generate_strings(1)[0])\n", setup=cuckoo_filter_setup_code, number=1000, repeat=10)

    # Measure add()
    linear_search_add = timeit.repeat("linear_search.add(generate_strings(1)[0])\n", setup=linear_search_setup_code, number=1000, repeat=10)
    binary_search_add = timeit.repeat("binary_search.add(generate_strings(1)[0])\n", setup=binary_search_setup_code, number=1000, repeat=10)
    hash_table_add = timeit.repeat("hash_table.add(generate_strings(1)[0])\n", setup=hash_table_setup_code, number=1000, repeat=10)
    bloom_filter_add = timeit.repeat("bloom_filter.add(generate_strings(1)[0])\n", setup=bloom_filter_setup_code, number=1000, repeat=10)
    cuckoo_filter_add = timeit.repeat("cuckoo_filter.add(generate_strings(1)[0])\n", setup=cuckoo_filter_setup_code, number=1000, repeat=10)

    linear_search_check_times.append(sum(linear_search_check)/len(linear_search_check))
    binary_search_check_times.append(sum(binary_search_check)/len(binary_search_check))
    hash_table_check_times.append(sum(hash_table_check)/len(hash_table_check))
    bloom_filter_check_times.append(sum(bloom_filter_check)/len(bloom_filter_check))
    cuckoo_filter_check_times.append(sum(cuckoo_filter_check)/len(cuckoo_filter_check))

    linear_search_add_times.append(sum(linear_search_add)/len(linear_search_add))
    binary_search_add_times.append(sum(binary_search_add)/len(binary_search_add))
    hash_table_add_times.append(sum(hash_table_add)/len(hash_table_add))
    bloom_filter_add_times.append(sum(bloom_filter_add)/len(bloom_filter_add))
    cuckoo_filter_add_times.append(sum(cuckoo_filter_add)/len(cuckoo_filter_add))

# --- Plot results ---
plt.figure(figsize=(10, 6))

plt.plot(sizes, linear_search_check_times, marker="o", label="Linear Search Check")
plt.plot(sizes, binary_search_check_times, marker="o", label="Binary Search Check")
plt.plot(sizes, hash_table_check_times, marker="o", label="Hash Table Check")
plt.plot(sizes, bloom_filter_check_times, marker="o", label="Bloom Filter Check")
plt.plot(sizes, cuckoo_filter_check_times, marker="o", label="Cuckoo Filter Check")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Number of Items (log scale)")
plt.ylabel("Time (seconds, log scale)")
plt.title("Check Runtime Analysis")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(sizes, linear_search_add_times, marker="o", label="Linear Search Add")
plt.plot(sizes, binary_search_add_times, marker="o", label="Binary Search Add")
plt.plot(sizes, hash_table_add_times, marker="o", label="Hash Table Add")
plt.plot(sizes, bloom_filter_add_times, marker="o", label="Bloom Filter Add")
plt.plot(sizes, cuckoo_filter_add_times, marker="o", label="Cuckoo Filter Add")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Number of Items (log scale)")
plt.ylabel("Time (seconds, log scale)")
plt.title("Add Runtime Analysis")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()