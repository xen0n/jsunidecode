JSunidecode
===========

This project is a (rather simple) JavaScript port of the Python Unicode
transliteration library ``unidecode``, done for the generation of slugs
from Chinese article titles.

Upon importing, it basically injects a ``unidecode`` function, which is
a near-verbatim translation of the original Python worker function, into
``String.prototype`` so that it can be used anywhere.

The datasheet mapping the vast number of Unicode codepoints to ASCII
is rather space-consuming, so you may want to turn on gzipping for your
JS files. It is created by importing all the individual Python data
modules, converting them into a Python ``dict``, then dumping the dict
into JSON format.


Usage
-----

The code can be incorporated into your JS environment in several ways.
Of course you can import the function and datasheet separately:

    <!-- XXX This method is NOT recommended -->
    <!-- datasheet must be imported first, for obvious reasons -->
    <script src="datasheet.js"></script>
    <script src="unidecode.js"></script>

\... but this approach has the apparent disadvantage of leaking a
``datasheet`` variable into the global namespace, subject to potential
overwrite. So you can first "embed" the datasheet into the closure
using the supplied Python script, then import ``unidecode.omni.js``
inside the ``build`` directory (the output path is hardcoded at the
moment).

For maximum bandwidth saving, you may also want to minify the resulting
file using, for example, the YUI compressor. The datasheet's size is
not quite sensitive to minification though; you definitely want to turn
on gzipping for at least this file, as well.


Bugs and Limitations
--------------------

The code is a near-exact translation of the Python (translation), so
it should be reasonably functionally equivalent to the Python library.
Thus, it can NOT handle transliteration of Japanese Kanji nor Korean
Hanja correctly -- they are all treated as Chinese characters and thus
transliterated with Standard Mandarin pronunciation. For that purpose
you may look at AJAX approaches, or try out Google's Transliteration
API for now.


.. vim:ai:et:ts=4:sw=4:sts=4:fenc=utf-8:
