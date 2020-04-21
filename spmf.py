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

import pandas as pd
import os
import subprocess


class Spmf:
    def __init__(self, algorithm_name, input_filename, output_filename,
                 arguments):
        # TODO: Un-hardcode
        self.executable_dir_ = "/home/me/programs/spmf/"
        self.executable_ = "spmf.jar"
        self.agorithm_name_ = algorithm_name
        self.input_ = input_filename
        self.output_ = output_filename
        self.arguments_ = [str(a) for a in arguments]
        self.patterns_ = []

    def run(self):
        subprocess_arguments = [
            "java", "-jar",
            os.path.join(self.executable_dir_, self.executable_),
            "run",
            self.agorithm_name_,
            self.input_, self.output_]
        subprocess_arguments.extend(self.arguments_)

        subprocess.call(subprocess_arguments)

    def decode_output(self):
        # read
        lines = []
        with open(self.output_, "r") as f:
            lines = f.readlines()

        # decode
        patterns = []
        for line in lines:
            line = line.strip()
            # -1 separates itemsets
            # -2 indicates end of a sequence
            # http://data-mining.philippe-fournier-viger.com/introduction-to-sequential-rule-mining/#comment-4114
            patterns.append(line.split(" -1 "))

        self.patterns_ = patterns
        return patterns

    def to_pandas_dataframe(self):
        patterns_dict_list = []
        for pattern_sup in self.patterns_:
            pattern = pattern_sup[:-1]
            sup = pattern_sup[-1:][0]
            sup = sup[len(sup) - 1]

            patterns_dict_list.append({'pattern': pattern, 'sup': sup})

        df = pd.DataFrame(patterns_dict_list)
        return df
