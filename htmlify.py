#!/usr/bin/env python
# -*- coding: utf8 -*-
# standard library imports
import subprocess
import sys

# third party related imports

# local library imports

"""Usage: pdf2htmlEX [options] <input.pdf> [<output.html>]
  -f,--first-page <int>         first page to convert (default: 1)
  -l,--last-page <int>          last page to convert (default: 2147483647)
  --zoom <fp>                   zoom ratio
  --fit-width <fp>              fit width to <fp> pixels
  --fit-height <fp>             fit height to <fp> pixels
  --use-cropbox <int>           use CropBox instead of MediaBox (default: 1)
  --hdpi <fp>                   horizontal resolution for graphics in DPI (default: 144)
  --vdpi <fp>                   vertical resolution for graphics in DPI (default: 144)
  --embed <string>              specify which elements should be embedded into output
  --embed-css <int>             embed CSS files into output (default: 1)
  --embed-font <int>            embed font files into output (default: 1)
  --embed-image <int>           embed image files into output (default: 1)
  --embed-javascript <int>      embed JavaScript files into output (default: 1)
  --embed-outline <int>         embed outlines into output (default: 1)
  --split-pages <int>           split pages into separate files (default: 0)
  --dest-dir <string>           specify destination directory (default: ".")
  --css-filename <string>       filename of the generated css file (default: "")
  --page-filename <string>      filename template for splitted pages  (default: "")
  --outline-filename <string>   filename of the generated outline file (default: "")
  --process-nontext <int>       render graphics in addition to text (default: 1)
  --process-outline <int>       show outline in HTML (default: 1)
  --process-annotation <int>    show annotation in HTML (default: 0)
  --printing <int>              enable printing support (default: 1)
  --fallback <int>              output in fallback mode (default: 0)
  --tmp-file-size-limit <int>   Maximum size (in KB) used by temporary files, -1 for no limit. (default: -1)
  --embed-external-font <int>   embed local match for external fonts (default: 1)
  --font-format <string>        suffix for embedded font files (ttf,otf,woff,svg) (default: "woff")
  --decompose-ligature <int>    decompose ligatures, such as ﬁ -> fi (default: 0)
  --auto-hint <int>             use fontforge autohint on fonts without hints (default: 0)
  --external-hint-tool <string> external tool for hinting fonts (overrides --auto-hint) (default: "")
  --stretch-narrow-glyph <int>  stretch narrow glyphs instead of padding them (default: 0)
  --squeeze-wide-glyph <int>    shrink wide glyphs instead of truncating them (default: 1)
  --override-fstype <int>       clear the fstype bits in TTF/OTF fonts (default: 0)
  --process-type3 <int>         convert Type 3 fonts for web (experimental) (default: 0)
  --heps <fp>                   horizontal threshold for merging text, in pixels (default: 1)
  --veps <fp>                   vertical threshold for merging text, in pixels (default: 1)
  --space-threshold <fp>        word break threshold (threshold * em) (default: 0.125)
  --font-size-multiplier <fp>   a value greater than 1 increases the rendering accuracy (default: 4)
  --space-as-offset <int>       treat space characters as offsets (default: 0)
  --tounicode <int>             how to handle ToUnicode CMaps (0=auto, 1=force, -1=ignore) (default: 0)
  --optimize-text <int>         try to reduce the number of HTML elements used for text (default: 0)
  --bg-format <string>          specify background image format (default: "png")
  -o,--owner-password <string>  owner password (for encrypted files)
  -u,--user-password <string>   user password (for encrypted files)
  --no-drm <int>                override document DRM settings (default: 0)
  --clean-tmp <int>             remove temporary files after conversion (default: 1)
  --tmp-dir <string>            specify the location of tempory directory. (default: "/tmp")
  --data-dir <string>           specify data directory (default: "/usr/local/share/pdf2htmlEX")
  --debug <int>                 print debugging information (default: 0)
  -v,--version                  print copyright and version info
  -h,--help                     print usage information

"""

def main(argv):

    if len(argv) != 3:
        print 'usage: python %s <pdf> <output-dir>' % argv[0]
        exit(1)

    pdf, output_dir = argv[1], argv[2]
    options = [
        '--embed-css=0',
        '--embed-font=0',
        '--embed-image=0',
        '--embed-javascript=0',
        '--embed-outline=0',
        '--split-pages=1',
        '--process-outline=0',
        '--external-hint-tool=ttfautohint',
        '--bg-format=jpg',
        '--dest-dir=%s' % output_dir,
        '--css-filename=main.css'
    ]

    subprocess.check_call(['pdf2htmlEX'] + options + [pdf, 'index.html'])


if __name__ == '__main__':

    main(sys.argv)
