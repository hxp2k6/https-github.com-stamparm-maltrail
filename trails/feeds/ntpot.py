#!/usr/bin/env python

"""
Copyright (c) 2014-2015 Miroslav Stampar (@stamparm)
See the file 'LICENSE' for copying permission
"""

from core.common import retrieve_content

__url__ = "https://raw.githubusercontent.com/aelth/ntpot-blacklist/master/bl/blacklist-weekly.txt"
__check__ = "NTPot"
__info__ = "attacker"
__reference__ = "(ntpot)"

def fetch():
    retval = {}
    content = retrieve_content(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#') or '.' not in line:
                continue
            retval[line] = (__info__, __reference__)

    return retval
