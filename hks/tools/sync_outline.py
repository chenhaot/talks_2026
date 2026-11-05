#!/usr/bin/env python3
"""Regenerate talk.md from the presentation's visible content and speaker notes.

Run after applying reviewed outline edits to talk.html:
    python3 tools/sync_outline.py
Use --check to verify that the two files match without changing either file.
"""
from pathlib import Path
import argparse
import json
import re
from lxml import html

ROOT = Path(__file__).resolve().parents[1]

def text(node):
    return re.sub(r'\s+', ' ', node.text_content()).strip()

def render(node):
    tag = node.tag
    cls = set(node.get('class', '').split())
    if 'equation' in cls and node.get('aria-label'):
        return '\n\n' + node.get('aria-label') + '\n\n'
    if cls & {'long-arrow', 'vertical-arrow', 'converging', 'xray-mark'}:
        return ''
    if tag == 'img':
        return f'\n\n![{node.get("alt", "")} ]({node.get("src")})\n\n'.replace(' ](', '](')
    if tag == 'table':
        rows = [[text(c).replace('|', '\\|') for c in row] for row in node.xpath('.//tr')]
        if not rows:
            return ''
        return '\n\n' + '\n'.join(['| ' + ' | '.join(rows[0]) + ' |', '| ' + ' | '.join(['---'] * len(rows[0])) + ' |'] + ['| ' + ' | '.join(row) + ' |' for row in rows[1:]]) + '\n\n'
    inner = (node.text or '') + ''.join(render(child) + (child.tail or '') for child in node)
    if tag == 'br':
        return '\n'
    parent_classes = set(node.getparent().get('class', '').split()) if node.getparent() is not None else set()
    if tag == 'small' or (tag == 'span' and parent_classes & {'map-understanding', 'map-shaping', 'paradox-stat', 'learning-objectives', 'native-chart-labels'}):
        return '\n' + inner.strip() + '\n'
    if tag in ('strong', 'b'):
        return '**' + inner.strip() + '**'
    if tag == 'a':
        return '[' + inner.strip() + '](' + node.get('href', '') + ')'
    if tag == 'blockquote':
        return '\n\n> ' + re.sub(r'\s+', ' ', inner).strip() + '\n\n'
    if tag == 'li':
        return '\n- ' + inner.strip() + '\n'
    if tag in ('div', 'p', 'figure', 'figcaption', 'ol', 'ul'):
        return '\n\n' + inner.strip() + '\n\n'
    return inner

def generate():
    doc = html.parse(str(ROOT / 'talk.html'))
    sections = doc.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," slides ")]/section')
    intro = '''# Towards Human-centered AI

Understanding and Shaping Human Decisions with AI

Chenhao Tan · Chicago Human+AI Lab

Presentation: `talk.html` · PDF: `talk.pdf`. Arrow keys navigate; F opens full screen; S opens speaker notes; Cmd/Ctrl+P opens the PDF layout. Runtime assets and fonts are local.

All slide text and the workload–fatigue diagrams use native HTML. Images are isolated figures, charts, and photographs; there are no whole-slide screenshots. The visible slide content, figures, references, and speaker notes below are synchronized from `talk.html` by `python3 tools/sync_outline.py`.

The testing-yield result uses the published **19%** estimate. Earlier physician-study analyses are labeled. The race analysis is exploratory and comes from the earlier preprint. The pneumonia experiment uses lay participants; **13.2 percentage points** is the improvement over random supporting examples.

'''
    output = [intro]
    for i, section in enumerate(sections, 1):
        heading = section.xpath('.//h1|.//h2')
        title = section.get('data-title') or (text(heading[0]) if heading else {2: 'An Overview of My Research', 3: 'Today: Healthcare and Explanations', 4: 'Policy outcomes hinge on human decisions'}.get(i, f'Slide {i}'))
        notes = section.xpath('.//aside[contains(@class,"notes")]')
        note_text = '\n\n'.join(text(n) for n in notes)
        refs = section.xpath('.//*[contains(concat(" ", normalize-space(@class), " "), " slide-references ")]')
        reference = '\n\n'.join(render(r).strip() for r in refs)
        for node in notes + refs + section.xpath('.//div[contains(concat(" ",normalize-space(@class)," ")," act-header ")]'):
            node.getparent().remove(node)
        if i == 1:
            for h in section.xpath('.//h1'):
                h.getparent().remove(h)
        body = render(section).strip()
        body = re.sub(r'\n[ \t]+', '\n', body)
        body = re.sub(r'\n{3,}', '\n\n', body)
        output.append(f'## Slide {i} — {title}\n\n{body}\n\n')
        if reference:
            output.append(f'Source: {reference}\n\n')
        if section.get('data-source'):
            output.append(f'PowerPoint source: `{section.get("data-source")}`\n\n')
        if section.get('data-builds'):
            builds = json.loads(section.get('data-builds'))
            output.append('Animation builds:\n\n' + '\n'.join(f'{j}. {step}' for j, step in enumerate(builds, 1)) + '\n\n')
        if note_text:
            output.append(f'Speaker notes: {note_text}\n\n')
    return ''.join(output).rstrip() + '\n'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = generate()
    target = ROOT / 'talk.md'
    if args.check:
        if target.read_text() != result:
            raise SystemExit('talk.md is out of sync; run python3 tools/sync_outline.py')
        print('talk.md matches talk.html')
    else:
        target.write_text(result)
        print('Updated talk.md from talk.html')
