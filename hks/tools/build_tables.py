#!/usr/bin/env python3
"""Compile the LaTeX tables used in talk.html into PNG figures.

The table style follows the LaTeX source of Hsu, Obermeyer, and Tan
(arXiv:2312.03077): booktabs rules, Computer Modern, coefficients with standard
errors underneath, bold "Controls" blocks, and significance stars as
superscripts. Numbers follow the published Nature Communications version.

Each table can have highlight steps. Step 0 is the plain table; step k draws a
red box around the cells tagged with step k. The layout is identical across
steps, so the slides stack the images and fade in later steps as fragments.

    python3 tools/build_tables.py
"""
from pathlib import Path
import json
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'resources'
DPI = 300
# All tables share one display scale so their text renders at the same size.
SCALE = 0.62

PREAMBLE = r"""
\documentclass[border=10pt]{standalone}
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{calc}
\definecolor{boxred}{HTML}{C00000}
\newcount\activestep
\activestep=STEP
\newcommand{\sig}[1]{$^{#1}$}
% \st{coef}{se}: coefficient with its standard error underneath.
\newcommand{\st}[2]{\begin{tabular}[t]{@{}c@{}}#1\\(#2)\end{tabular}}
% \hl{step}{content}: box a single cell.
\newcommand{\hl}[2]{\begin{tikzpicture}[baseline=(X.base)]
  \node[inner sep=0pt,outer sep=0pt](X){#2};
  \ifnum\activestep=#1 \draw[overlay,boxred,line width=1.3pt]
    ($(X.south west)+(-5pt,-4pt)$) rectangle ($(X.north east)+(5pt,4pt)$);\fi
\end{tikzpicture}}
% Boxes spanning several cells: \tl{name} marks the top left, \br{name} the
% bottom right of a one-line cell, \brs{name} of a coefficient/SE cell.
\newcommand{\tl}[1]{\tikz[remember picture,overlay]\coordinate(#1-tl) at (-6pt,2.6ex);}
\newcommand{\br}[1]{\tikz[remember picture,overlay]\coordinate(#1-br) at (6pt,-1.1ex);}
\newcommand{\brs}[1]{\tikz[remember picture,overlay]\coordinate(#1-br) at (6pt,-16.7pt);}
% Tighter variants for smaller outlines.
\newcommand{\tlt}[1]{\tikz[remember picture,overlay]\coordinate(#1-tl) at (-3pt,2.3ex);}
\newcommand{\brst}[1]{\tikz[remember picture,overlay]\coordinate(#1-br) at (3pt,-15pt);}
\newcommand{\rowbox}[2]{\ifnum\activestep=#1 \tikz[remember picture,overlay]
  \draw[boxred,line width=1.3pt] (#2-tl) rectangle (#2-br);\fi}
\begin{document}
"""

STARS = r'\multicolumn{%d}{@{}l}{$p<0.05^{*}, p<0.01^{**}, p<0.001^{***}$}'

CONTROLS_9 = r"""
\textbf{Controls} & %(blank)s \\
\hspace{1em} Time of day & %(tod)s \\
\hspace{1em} Day of week & %(rest)s \\
\hspace{1em} Week of year & %(rest)s \\
\hspace{1em} Year & %(rest)s \\
\hspace{1em} Demographics & %(all)s \\
\hspace{1em} Chief complaint & %(all)s \\
\hspace{1em} Physician & %(all)s \\
\hspace{1em} Length of stay & %(all)s \\
\hspace{1em} Insurance type & %(all)s \\
"""

YIELD = r"""
\begin{tabular}{@{}lcc@{}}
\toprule
 & Effect of workload & Effect of predicted fatigue \\
 & on yield of testing & on yield of testing \\
\midrule
Coefficient & \hl{1}{\st{$-0.0081$}{0.009}} & \hl{2}{\st{$-0.2935$\sig{*}}{0.147}} \\
\addlinespace
""" + CONTROLS_9 % dict(blank='&', tod='YES & YES', rest='YES & YES', all='YES & YES') + r"""
\bottomrule
\multicolumn{3}{@{}l}{$n=1{,}017$; $p<0.05^{*}$}
\end{tabular}
"""

