# spmf-py
Python Wrapper for SPMF 🐍 🎁

## Information
The [SPMF](http://www.philippe-fournier-viger.com/spmf) [[1](https://github.com/LoLei/spmf-py#bibliography)] data mining Java library usable in Python.  

Essentially, this module calls the Java command line tool of SPMF, passes the user arguments to it, and parses the output.  
In addition, transformation of the data to Pandas DataFrame and CSV is possible.

In theory, all algorithms featured in SPMF are callable. Nothing is hardcoded, the desired algorithm and its parameters need to be perused in the [SPMF documentation](http://www.philippe-fournier-viger.com/spmf/index.php?link=documentation.php).

## Installation
[`pip install spmf`](https://pypi.org/project/spmf/)

## Usage
Example:  
```python
from spmf import Spmf

spmf = Spmf("PrefixSpan", input_filename="contextPrefixSpan.txt",
            output_filename="output.txt", arguments=[0.7, 5])
spmf.run()
print(spmf.to_pandas_dataframe(pickle=True))
spmf.to_csv("output.csv")
```

Output:
```
=============  PREFIXSPAN 0.99-2016 - STATISTICS =============
 Total time ~ 2 ms
 Frequent sequences count : 14
 Max memory (mb) : 6.487663269042969
 minsup = 3 sequences.
 Pattern count : 14
===================================================

      pattern sup
0         [1]   4
1      [1, 2]   4
2      [1, 3]   4
3   [1, 3, 2]   3
4   [1, 3, 3]   3
5         [2]   4
6      [2, 3]   3
7         [3]   4
8      [3, 2]   3
9      [3, 3]   3
10        [4]   3
11     [4, 3]   3
12        [5]   3
13        [6]   3
```

The usage is similar to the one described in the SPMF [documentation](http://www.philippe-fournier-viger.com/spmf/index.php?link=documentation.php).  
For all Python parameters, see the [Spmf class](https://github.com/LoLei/spmf-py/blob/master/spmf/__init__.py).  

### SPMF Arguments
The `arguments` parameter are the arguments that are passed to SPMF and depend on the chosen algorithm. SPMF handles optional parameters as an ordered list. As there are no named parameters for the algorithms, if e.g. only the first and the last parameter of an algorithm are to be used, the ones in between must be filled with `""` blank strings.  
For advanced usage examples, see [`examples`](https://github.com/LoLei/spmf-py/tree/master/examples).

### SPMF Executable
Download it from the [SPMF Website](http://www.philippe-fournier-viger.com/spmf/index.php?link=download.php).  
It is assumed that the SPMF binary `spmf.jar` is located in the same directory as `spmf-py`. If it is not, either symlink it, or use the `spmf_bin_location_dir` parameter.

### Input Formats
Either use an input file as specified by SPMF, or use one of the in-line formats as seen in [`examples`](https://github.com/LoLei/spmf-py/tree/master/examples).

### Memory
The maxmimum memory can be increased in the constructor via `Spmf(memory=n)`,
where `n` is megabyte, see SPMF's
[FAQ](http://www.philippe-fournier-viger.com/spmf/index.php?link=FAQ.php#memory).

## Background
Why? If you're in a Python pipeline, like a Jupyter Notebook, it might be cumbersome to use Java as an intermediate step. Using `spmf-py` you can stay in your pipeline as though Java is never used at all.

## Bibliography
```
Fournier-Viger, P., Lin, C.W., Gomariz, A., Gueniche, T., Soltani, A., Deng, Z., Lam, H. T. (2016).  
The SPMF Open-Source Data Mining Library Version 2.  
Proc. 19th European Conference on Principles of Data Mining and Knowledge Discovery (PKDD 2016) Part III, Springer LNCS 9853,  pp. 36-40.
```

## Disclaimer
This module has not been tested for all 184 algorithms offered in SPMF. Calling them and writing to the output file should be possible for all. Output parsing however should work for those that have outputs like the sequential pattern mining algorithms. It was not tested it with other types, some adaption of the output parsing might be necessary. If something is not working, submit an issue or create a PR yourself!
