import sys

def is_free(span, line):
    for s in line:
        if (span[1] <= s[0]): continue
        if (span[0] >= s[1]): continue
        return False
    return True


line_num = 0
lines = []

for line in sys.stdin:
    line = line.rstrip('\n')
    if len(line) == 0:
        break

    line_spans = []
    span_start = None
    span_contents = None

    if line_num % 2 == 0:
        for i, c in enumerate(line):
            if span_start is None:
                if c in ('-', '|'):
                    span_start = i
            else:
                if c not in ('-', '|'):
                    line_spans.append((span_start, i-1, None))
                    span_start = None
        if span_start is not None:
            line_spans.append((span_start, len(line)-1, None))
    else:
        span_start = 0
        span_contents = []
        for i, c in enumerate(line):
            if i == 0:
                continue

            if c == '|':
                if len(span_contents) > 0:
                    line_spans.append((span_start, i, ''.join(span_contents)))
                span_contents = []
                span_start = i
            else:
                span_contents.append(c)
        if len(span_contents) > 0:
            line_spans.append((span_start, len(line), ''.join(span_contents)))

    lines.append(line_spans)

    line_num += 1


table_width = 0
for line in lines:
    for span in line:
        table_width = max(table_width, span[1])

nlines = []
empty_spans = {}
for i, line in enumerate(lines):
    if i % 2 == 0:
        nlines.append(map(list, line))
    else:
        nline = []
        for span in line:
            inside = span[0:2] in empty_spans
            if inside:
                nline.append(['empty', span[0], span[1]])
                empty_spans[span[0:2]][3] += 1
                if not is_free(span[0:2], lines[i+1]):
                    del empty_spans[span[0:2]]
            else:
                foo = ['text', span[0], span[1], 1, span[2].strip()]
                nline.append(foo)
                if is_free(span[0:2], lines[i+1]):
                    empty_spans[span[0:2]] = foo
        nlines.append(nline)

cur_index = 0
while cur_index <= table_width:
    min_num = 9999
    for i, line in enumerate(nlines):
        if i % 2 == 0:
            for span in line:
                if span[1] - span[0] > 0:
                    if span[0] >= cur_index: min_num = min(min_num, span[0])
                    if span[1] >= cur_index: min_num = min(min_num, span[1])
        else:
            for span in line:
                if span[1] >= cur_index: min_num = min(min_num, span[1])
                if span[2] >= cur_index: min_num = min(min_num, span[2])
    for i, line in enumerate(nlines):
        if i % 2 == 0:
            for span in line:
                if span[0] == min_num: span[0] = cur_index
                if span[1] == min_num: span[1] = cur_index
        else:
            for span in line:
                if span[1] == min_num: span[1] = cur_index
                if span[2] == min_num: span[2] = cur_index


    cur_index += 1

table_width = 0
for line in nlines:
    for span in line:
        table_width = max(table_width, span[1])

latex_lines = ['\\begin{tabular}{|' + 'c|'*table_width + '}']
for i, line in enumerate(nlines):
    if i % 2 == 0:
        if len(line) == 1 and tuple(line[0][0:2]) == (0, table_width):
            latex_lines.append("\\hline")
        else:
            lline = []
            for span in line:
                if span[1] > span[0]:
                    lline.append("\\cline{%d-%d}" % (span[0]+1, span[1]))
            latex_lines.append(''.join(lline))
    else:
        cl = []
        for span in line:
            l = span[2] - span[1]
            if span[0] == 'empty':
                if l > 1:
                    cl.append('\\multicolumn{%d}{|c|}{} ' % (l,))
                else:
                    cl.append('')
            elif span[0] == 'text':
                t = ""
                if l > 1:
                    t += '\\multicolumn{%d}{|c|}{' % (l,)
                if span[3] > 1:
                    t += '\\multirow{%d}{*}{' % (span[3],)
                t += span[4]
                if span[3] > 1:
                    t += '}'
                if l > 1:
                    t += '}'
                t += ' '
                cl.append(t)
        latex_lines.append('& '.join(cl) + ' \\\\')

latex_lines.append('\\end{tabular}')


for i in latex_lines:
    print i
