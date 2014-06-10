#!/usr/bin/env python

# standard library imports
from collections import defaultdict
from contextlib import closing
from fnmatch import fnmatch
import json
import os
import os.path
import shutil
import subprocess
import sys

# third party related imports
import fontforge

# local library imports


def list_woffs(folder):
    """Find all woff files containing in a directory."""

    ret = filter(lambda f: fnmatch(f, '*.woff'), os.listdir(folder))
    ret.sort(key=lambda w: int(w[1:w.index('.')], 16))
    return ret


def analyze_woff(folder, woff_name):
    """Read a woff file."""

    ret = {'fullname': None}

    with closing(fontforge.open(os.path.join(folder, woff_name))) as f:
        ret['fullname'] = f.fullname

    return ret


def group_by_fontname(folder, woffs, woff_detail):
    """Aggregate all woff files with same fullname."""

    ret = defaultdict(list)

    for woff in woffs:
        detail = woff_detail[woff]
        ret[detail['fullname']].append(woff)

    for key in ret:
        ret[key].sort(key=lambda w: int(w[1:w.index('.')], 16))

    return ret


def merge(folder, woffs, woff_detail):
    """Merge woff files with the same fullname and modify css file."""

    font_name_dict = group_by_fontname(folder, woffs, woff_detail)

    with closing(open('font_name_dict', 'w')) as f:
        f.write(json.dumps(font_name_dict, indent=4))

    for font_name, woffs in font_name_dict.items():
        output_woff = os.path.join(folder, font_name + '.woff')

        if len(woffs) == 1:
            shutil.copy(os.path.join(folder, woffs[0]), output_woff)
        else:
            merged = fontforge.open(os.path.join(folder, woffs[0]))
            for ix in xrange(2, len(woffs)):
                merged.mergeFonts(os.path.join(folder, woffs[ix]))

            merged.generate(output_woff)

    modify_css(folder, font_name_dict)


def modify_css(folder, font_name_dict):
    """Replace font family in css file."""

    with closing(open(os.path.join(folder, 'main.css'))) as f:
        css_file = f.read().decode('utf8')

    for font_name, woffs in font_name_dict.items():
        for woff in woffs:
            replacee = 'url(%s)' % woff
            replacer = 'url(%s)' % (font_name + '.woff')
            css_file = css_file.replace(replacee, replacer)

    with closing(open(os.path.join(folder, 'main.css'), 'wb')) as f:
        f.write(css_file.encode('utf8'))


def delete_old_woffs(folder, woffs):
    """Delete pdf2htmlEX output woff files."""

    for woff in woffs:
        old_woff = os.path.join(folder, woff)
        if os.path.exists(old_woff):
            os.unlink(old_woff)


def main(argv):

    if len(argv) != 2:
        print 'usage: python %s <output_dir>' % argv[0]
        exit(1)

    output_dir = argv[1]
    woffs = list_woffs(output_dir)
    woff_detail = {woff: analyze_woff(output_dir, woff) for woff in woffs}
    merge(output_dir, woffs, woff_detail)
    delete_old_woffs(output_dir, woffs)


if __name__ == '__main__':

    main(sys.argv)
