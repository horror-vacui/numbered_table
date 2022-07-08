import numpy as np
from tabulate import tabulate
import subprocess

# Sorry, the code has been butchered a bit. I had not had the time to make it nicely configurable for all use cases...


transpose = False
n_start = 619   # frist field; by default 1
n_mate1 = 4462 # 306
n_col = 6
# n_mate2 = 3718
# n_mate3 = 4462

# n_mate1 = 50  # nyelvtan tesztekhez
# n_col1  = 10
# n_mate2 = 0 
# n_mate3 = 0 
# transpose = True

# modulo artimetic --> multiple tables on the same page

# print(f"{n_mate1}, {n_mate2}, {np.floor((n_mate2-n_mate1)/3)+1}")
# The number of the table columns are hardcoded: 8, 3, and 1
n_row_full = np.floor((n_mate1 - n_start +1) / n_col)
n_mate1_full = n_start + n_row_full * n_col 
mate1 = np.array_split(np.arange(n_start,n_mate1_full), n_row_full)
mate1.append(np.arange(n_mate1_full, n_mate1+1))
# mate1 = np.array_split(np.arange(n_start,n_mate1+1), np.floor(n_mate1/n_col)+1)
# mate2 = np.array_split(np.arange(n_mate1+1,n_mate2+1), np.floor((n_mate2-n_mate1)/3)+1)
# mate3 = np.array_split(np.arange(n_mate2+1,n_mate3+1), np.floor((n_mate3-n_mate2)/1)+1)

# Debug only:
# for i in mate1:
#     print(i)
# print(f"{n_mate1}, {n_col}, {n_row_full}, {n_mate1_full}")

# for tbl, fn in zip([mate1, mate2, mate3], ["mate1.tex", "mate2.tex", "mate3.tex"]):
if True: # indent
    tbl = mate1
    fn = "compact_longtabu.tex"
    with open(fn,"w") as f:
        print(tabulate(tbl, tablefmt="latex", floatfmt=".0f"), file=f)

    # Now I change the tabular environment into longtblr for multi page compatibility
    # And also adding the cell borders
    n_col = len(tbl[0])
    subprocess.call(["sed", "-i", "-e", r"s/\\\\/\\\\\\hline/", 
                                  "-e", r"s/tabular/longtblr/", 
                                  # "-e", r"s/ \([0-9]\+\) / \\ts{\1} /g", --> this would cause an memory (register???) issue within tabularray/l3regex
                                  "-e", "s/{" + "r"*n_col + r"""}/[entry=none]{colspec=""" + "|X"*n_col + r"""|, width=\\linewidth}/""",
                                  fn])
