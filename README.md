# circuits Website

This is the circuits Website a static site generated using [Pelican][1].
All content are maintained by [reStructedText][2] so you can easily
add to or modify content with any regular text editor.


## Quick Start

```#!bash
$ python3 -m venv tmp
$ . tmp/bin/activate
$ pip install -r requirements.txt
$ make clean html
$ circuits.web output
$ deactivate
```

Generated website should be viewable at: http://localhost:8000/

  [1]: http://blog.getpelican.com/
  [2]: https://en.wikipedia.org/wiki/ReStructuredText
