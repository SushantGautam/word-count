from collections import Counter
from typing import Dict, Sequence
from pathlib import Path
import json
import argparse


def count_words(text: str) -> Dict[str, int]:
    """Count the number of times each word appears in a
    file and save the 10 most common words.
    """
    delimiters = ". , ; : ? $ @ ^ < > # % ` ! * - = ( ) [ ] { } / \" '".split()

    counts = Counter()

    for line in text.split("\n"):

        # replace all delimiters with spaces
        for delimiter in delimiters:
            line = line.replace(delimiter, " ")

        counts.update(line.split())

    # grab the 10 most common words
    return dict(counts.most_common(10))

import glob 
from os.path import basename
import matplotlib.pyplot as plt
from plot import plot

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=count_words.__doc__)
    parser.add_argument("--path", type=Path, required=True)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = vars(parser.parse_args(argv))
    all_files_in_dir =  glob.glob(str(args["path"]) + '/*.txt')
    #import basename#
    for file in all_files_in_dir:
        file_obj = open(file, "r")
        counts = count_words(file_obj.read())
        output_file = args["output"] / (basename(file).split(".")[0] + ".png")
        # create if not path exist
        output_file.parent.mkdir(parents=True, exist_ok=True)
        plot(counts, output_file)



    # output = json.dumps(counts_all, indent=4)
    # print(output)

    # # save the output
    # if args["output"] is not None:
    #     args["output"].parent.mkdir(parents=True, exist_ok=True)
    #     args["output"].write_text(output)

    # return 0


if __name__ == "__main__":
    raise SystemExit(main())
