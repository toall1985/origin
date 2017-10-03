import re
import requests

domain = ['streamango.com']
name = 'Streamango'

sources = []

#### Credit to Jsergio for decode method

def decode(encoded, code):
        _0x59b81a = ""
        k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
        k = k[::-1]

        count = 0

        for index in range(0, len(encoded) - 1):
            while count <= len(encoded) - 1:
                _0x4a2f3a = k.index(encoded[count])
                count += 1
                _0x29d5bf = k.index(encoded[count])
                count += 1
                _0x3b6833 = k.index(encoded[count])
                count += 1
                _0x426d70 = k.index(encoded[count])
                count += 1

                _0x2e4782 = ((_0x4a2f3a << 2) | (_0x29d5bf >> 4))
                _0x2c0540 = (((_0x29d5bf & 15) << 4) | (_0x3b6833 >> 2))
                _0x5a46ef = ((_0x3b6833 & 3) << 6) | _0x426d70
                _0x2e4782 = _0x2e4782 ^ code

                _0x59b81a = str(_0x59b81a) + chr(_0x2e4782)

                if _0x3b6833 != 64:
                    _0x59b81a = str(_0x59b81a) + chr(_0x2c0540)
                if _0x3b6833 != 64:
                    _0x59b81a = str(_0x59b81a) + chr(_0x5a46ef)

        return 'http:'+ _0x59b81a

def resolve(url):
    html = requests.get(url).content
    encoded = re.search('''srces\.push\({type:"video/mp4",src:\w+\('([^']+)',(\d+)''', html)
    source = decode(encoded.group(1), int(encoded.group(2)))
    try:
        quality = re.findall('type:"video/mp4",src:".+?",height:(.+?),',html)[0]
        quality = quality+'p'
    except:
        quality = 'SD'

    sources.append({'source': 'Streamango', 'quality': quality, 'scraper':name, 'url': source,'direct': True})
    print sources
