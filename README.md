# spmf-py
Python SPMF Wrapper 🐍 🎁

## Information
The [SPMF](http://www.philippe-fournier-viger.com/spmf) data mining Java library usable in Python.  

Essentially, this module calls the Java command line tool of SPMF, passes the user arguments to it, and parses the output.  
In addition, transformation of the data to Pandas DataFrame and CSV is possible.

In theory, all algorithms featured in SPMF are callable. Nothing is hardcoded, the desired algorithm and its parameters need to be perused in the [SPMF documentation](http://www.philippe-fournier-viger.com/spmf/index.php?link=documentation.php).

## Usage
`TODO`

It is assumed that the SPMF binary `spmf.jar` is located in the same directory as `spmf-py`. If it is not, either symlink it, or use the `spmf_bin_location_dir` parameter.
