#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# part of JSunidecode library
# rather simple script for embedding datasheet into the JSunidecode closure

from __future__ import unicode_literals


EMBED_TARGET = b'/*!DATASHEET**/'
DATASHEET_PATH = 'datasheet.js'
JSUNIDECODE_PATH = 'unidecode.js'
OUTPUT_PATH = 'build/unidecode.omni.js'

def main(argv):
    with open(JSUNIDECODE_PATH, 'rb') as infp_js:
        content = infp_js.read()

    with open(DATASHEET_PATH, 'rb') as infp_data:
        datasheet = infp_data.read()

    result = content.replace(EMBED_TARGET, datasheet, 1)

    with open(OUTPUT_PATH, 'wb') as outfp:
        outfp.write(result)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


# vim:ai:et:ts=4:sw=4:sts=4:fenc=utf-8:
