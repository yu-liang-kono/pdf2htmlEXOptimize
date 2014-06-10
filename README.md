pdf2htmlEXOptimize
==================

## Introduction
`pdf2htmlEXOptimize` is a python tool set aiming to reduce [pdf2htmlEX][1] output file size. The output `woff` files of [pdf2htmlEX][2] are usually bloated and cost lots of space and bandwidth. `pdf2htmlEXOptimize` is a post-processing tool set trying to minimize the file size.

## Prerequsite

 - [pdf2htmlEX][3]
 - [fontforge][4] with python support
 - [ttfautohint][5] (optional)

### htmlify.py

 - usage: `python htmlify.py pdf-file output-dir`
 - It generates html by `pdf2htmlEX` using the following options
     - `--embed-css=0`
     - `--embed-font=0`
     - `--embed-image=0`
     - `--embed-javascript=0`
     - `--embed-outline=0`
     - `--split-pages=1`
     - `--process-outline=0`
     - `--external-hint-tool=ttfautohint` (If `ttfautohint` is installed.)
     - `--bg-format=jpg`
     - `--css-filename=main.css`
 - The output html is `index.html`.

### optimize_woff.py

 - usage: `python optimize_woff.py pdf2htmlEX-output-dir`
 - It merges `woff` files with the same name and modify `main.css` accordingly.

  [1]: https://github.com/coolwanglu/pdf2htmlEX
  [2]: https://github.com/coolwanglu/pdf2htmlEX
  [3]: https://github.com/coolwanglu/pdf2htmlEX
  [4]: http://fontforge.org/python.html
  [5]: http://www.freetype.org/ttfautohint/