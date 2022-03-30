import os, re, sys, glob, time, urllib2, cookielib, random
from urlparse import urlparse
import threading
from Queue import Queue

try:
    import requests
except ImportError:
    print '---------------------------------------------------'
    print '[*] pip install requests'
    print '   [-] you need to install requests Module'
    sys.exit()


class Dorker(object):
    def __init__(self):
        self.cls()
        self.print_logo()
        try:
            os.mkdir('logs')
        except:
            pass
        try:
            os.mkdir('results')
        except:
            pass
        self.concurrent = 70
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.Header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        self.domains = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao',
                        'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb',
                        'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo',
                        'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd',
                        'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr',
                        'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do',
                        'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi',
                        'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf',
                        'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs',
                        'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
                        'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'is', 'it',
                        'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn',
                        'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk',
                        'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me',
                        'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr',
                        'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc',
                        'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz',
                        'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn',
                        'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru',
                        'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj',
                        'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy',
                        'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm',
                        'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug',
                        'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi',
                        'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw', 'com',
                        'net', 'org', 'biz', 'gov', 'mil', 'edu', 'info', 'int', 'tel',
                        'name', 'aero', 'asia', 'cat', 'coop', 'jobs', 'mobi', 'museum',
                        'pro', 'travel']
        try:
            self.Get_list = raw_input(self.r + '    [+]' + self.c + ' Enter List Dork: ' + self.y)
        except IOError:
            print self.r + '--------------------------------------------'
            print self.r + '    [' + self.y + '-' + self.r + '] ' + self.c + ' List Not Found in Directory!'
            sys.exit()
        self.q = Queue(self.concurrent * 2)
        for i in range(self.concurrent):
            self.t = threading.Thread(target=self.doWork)
            self.t.daemon = True
            self.t.start()
        try:
            for url in open(self.Get_list):
                self.q.put(url.strip())
            self.q.join()
        except:
            sys.exit()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """

                    Black Hat Hackers                                                                                           
   _|_|_|    _|_|      _|        _|  _|_|_|_|  _|                  _|                      
 _|        _|    _|    _|            _|            _|_|_|      _|_|_|    _|_|    _|  _|_|  
   _|_|    _|  _|_|    _|        _|  _|_|_|    _|  _|    _|  _|    _|  _|_|_|_|  _|_|      
       _|  _|    _|    _|        _|  _|        _|  _|    _|  _|    _|  _|        _|        
 _|_|_|      _|_|  _|  _|_|_|_|  _|  _|        _|  _|    _|    _|_|_|    _|_|_|  _|        
       Priv8 Tools SQLi Finder Mass     
Special Thanks To: INDONESIA~SYNDICATE666 Gh0sT Sec T34M ~
GrayHat Sec666 Gh0sT T34M ~ GreyHat School Of Hackers ~ Boyolali BlackHat T34M ~
All HackTivist INDONESIA & Hacker`s Rulezzz INDONESIA!
                                                                              AUTHOR: Alice666x
                                                                              C0d3D: Alice666x         
     Note! : We don't Accept any responsibility for any illegal usage.       
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def duplicate_remover(self, x):
        urls3 = glob.glob(x)
        domains = {}
        for line in urls3:
            with open(line, "r") as infile:
                for line1 in infile:
                    if line1.startswith("http://"):
                        line1 = line1.replace("http://", "")
                    elif line1.startswith("https://"):
                        line1 = line1.replace("https://", "")
                    else:
                        pass
                    x = 'http://' + line1
                    parse = urlparse(x)
                    domains[parse[1]] = line1
            with open('results/MyBeSqliVulnLists.txt', "a") as outfile:
                for line1 in domains:
                    outfile.write(domains[line1])
            domains.clear()
        os.unlink('results/MyBeSqliVulnList.txt')

    def doWork(self):
        try:
            while True:
                dork = self.q.get()
                for domain in self.domains:
                    next = 0
                    while next <= 500:
                        url = 'http://www.bing.com/search?q=' + dork + 'site:' + domain + ' php?id=&first=' + str(
                            next) + '&FORM=PORE'
                        sess = requests.session()
                        cnn = sess.get(url, headers=self.Header, timeout=5)
                        next = next + 10
                        finder = re.findall('<h2><a href="(\S+)"', cnn.text)
                        for url in finder:
                            if url.startswith('http://'):
                                url = url.replace('http://', '')
                            elif url.startswith('https://'):
                                url = url.replace('https://', '')
                            else:
                                pass
                            with open("logs/logs.txt", 'a') as f:
                                if 'go.microsoft.com' in url:
                                    pass
                                elif '.wordpress.' in url:
                                    pass
                                elif '.blogspot.' in url:
                                    pass
                                else:
                                    if 'php?id=' in url:
                                        print self.c + '       [' + self.y + '+' + self.c + '] ' + self.y + url
                                        f.write(str(url + '\n'))
                                    else:
                                        pass
                    lines = open("logs/logs.txt", 'r').read().splitlines()
                    lines_set = set(lines)
                    count = 0
                    for line in lines_set:
                        with open("results/MyBeSqliVulnList.txt", 'a') as xx:
                            count = count + 1
                            xx.write(line + '\n')
                    '''self.duplicate_remover('results/MyBeSqliVulnList.txt')'''
                self.q.task_done()
        except:
            pass


Dorker()