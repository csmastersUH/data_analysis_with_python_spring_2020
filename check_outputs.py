import nbformat
import sys

inputnb = "src/project_notebook_sequence_analysis.ipynb"

nb = nbformat.read(inputnb, as_version=4)

__name__ = sys.argv[0]

for cell in nb.cells:
    if cell.cell_type == "code":
        exec(cell.source)
