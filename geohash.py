from datetime import datetime
import hashlib
from struct import unpack
# https://www.codewars.com/kata/58ca7afc92ce34dfa50001fa/train/python


def geohash(dow, date=datetime.now()):
    s = "{}-{:.2f}".format(date.strftime("%Y-%m-%d"), dow)
    md5 = hashlib.md5(s.encode("UTF-8")).hexdigest()
    f = [float.fromhex("0.{}".format(i)) for i in [md5[:16], md5[16:]]]
    return [float("%.6f" % i) for i in f]



def geohash2(s, d=datetime.now()):
    return [round(n / 0x100000000, 6) for n in unpack('>I4xI4x', md5('{}-{:.02f}'.format(d.strftime('%Y-%m-%d'), s).encode()).digest())]



d = datetime(2005, 5, 26)
s = 10458.68
expt = [0.857713, 0.544543]

m = hashlib.md5('{}-{:.02f}'.format(d.strftime('%Y-%m-%d'), s).encode())
u = unpack('>I4xI4x', m.digest())