# LCP Methods Benchmark

This project benchmarks different **LCP (Login Checker Problem) solution methods** including:

- Linear Search  
- Binary Search  
- Hash Table  
- Bloom Filter  
- Cuckoo Filter  

It measures the runtime for `add` (i.e. insert) and `check` (i.e. lookup) operations across varying input sizes and can generate plots for visual comparison.

## Requirements

- Python 3.7+  
- `pytest` module
- `pandas` module  
- `matplotlib` module
- `mmh3` module
- `bitarray` module

Install dependencies with:

```bash
pip install pytest
pip install pandas
pip install matplotlib
pip install mmh3
pip install bitarray
```

## Running main program

Use command `python benchmark.py <operation> <max_exp>` to run

- Operation: check, add
- Max_exp: positive integer number that corresponds to maximum number of inputs (10^max_exp)

e.g., `python benchmark.py add 5`

OR use command `python benchmark.py -plot <operation>` to plot runtime

- Operation: check, add

e.g., `python benchmark.py -plot add`

## Running unit tests

Use command `pytest` to run the unit tests
