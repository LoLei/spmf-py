"""
Python 3 Wrapper for SPMF
http://www.philippe-fournier-viger.com/spmf

Inspiration from:
https://github.com/fandu/maximal-sequential-patterns-mining
http://forum.ai-directory.com/read.php?5,5510
"""

__author__ = "Lorenz Leitner"
__version__ = "0.1.0"
__license__ = "GNU GPL v3.0"

import os
import subprocess


class Spmf:
    def __init__(self):
        # TODO: Un-hardcode
        self.executable_dir_ = "/home/me/programs/spmf/"
        self._executable = "spmf.jar"
        self._input = "input.text"
        self._output = "output.txt"

    def run(self):
        subprocess.call(["java", "-jar", os.path.join(self.executable_dir_,
            self._executable), "run", "TKS", self._input, self._output,
            str(5),
            str(4),
            str(""),
            str(""),
            str(1)
            ])

    def decode_output(self):
        # read
        lines = []
        try:
            with open(self._output, "r") as f:
                lines = f.readlines()
        except:
            print("read output error")

        # decode
        patterns = []
        for line in lines:
            line = line.strip()
            # -1 separates itemsets
            # -2 indicates end of a sequence
            # http://data-mining.philippe-fournier-viger.com/introduction-to-sequential-rule-mining/#comment-4114
            patterns.append(line.split(" -1 "))

        return patterns


if __name__ == "__main__":
    spmf = Spmf()
    # Important: Use .text extension of text data input, it will fail with .txt
    # https://www.philippe-fournier-viger.com/spmf/Using_a_TEXT_file_as_input.php
    spmf.run()
    print(spmf.decode_output())
