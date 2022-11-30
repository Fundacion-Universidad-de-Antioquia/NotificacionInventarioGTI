# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

from reportlab.pdfbase.pdfmetrics import stringWidth
#from textwrap import wrap
import textwrap, re

lead_re = re.compile(r'(^\s+)(.*)$') 

def justifyCenter(string, font, size, charspace):
    width = stringWidth(string, font, size)
    width += (len(string) - 1) * charspace
    return width

# def justify(text):
#     wraped_text = "\n".join(wrap(text, 80)) # 80 is line width
#     return wraped_text

def items_len(l): 
    return sum([ len(x) for x in l] )

def justify(text):
    
    wraped_text = align_paragraph(text,width=100,debug=0)
    #wraped_text = textwrap.fill(text, 100) # 80 is line width
    return wraped_text

def align_string(s, width, last_paragraph_line=0): 
    ''' 
    align string to specified width  
    ''' 
    # detect and save leading whitespace 
    m = lead_re.match(s)  
    if m is None: 
        left, right, w = '', s, width 
    else: 
        left, right, w = m.group(1), m.group(2), width - len(m.group(1)) 
 
    items = right.split() 
 
    # add required space to each words, exclude last item 
    for i in range(len(items) - 1): 
        items[i] += ' ' 
 
    if not last_paragraph_line: 
        # number of spaces to add 
        left_count = w - items_len(items) 
        while left_count > 0 and len(items) > 1: 
            for i in range(len(items) - 1): 
                items[i] += '  ' 
                left_count -= 1 
                if left_count < 1:   
                    break 
 
    res = left + ''.join(items) 
    return res 

def align_paragraph(paragraph, width, debug=0): 
    ''' 
    align paragraph to specified width, 
    returns list of paragraph lines 
    ''' 
    lines = list() 
    if type(paragraph) == type(lines): 
        lines.extend(paragraph) 
    elif type(paragraph) == type(''): 
        lines.append(paragraph) 
    elif type(paragraph) == type(tuple()): 
        lines.extend(list(paragraph)) 
    else: 
        raise TypeError, 'Unsopported paragraph type: %r' % type(paragraph) 
 
    flatten_para = ' '.join(lines) 
 
    splitted = textwrap.wrap(flatten_para, width)  
    # if debug: 
    #     print 'textwrap:\n%s\n' % '\n'.join(splitted) 
 
    wrapped = list() 
    while len(splitted) > 0: 
        line = splitted.pop(0) 
        if len(splitted) == 0: 
            last_paragraph_line = 1 
        else: 
            last_paragraph_line = 0 
        aligned = align_string(line, width, last_paragraph_line) 
        wrapped.append(aligned)
 
    if debug: 
        print 'textwrap & align_string:\n%s\n' % '\n'.join(wrapped) 
 
    return wrapped 