RACE = r"""
\begin{tabular}{@{}lcc@{}}
\toprule
 & Workload (Day) & Predicted Fatigue \\
\midrule
Race (vs.\ White) & & \\
\hspace{1em} Black & \tlt{w}\st{$-0.0009$}{0.017} & \tlt{g}\st{0.0112\sig{***}}{0.001} \\
\hspace{1em} Hispanic & \st{$-0.0125$}{0.018}\brst{w} & \st{0.0192\sig{***}}{0.001}\brst{g} \\
\hspace{1em} Other & \st{$-0.0213$}{0.027} & \st{0.0086\sig{***}}{0.002} \\
\addlinespace
Female (vs.\ Male) & \st{0.0041}{0.015} & \st{$-0.003$\sig{**}}{0.001} \\
\addlinespace
Age & \st{0.0006}{0} & \st{$-0.0003$\sig{***}}{0.00003} \\
\addlinespace
Intercept & \st{3.2354\sig{***}}{0.084} & \st{0.569\sig{***}}{0.005} \\
\addlinespace
\textbf{Controls} & & \\
\hspace{1em} Time of day & YES & YES \\
\hspace{1em} Day of week & YES & YES \\
\hspace{1em} Week of year & YES & YES \\
\hspace{1em} Year & YES & YES \\
\hspace{1em} Chief complaint & YES & YES \\
\hspace{1em} Physician & YES & YES \\
\bottomrule
""" + STARS % 3 + r"""
\end{tabular}
\rowbox{1}{w}\rowbox{2}{g}
"""

FEATURES = r"""
\begin{tabular}{@{}lc@{}}
\toprule
Feature & Correlation with \\
 & physician workload \\
\midrule
\tl{a}\textbf{Word Un-predictability} & \\
\hspace{1em} Perplexity (log) & $-0.092$\sig{***}\br{a} \\
\addlinespace
\tl{b}\textbf{Cognitive words (LIWC)} & \\
\hspace{1em} Insight (fraction) & $-0.09$\sig{***} \\
\hspace{1em} Certainty (fraction) & 0.075\sig{***}\br{b} \\
\addlinespace
\textbf{Pronouns (LIWC)} & \\
\hspace{1em} First person singular pronouns (fraction) & $-0.07$\sig{***} \\
\hspace{1em} Impersonal pronouns (fraction) & $-0.049$\sig{***} \\
\addlinespace
\textbf{Affect (LIWC)} & \\
\hspace{1em} Anger (fraction) & 0.025\sig{***} \\
\addlinespace
\textbf{Readability} & \\
\hspace{1em} Flesch-Kincaid grade & $-0.05$\sig{***} \\
\bottomrule
\multicolumn{2}{@{}l}{$p<0.001^{***}$}
\end{tabular}
\rowbox{1}{a}\rowbox{2}{b}
"""

AUC = r"""
\begin{tabular}{@{}lc@{}}
\toprule
Input / method & AUC-ROC (\%) \\
\midrule
Chief complaint baseline & 50.0 \\
Zero-shot Vicuna-7B & 53.2 \\
\textbf{Clinical note features} & \textbf{60.1} \\
\bottomrule
\end{tabular}
"""


