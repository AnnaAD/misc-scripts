import json

# Sample JSON string


# Parse the JSON data
f = open("calendar.json", "r")
data = json.loads(f.read())

from datetime import datetime


events = [(item['start']['date'] if 'date' in item['start'] else item['start']['dateTime'][:10], item['summary']) for item in data['items'] if "start" in item]
events.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))

# Generate LaTeX table snippet
latex_table = """
\\definecolor{arch}{HTML}{90e8a7}
\\definecolor{asm}{HTML}{90bbe8}
\\definecolor{c}{HTML}{e8bf90}
\\definecolor{improve}{HTML}{c890e8}
\\begin{tabular}{|c|l|}
\\hline
\\rowcolor{lightgray} \\bf{Date} & \\bf{Summary} \\\\ 
\\hline
"""

unit1 = (1,7)
unit2 = (8,14)
unit3 = (15,20)
unit4 = (21,27)

colors = ["\\rowcolor{arch}", "\\rowcolor{asm}","\\rowcolor{c}", "\\rowcolor{improve}"]
units = {
    0:"L1 L2 L3 L4 L5 L6 L7",
    1: "L8 L9 L10 L11 L12 L13 L14",
    2: "L15 L16 L17 L18 L19 L20",
    3: "L21 L22 L23 L24 L25 L26 L27"
}

for date, summary in events:
    if(summary == "Lecture"):
        continue
    color = ""

    for key in units:
        for l in units[key].split(" "):
            if l in summary:
                color = colors[key]
    
    font = ""
    if "Due" in summary:
        font = "\\color{red}"
    
    if "Exam" in summary and "L" not in summary:
        font = "\\bf{}"

    latex_table += f"{color} {date} & {font} {summary} \\\\\n\\hline\n"

latex_table += "\\end{tabular}"

# Output the LaTeX table
print(latex_table)
