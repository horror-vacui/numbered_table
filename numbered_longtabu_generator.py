import numpy as np
from tabulate import tabulate
import subprocess

n_mate1 = 306
n_mate2 = 3718
n_mate3 = 4462

# The number of the table columns are hardcoded: 8, 3, and 1
mate1 = np.array_split(np.arange(1,n_mate1+1), np.floor(n_mate1/8)+1)
mate2 = np.array_split(np.arange(n_mate1+1,n_mate2+1), np.floor((n_mate2-n_mate1)/3)+1)
mate3 = np.array_split(np.arange(n_mate2+1,n_mate3+1), np.floor((n_mate3-n_mate2)/1)+1)

for tbl, fn in zip([mate1, mate2, mate3], ["mate1.tex", "mate2.tex", "mate3.tex"]):
    with open(fn,"w") as f:
        print(tabulate(tbl, tablefmt="latex", floatfmt=".0f"), file=f)
    # Now I change the tabular environment into longtabu for multi page compatibility
    # And also adding the cell borders
    n_col = len(tbl[0])
    subprocess.call(["sed", "-i", "-e", r"s/\\\\/\\\\\\hline/", 
                                  "-e", r"s/tabular/longtabu/", 
                                  "-e", "s/{" + "r"*n_col + r"""}/ to \\linewidth {""" + "|@{}X"*n_col + "|}/",
                                  fn])
