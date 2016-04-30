#!/usr/bin/env python
#coding:utf-8
# Copyright: (c) 2016 by Mehdi Bayazee <bayazee@gmail.com>
# Multi-purpose iransystem codec convertor
# License: BSD, see LICENSE for more details.


import sys

iransystem = (
    u'\u0000', u'\u0001', u'\u0002', u'\u0003', u'\u0004', u'\u0005', u'\u0006', u'\u0007', # 0-7
    u'\u0008', u'\u0009', u'\u000A', u'\u000B', u'\u000C', u'\u000D', u'\u000E', u'\u000F', # 8-16
    u'\u0010', u'\u0011', u'\u0012', u'\u0013', u'\u0014', u'\u0015', u'\u0016', u'\u0017', # 16-23
    u'\u0018', u'\u0019', u'\u001A', u'\u001B', u'\u001C', u'\u001D', u'\u001E', u'\u001F', # 24-31
    u'\u0020', u'\u0021', u'\u0022', u'\u0023', u'\u0024', u'\u0025', u'\u0026', u'\u0027', # 32-39
    u'\u0028', u'\u0029', u'\u002A', u'\u002B', u'\u002C', u'\u002D', u'\u002E', u'\u002F', # 40-47
    u'\u0030', u'\u0031', u'\u0032', u'\u0033', u'\u0034', u'\u0035', u'\u0036', u'\u0037', # 48-55
    u'\u0038', u'\u0039', u'\u003A', u'\u003B', u'\u003C', u'\u003D', u'\u003E', u'\u003F', # 56-63
    u'\u0040', u'\u0041', u'\u0042', u'\u0043', u'\u0044', u'\u0045', u'\u0046', u'\u0047', # 64-71
    u'\u0048', u'\u0049', u'\u004A', u'\u004B', u'\u004C', u'\u004D', u'\u004E', u'\u004F', # 72-79
    u'\u0050', u'\u0051', u'\u0052', u'\u0053', u'\u0054', u'\u0055', u'\u0056', u'\u0057', # 80-87
    u'\u0058', u'\u0059', u'\u005A', u'\u005B', u'\u005C', u'\u005D', u'\u005E', u'\u005F', # 88-95
    u'\u0060', u'\u0061', u'\u0062', u'\u0063', u'\u0064', u'\u0065', u'\u0066', u'\u0067', # 96-103
    u'\u0068', u'\u0069', u'\u006A', u'\u006B', u'\u006C', u'\u006D', u'\u006E', u'\u006F', # 104-111
    u'\u0070', u'\u0071', u'\u0072', u'\u0073', u'\u0074', u'\u0075', u'\u0076', u'\u0077', # 112-119
    u'\u0078', u'\u0079', u'\u007A', u'\u007B', u'\u007C', u'\u007D', u'\u007E', u'\u007F', # 120-127

    u'\u06F0', u'\u06F1', u'\u06F2', u'\u06F3', u'\u06F4', u'\u06F5', u'\u06F6', u'\u06F7', # 128-135
    u'\u06F8', u'\u06F9', u'\u060C', u'\u0640', u'\u061F', u'\u0622', u'\u0626', u'\u0621', # 136-143
    u'\u0627', u'\u0627', u'\u0628', u'\u0628', u'\u067E', u'\u067E', u'\u062A', u'\u062A', # 144-151
    u'\u062B', u'\u062B', u'\u062C', u'\u062C', u'\u0686', u'\u0686', u'\u062D', u'\u062D', # 152-159
    u'\u062E', u'\u062E', u'\u062F', u'\u0630', u'\u0631', u'\u0632', u'\u0698', u'\u0633', # 160-167
    u'\u0633', u'\u0634', u'\u0634', u'\u0635', u'\u0635', u'\u0636', u'\u0636', u'\u0637', # 168-175
    u'\xb0', u'\u2593', u'\u2502', u'\xb2', u'\xb3', u'\xb4', u'\xb4', u'\xb6', # 176-183
    u'\u2563', u'\u061F', u'\u2557', u'\u061B', u'\u255C', u'\u255B', u'\u2510', u'\u0638', # 184-191
    u'\u061f', u'\u06c1', u'\u0621', u'\u0622', u'\u0623', u'\u0624', u'\u0625', u'\u0626', # 192-199
    u'\u0627', u'\u0628', u'\u0629', u'\u062A', u'\u062B', u'\u062C', u'\u062D', u'\u062E', # 200-107
    u'\u062F', u'\u0630', u'\u0631', u'\u062b', u'\u0628', u'\u06C1', u'\u0639', u'\u0629', # 208-215
    u'\xd7', u'\u0637', u'\u0638', u'\u0639', u'\u063A', u'\u063A', u'\u063A', u'\u0643', # 216-223
    u'\u0638', u'\u0639', u'\u0639', u'\u0639', u'\u0639', u'\u063A', u'\u063A', u'\u063A', # 224-231
    u'\u063A', u'\u0641', u'\u0641', u'\u0642', u'\u0642', u'\u0643', u'\u0643', u'\u06AF', # 232-239
    u'\u06AF', u'\u0644', u'\u0644\u0627', u'\u0644', u'\u0645', u'\u0645', u'\u0646', u'\u0646', # 240-247
    u'\u0648', u'\u0647', u'\u0647', u'\u0647', u'\u06CC', u'\u06CC', u'\u06CC'  # 248-254
)

