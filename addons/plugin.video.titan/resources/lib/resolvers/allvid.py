# -*- coding: utf-8 -*-

'''
    Genesis Add-on
    Copyright (C) 2015 lambda

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import re,urllib
from resources.lib.libraries import client
from resources.lib.libraries import jsunpack


def resolve(url):
    try:
        headers = '|%s' % urllib.urlencode({'User-Agent': client.agent(), 'Referer': url})

        url = url.replace('/embed-', '/')
        url = re.compile('//.+?/([\w]+)').findall(url)[0]
        url = 'http://allvid.ch/embed-%s.html' % url

        result = client.request(url)

        r = re.compile('file\s*:\s*"(.+?)".+?label\s*:\s*"(\d+)"').findall(result)

        if len(r) == 0:
            r = re.compile('(eval.*?\)\)\))').findall(result)[-1]
            r = jsunpack.unpack(r)
            r = re.compile('file\s*:\s*"(.+?)".+?label\s*:\s*"(\d+)"').findall(r)

        url = []
        try: url.append({'quality': '1080p', 'url': [i[0] + headers for i in r if int(i[1]) >= 1080][0]})
        except: pass
        try: url.append({'quality': 'HD', 'url': [i[0] + headers for i in r if 720 <= int(i[1]) < 1080][0]})
        except: pass
        try: url.append({'quality': 'SD', 'url': [i[0] + headers for i in r if int(i[1]) < 720][0]})
        except: pass

        return url
    except:
        return


