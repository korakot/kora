"""
My improvement to NLTK for Colab
"""
import os
from IPython.display import display, HTML

os.system("pip install nltk -U")  # 3.2.5 -> 3.5
from nltk import *                # replacement


def _print_concordance(self, word, width=80, lines=25):
    concordance_list = self.find_concordance(word, width=width)

    if not concordance_list:
        print("no matches")
    else:
        lines = min(lines, len(concordance_list))
        print("Displaying {} of {} matches:".format(lines, len(concordance_list)))
        html = "<table>\n"
        rep = f"<font color='green'>{word}</font>"
        for i, concordance_line in enumerate(concordance_list[:lines]):
            row = f"""
              <tr>
                <td>{concordance_line.left_print.replace(word, rep)}</td>
                <td>{rep}</td>
                <td>{concordance_line.right_print.replace(word, rep)}</td>
              </tr>
            """
            html += row
        html += "<style>td:first-child {text-align: right}</style>"
        display(HTML(html))

ConcordanceIndex.print_concordance = _print_concordance