u2irs = {
    # ISOLATED - INITIAL - MEDIAL - FINALL
    0x060C: ('\x8A', '\x8A', '\x8A', '\x8A'), # ARABIC COMMA : ،
    0x0640: ('\x8B', '\x8B', '\x8B', '\x8B'), # ARABIC TATWEEL : ـ
    0x061F: ('\x8C', '\x8C', '\x8C', '\x8C'), # ARABIC QUESTION MARK : ؟
    0x0622: ('\x8D', '\x8D', '\x8D', '\x8D'), # ARABIC LETTER ALEF WITH MADDA ABOVE : آ
    0x0626: ('\x8E', '\x8E', '\x8E', '\x8E'), # ARABIC LETTER YEH WITH HAMZA ABOVE : ئ
    0x0621: ('\x8F', '\x8F', '\x8F', '\x8F'), # ARABIC LETTER HAMZA : ء
    0x0627: ('\x90', '\x90', '\x91', '\x91'), # ARABIC LETTER ALEF : ا
    0x0623: ('\x90', '\x90', '\x91', '\x91'), # ARABIC LETTER ALEF WITH HAMZA ABOVE : أ
    0x0625: ('\x90', '\x90', '\x91', '\x91'), # ARABIC LETTER ALEF WITH HAMZA BELOW : إ
    0x0628: ('\x92', '\x93', '\x93', '\x92'), # ARABIC LETTER BEH : ب
    0x067E: ('\x94', '\x95', '\x95', '\x94'), # ARABIC LETTER PEH : پ
    0x062A: ('\x96', '\x97', '\x97', '\x96'), # ARABIC LETTER TEH : ت
    0x062B: ('\x98', '\x99', '\x99', '\x98'), # ARABIC LETTER THEH : ث
    0x062C: ('\x9A', '\x9B', '\x9B', '\x9A'), # ARABIC LETTER JEEM : ج
    0x0686: ('\x9C', '\x9D', '\x9D', '\x9C'), # ARABIC LETTER TCHEH : چ
    0x062D: ('\x9E', '\x9F', '\x9F', '\x9E'), # ARABIC LETTER HAH : ح
    0x062E: ('\xA0', '\xA1', '\xA1', '\xA0'), # ARABIC LETTER KHAH : خ
    0x062F: ('\xA2', '\xA2', '\xA2', '\xA2'), # ARABIC LETTER DAL : د
    0x0630: ('\xA3', '\xA3', '\xA3', '\xA3'), # ARABIC LETTER THAL : ذ
    0x0631: ('\xA4', '\xA4', '\xA4', '\xA4'), # ARABIC LETTER REH : ر
    0x0632: ('\xA5', '\xA5', '\xA5', '\xA5'), # ARABIC LETTER ZAIN : ز
    0x0698: ('\xA6', '\xA6', '\xA6', '\xA6'), # ARABIC LETTER JEH : ژ
    0x0633: ('\xA7', '\xA8', '\xA8', '\xA7'), # ARABIC LETTER SEEN : س
    0x0634: ('\xA9', '\xAA', '\xAA', '\xA9'), # ARABIC LETTER SHEEN : ش
    0x0635: ('\xAB', '\xAC', '\xAC', '\xAB'), # ARABIC LETTER SAD : ص
    0x0636: ('\xAD', '\xAE', '\xAE', '\xAD'), # ARABIC LETTER DAD : ض
    0x0637: ('\xAF', '\xAF', '\xAF', '\xAF'), # ARABIC LETTER TAH : ط
    0x0638: ('\xE0', '\xE0', '\xE0', '\xE0'), # ARABIC LETTER ZAH : ظ
    0x0639: ('\xE1', '\xE4', '\xE3', '\xE2'), # ARABIC LETTER AIN : ع
    0x063A: ('\xE5', '\xE8', '\xE7', '\xE6'), # ARABIC LETTER GHAIN : غ
    0x0641: ('\xE9', '\xEA', '\xEA', '\xE9'), # ARABIC LETTER FEH : ف
    0x0642: ('\xEB', '\xEC', '\xEC', '\xEB'), # ARABIC LETTER QAF : ق
    0x06A9: ('\xED', '\xEE', '\xEE', '\xED'), # ARABIC LETTER KEHEH : ک
    0x0643: ('\xED', '\xEE', '\xEE', '\xED'), # ARABIC LETTER KAF : ك
    0x06AF: ('\xEF', '\xF0', '\xF0', '\xEF'), # ARABIC LETTER GAF : گ
    0x0644: ('\xF1', '\xF3', '\xF3', '\xF1'), # ARABIC LETTER LAM : ل
    0x0645: ('\xF4', '\xF5', '\xF5', '\xF4'), # ARABIC LETTER MEEM : م
    0x0646: ('\xF6', '\xF7', '\xF7', '\xF6'), # ARABIC LETTER NOON : ن
    0x0648: ('\xF8', '\xF8', '\xF8', '\xF8'), # ARABIC LETTER WAW : و
    0x0647: ('\xF9', '\xFB', '\xFA', '\xF9'), # ARABIC LETTER HEH : ه
    0x06CC: ('\xFD', '\xFE', '\xFE', '\xFC'), # ARABIC LETTER FARSI YEH : ی
    0x0649: ('\xFD', '\xFE', '\xFE', '\xFC'), # ARABIC LETTER ALEF MAKSURA : ى
    0x064A: ('\xFD', '\xFE', '\xFE', '\xFC'), # ARABIC LETTER YEH : ي
    0x06A0: ('\xFF', '\xFF', '\xFF', '\xFF'), # ARABIC LETTER AIN WITH THREE DOTS ABOVE : ڠ

}

