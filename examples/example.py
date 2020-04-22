from spmf import Spmf

# Different input formats (apart from file):

input_example_list = [
    [[1], [1, 2, 3], [1, 3], [4], [3, 6]],
    [[1, 4], [3], [2, 3], [1, 5]],
    [[5, 6], [1, 2], [4, 6], [3], [2]],
    [[5], [7], [1, 6], [3], [2], [3]]
]

input_example_list_text = [
    "w1 w1 w2 w3 w1 w3 w4 w3 w6",
    "w1 w4 w3 w2 w3 w1 w5",
    "w5 w6 w1 w2 w4 w6 w3 w2",
    "w5 w7 w1 w6 w3 w2 w3"
]

input_example_raw = """1 -1 1 2 3 -1 1 3 -1 4 -1 3 6 -1 -2
1 4 -1 3 -1 2 3 -1 1 5 -1 -2
5 6 -1 1 2 -1 4 6 -1 3 -1 2 -1 -2
5 -1 7 -1 1 6 -1 3 -1 2 -1 3 -1 -2
"""

input_example_raw_text = """w1 w1 w2 w3 w1 w3 w4 w3 w6.
w1 w4 w3 w2 w3 w1 w5.
w5 w6 w1 w2 w4 w6 w3 w2.
w5 w7 w1 w6 w3 w2 w3.
"""


# Different algorithms:

spmf = Spmf("PrefixSpan", input_filename="contextPrefixSpan.txt",
            output_filename="output.txt", arguments=[0.7, 5])


# spmf = Spmf("SPAM", input_filename="contextPrefixSpan.txt",
            # output_filename="output.txt", arguments=[0.6, "", 5])


# Different arguments:

# spmf = Spmf("PrefixSpan", input_filename="contextPrefixSpan.txt",
            # output_filename="output.txt", arguments=[1, "", True])

# spmf = Spmf("PrefixSpan", input_direct=input_example_raw,
            # output_filename="output.txt",
            # arguments=[1, "", True])

# spmf = Spmf("PrefixSpan", input_direct=input_example_raw_text,
            # input_type="text",
            # output_filename="output.txt",
            # arguments=[1, "", True])

# spmf = Spmf("PrefixSpan", input_direct=input_example_list,
            # output_filename="output.txt",
            # arguments=[1, "", True])

# spmf = Spmf("PrefixSpan", input_direct=input_example_list_text,
            # input_type="text",
            # output_filename="output.txt",
            # arguments=[1, "", True])

spmf.run()
# print(spmf.parse_output())
print(spmf.to_pandas_dataframe(pickle=True))
spmf.to_csv("output.csv")