def table1(external):
    cols = 5 if external else 4
    spec = 'l' + 'c' * cols
    head = [r' & (1) & (2) & (3) & (4)' + (r' & (5)' if external else '') + r' \\',
            r' & \multicolumn{4}{c}{\emph{Hospital Dataset}}' + (r' & \emph{Ext. Validation}' if external else '') + r' \\',
            r'\cmidrule(lr){2-5}' + (r'\cmidrule(l){6-6}' if external else ''),
            r' & Workload & Overnight & Variation in Shift - & Patients' + (r' & Overnight' if external else '') + r' \\',
            r' & (Day) & Shift & Start-Time & Seen Prior' + (r' & Shift' if external else '') + r' \\']
    fat = [r'\st{0.384\sig{***}}{0.087}', r'\st{0.041\sig{*}}{0.018}', r'\st{5.606\sig{*}}{2.265}', r'\st{1.073\sig{***}}{0.298}']
    icp = [r'\st{3.072\sig{***}}{0.102}', r'\st{0.158\sig{***}}{0.019}', r'\st{29.855\sig{***}}{2.669}', r'\st{9.011\sig{***}}{0.352}']
    if external:
        fat.append(r'\hl{1}{\st{0.364\sig{*}}{0.162}}')
        icp.append(r'\st{$-0.239$}{0.288}')
    else:
        fat[0] = r'\tl{f}' + fat[0]
        fat[3] = fat[3] + r'\brs{f}'
    yes = ' & '.join(['YES'] * cols)
    ctrl = CONTROLS_9 % dict(
        blank='& ' * (cols - 1),
        tod='YES & NO & YES & YES' + (' & YES' if external else ''),
        rest='YES & YES & YES & YES' + (' & N/A' if external else ''),
        all=yes)
    body = '\n'.join([r'\begin{tabular}{@{}%s@{}}' % spec, r'\toprule', *head, r'\midrule',
                      'Fatigue & ' + ' & '.join(fat) + r' \\', r'\addlinespace',
                      'Intercept & ' + ' & '.join(icp) + r' \\', r'\addlinespace',
                      ctrl, r'\bottomrule', STARS % (cols + 1), r'\end{tabular}'])
    if not external:
        body += r'\rowbox{1}{f}'
    return body


SANITY = r"""
\begin{tabular}{@{}lccc@{}}
\toprule
 & Is Female & Is White & Age \\
\midrule
Workload & \st{$-0.0055$}{0.006} & \st{$-0.0023$}{0.006} & \st{$-0.1562$}{0.189} \\
\addlinespace
Intercept & \st{0.5694\sig{***}}{0.029} & \st{0.4724\sig{***}}{0.03} & \st{40.333\sig{***}}{0.961} \\
\addlinespace
\textbf{Controls} & & & \\
\hspace{1em} Time of day & YES & YES & YES \\
\hspace{1em} Day of week & YES & YES & YES \\
\hspace{1em} Week of year & YES & YES & YES \\
\hspace{1em} Year & YES & YES & YES \\
\hspace{1em} Chief complaint & YES & YES & YES \\
\hspace{1em} Physician & YES & YES & YES \\
\bottomrule
""" + STARS % 4 + r"""
\end{tabular}
"""

AI_NOTES = r"""
\begin{tabular}{@{}lc@{}}
\toprule
Text source & Score deviation from mean \\
\midrule
Greedy generation & $+189\%$ \\
Sampled generation & $+8\%$ \\
Original History of Present Illness & $-66\%$ \\
\bottomrule
\end{tabular}
"""

TABLES = {
    'table-yield': (YIELD, 2),
    'table-race': (RACE, 2),
    'table-features': (FEATURES, 2),
    'table-auc': (AUC, 0),
    'table-fatigue-hospital': (table1(False), 1),
    'table-fatigue-mimic': (table1(True), 1),
    'table-sanity': (SANITY, 0),
    'table-ai-notes': (AI_NOTES, 0),
}


def build(name, body, step, workdir):
    stem = f'{name}-{step}' if step else name
    tex = workdir / f'{stem}.tex'
    tex.write_text(PREAMBLE.replace('STEP', str(step)) + body + '\n\\end{document}\n')
    for _ in range(2):  # second pass resolves remember-picture coordinates
        subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', tex.name],
                       cwd=workdir, check=True, stdout=subprocess.DEVNULL)
    subprocess.run(['pdftoppm', '-png', '-r', str(DPI), '-singlefile', f'{stem}.pdf',
                    str(OUT / stem)], cwd=workdir, check=True)
    print('wrote', (OUT / f'{stem}.png').relative_to(ROOT))


def display_sizes():
    """CSS widths that give every table the same text size on the slides."""
    from PIL import Image
    return {name: round(Image.open(OUT / f'{name}.png').size[0] * SCALE) for name in TABLES}


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tmp:
        for name, (body, steps) in TABLES.items():
            for step in range(steps + 1):
                build(name, body, step, Path(tmp))
    print(json.dumps(display_sizes(), indent=1))