set_im_iso = (
    0x0622, # ARABIC LETTER ALEF WITH MADDA ABOVE : آ
    0x0621, # ARABIC LETTER HAMZA : ء
    0x0627, # ARABIC LETTER ALEF : ا
    0x0623, # ARABIC LETTER ALEF WITH HAMZA ABOVE : أ
    0x0625, # ARABIC LETTER ALEF WITH HAMZA BELOW : إ
    0x062F, # ARABIC LETTER DAL : د
    0x0630, # ARABIC LETTER THAL : ذ
    0x0631, # ARABIC LETTER REH : ر
    0x0632, # ARABIC LETTER ZAIN : ز
    0x0698, # ARABIC LETTER JEH : ژ
    0x0648, # ARABIC LETTER WAW : و
)

# We should add an extra space to these letters
hasSpace = (146, 148, 150, 152, 154, 156, 158, 160, 167, 169, 171, 173, 225,
            226, 229, 230, 233, 235, 237, 239, 241, 244, 246, 249, 252, 253)

spcs = {32: ' ', 40: ')', 41: '(', 47: '/'}

ISOLATED = 0
INITIAL = 1
MEDIAL = 2
FINALL = 3

def irs_spc_char(ordCh):
    """return true if ch is spc"""

    return spcs.get(ordCh, 0)

def irs_to_utf8(iBuf):
    """convert iransystem codec to unicode"""

    uBuf = ''
    subStr = ''

    for ch in iBuf:
        ordCh = ord(ch)
        uCh = iransystem[ordCh & 0x00ff]

        uCh = spcs.get(ordCh, uCh)
        uCh += (' ' if ordCh in hasSpace else '')

        if ordCh < 138 :
            subStr += uCh
        else:
            uBuf = subStr + uBuf
            subStr = ''
            uBuf = uCh + uBuf
            uCh = ''

        uBuf = subStr + uBuf
        subStr = ''

    return uBuf.strip()

def utf8_to_irs(uBuf):
    """Convert unicode string to iransystem"""

    #TODO: mixed strings. en in farsi

    if not isinstance(uBuf, unicode):
        raise TypeError, 'unicode needed'
    uBuf += u' '
    uBuf = u' ' + uBuf
    iBuf = ''

    for i in range(1, len(uBuf)-1):
        iBuf = _unicode_to_iransystem(uBuf[i], uBuf[i-1], uBuf[i+1]) + iBuf

    return iBuf

def _unicode_to_iransystem(uCh, beforCh=None, afterCh=None):
    """convert unicode char to iransystem"""

    uni = ord(uCh)
    after = ord(afterCh)
    befor = ord(beforCh)

    before_is_letter = False
    after_is_letter = False

    if uni < 0x0600:
        return chr(uni)

    # numbers
    if uni >= 0x6f0 and uni <= 0x6f9:
        return chr(uni - 0x670)

    # لا
    if uni == 0x0644 and after == 0x0627:
        return '\xF2'

    if uni == 0x0627 and befor == 0x0644:
        return ''

    if befor >= 0x620 and befor <= 0x6d0:
        before_is_letter = True

    if after >= 0x620 and after <= 0x6d0:
        after_is_letter = True

    if before_is_letter and after_is_letter:
        pos = MEDIAL
    elif before_is_letter and not after_is_letter:
        pos = FINALL
    elif not before_is_letter and after_is_letter:
        pos = INITIAL
    else:
        pos = ISOLATED

    if befor in set_im_iso :
        if pos == MEDIAL:
            pos = INITIAL
        elif pos == FINALL:
            pos = ISOLATED


    return u2irs[uni][pos]


if __name__=='__main__':
    #data = file('data.py', 'r').readlines()
    #fp =file('fa2.txt', 'w')

    #for line in data:
        #fp.write(utf8_to_irs(unicode(line, 'utf8')))

    #data = file('fa2.txt', 'r').readlines()

    #for l in data:
        #print irs_to_utf8(l)
    print irs_to_utf8('\x81            \x91\xfa\xf7\x91\x97\xa8\x90')
