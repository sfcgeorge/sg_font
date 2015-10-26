#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
import fontforge

font = fontforge.font()
font.fontname = "SG"
font.fullname = "SG"
font.familyname = "SG"
font.em = 500

upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
chars = [["period", "."], ["comma", ","], ["apostrophe", "'"], ["quote", '"'], ["semicolon", ";"], ["colon", ":"], ["question", "?"], ["interrobang", u"‽"], ["exclamation", "!"], ["hyphen", "-"], ["underscore", "_"], ["forwardslash", "/"], ["backslash", "\\"], ["pipe", "|"], ["lbracket", "("], ["rbracket", ")"], ["lsquare", "["], ["rsquare", "]"], ["lbrace", "{"], ["rbrace", "}"], ["at", "@"], ["hash", "#"], ["pound", u"£"], ["dollar", "$"], ["percent", "%"], ["hat", "^"], ["ampersand", "&"], ["star", "*"], ["plus", "+"], ["equals", "="], ["tilde", "~"], ["tick", "`"], ["less", "<"], ["more", ">"]]
descenders = ["g", "p", "q", "y"]
superscript = ["'", '"', "`", "^"]
floating = ["*", "+", "="]
middle = ["-", "~"]

def gen(kind, mapping):
    for char in mapping:
        if type(char) == list:
            name = char[0]
            char = char[1]
        else:
            name = char

        glyph = font.createChar(ord(char))
        glyph.importOutlines("characters/{0}_{1}.svg".format(kind, name))
        ymin = glyph.boundingBox()[1]
        glyph.transform([1, 0, 0, 1, 0, -ymin])
        glyph.left_side_bearing = glyph.right_side_bearing = 40

        if char in descenders: glyph.transform([1, 0, 0, 1, 0, -100])
        if char in superscript: glyph.transform([1, 0, 0, 1, 0, 300])
        if char in floating: glyph.transform([1, 0, 0, 1, 0, 100])
        if char in middle: glyph.transform([1, 0, 0, 1, 0, 200])

        glyph.autoHint()

glyph = font.createMappedChar(" ")
glyph.width = 200

gen("upper", upper)
gen("lowerbig", lower)
gen("numbers", numbers)
gen("chars", chars)

#  font.generate("sg_font.pfb", flags=["tfm", "afm"]) # type1 with tfm/afm
font.generate("sg_font.otf") # opentype
font.generate("sg_font.ttf") # truetype
