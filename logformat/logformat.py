#!/usr/bin/env python
# encoding: utf-8
# author: wucheng <jacky.wucheng@gmail.com>
# date: 2011年12月 9日 星期五 11时46分43秒 CST

from termcolor import cprint
from optparse import OptionParser
from urlparse import urlparse
import time
import sys
import re
import pprint

############## global regex pattern ######################
source_url_pattern = r'full_url: (.*),'
remote_ip_pattern = r'remote_ip: (.*?),'
sep = '-'*40
##########################################################

def filtrator(input_line, regex_pattern):
    if not input_line:
        return None
    
    m = re.search(regex_pattern, input_line)
    if not m:
        return None
    
    return m.groups()[0]

def asleep(t=0.2):
    time.sleep(t)

def highlight_source_url():
    while True:
        line = sys.stdin.readline().strip()

        if not line:
            asleep()
            continue
        source_url = filtrator(line, source_url_pattern)
        if not source_url:
            asleep()
            continue
        
        cprint(source_url, "yellow")
        asleep()
        
def highlight_remote_ip():
    while True:
        line = sys.stdin.readline().strip()

        if not line:
            asleep()
            continue

        remote_ip = filtrator(line, remote_ip_pattern)
        if not remote_ip:
            asleep()
            continue
        cprint(remote_ip, "red")
        asleep()

def stat_remote_ip(topn):
    """ 统计remote_ip的出现次数，按照topN排序 """
    stat = {}
    for line in sys.stdin:
        line_s = line.strip()
        if not line_s:
            continue
        remote_ip = filtrator(line, remote_ip_pattern)
        if not remote_ip:
            continue
        if remote_ip not in stat:
            stat[remote_ip] = 1
        else:
            stat[remote_ip] += 1
    # 排序
    sorted_stat = sorted(stat.items(), key=lambda x: x[1], reverse=True)
    topn_stat = sorted_stat[0:topn]
    pprint.pprint(topn_stat)


def loop_stat_remote_ip(topn):
    """ 统计remote_ip的出现次数，按照topN排序 """
    stat = {}
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue
        remote_ip = filtrator(line, remote_ip_pattern)
        if not remote_ip:
            continue
        if remote_ip not in stat:
            stat[remote_ip] = 1
        else:
            stat[remote_ip] += 1
        # 排序
        sorted_stat = sorted(stat.items(), key=lambda x: x[1], reverse=True)
        topn_stat = sorted_stat[0:topn]
        pprint.pprint(topn_stat)
        print(sep)

def stat_path(topn):
    stat = {}
    for line in sys.stdin:
        line_s = line.strip()
        if not line_s:
            continue
        full_url = filtrator(line, source_url_pattern)
        if not full_url:
            continue
        parse_o = urlparse(full_url)
        domain = parse_o.netloc
        path = parse_o.path
        url_path = "%s/%s" % (domain, path)

        if not url_path:
            continue
        if url_path not in stat:
            stat[url_path] = 1
        else:
            stat[url_path] += 1
    # 排序
    sorted_stat = sorted(stat.items(), key=lambda x: x[1], reverse=True)
    topn_stat = sorted_stat[0:topn]
    pprint.pprint(topn_stat)

def stat_domain(topn):
    stat = {}
    for line in sys.stdin:
        line_s = line.strip()
        if not line_s:
            continue
        full_url = filtrator(line, source_url_pattern)
        if not full_url:
            continue
        domain = urlparse(full_url).netloc

        if not domain:
            continue
        if domain not in stat:
            stat[domain] = 1
        else:
            stat[domain] += 1
    # 排序
    sorted_stat = sorted(stat.items(), key=lambda x: x[1], reverse=True)
    topn_stat = sorted_stat[0:topn]
    pprint.pprint(topn_stat)


def loop_stat_domain(topn):
    stat = {}
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue
        full_url = filtrator(line, source_url_pattern)
        if not full_url:
            continue
        domain = urlparse(full_url).netloc

        if not domain:
            continue
        if domain not in stat:
            stat[domain] = 1
        else:
            stat[domain] += 1
        # 排序
        sorted_stat = sorted(stat.items(), key=lambda x: x[1], reverse=True)
        topn_stat = sorted_stat[0:topn]
        pprint.pprint(topn_stat)
        #print(topn_stat)
        print(sep)
        #asleep(1)


        
def loop_stat_path(topn):
    stat = {}
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue
        full_url = filtrator(line, source_url_pattern)
        if not full_url:
            continue
        parse_o = urlparse(full_url)
        domain = parse_o.netloc
        path = parse_o.path
        url_path = "%s/%s" % (domain, path)

        if not url_path:
            continue
        if url_path not in stat:
            stat[url_path] = 1
        else:
            stat[url_path] += 1
        # 排序
        sorted_stat = sorted(stat.items(), key=lambda x: x[1], reverse=True)
        topn_stat = sorted_stat[0:topn]
        pprint.pprint(topn_stat)
        #print(topn_stat)
        print(sep)

def test():
    cprint("hello", "yellow")

def test_filtrator():
    input_line = ("[I 111208 21:56:04 r3_http:104] R3Handler: succ redirect,"
                "redirect_url: http://119.147.148.28/tech.down.sina.com.cn/20110615/edfc53d9/AdbeRdr1010_zh_CN.exe"
                "?fn=&ssig=I5C8shI79Z&Expires=1311778341&KID=sae,230kw3wk15&ip=1311699141,125.112.230.195, "
                "remote_ip: 125.77.120.9, full_url: http://tech.down.sina.com.cn/20110615/edfc53d9/AdbeRdr1010_zh_CN.exe?"
                "fn=&ssig=I5C8shI79Z&Expires=1311778341&KID=sae,230kw3wk15&ip=1311699141,125.112.230.195, elapse: 1.751 ms")

    regex_pattern = r'full_url: (.*),'
    print filter(input_line, regex_pattern)


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage=usage)
    parser.add_option("-u", "--source_url", dest="source_url", action="store_true", 
                         help="highlight source url")
    parser.add_option("-p", "--remote_ip", dest="remote_ip", action="store_true",
                        help="highlight remote ip")
    parser.add_option("-s", "--stat_remote_ip", dest="stat_remote_ip", action="store_true",
                        help="stats remote ip and sorted to top N")
    parser.add_option("-r", "--loop_stat_remote_ip", dest="loop_stat_remote_ip", action="store_true",
                        help="loop read lines from tailf and stats remote ip and sorted to top N")
    parser.add_option("-d", "--stat_domain", dest="stat_domain", action="store_true",
                        help="stats domain and sorted to top N")
    parser.add_option("-l", "--loop_stat_domain", dest="loop_stat_domain", action="store_true",
                        help="loop read lines from tailf and stats domain and sorted to top N")
    parser.add_option("-q", "--loop_stat_path", dest="loop_stat_path", action="store_true",
                        help="loop read lines from tailf and stats url path and sorted to top N")
    parser.add_option("-n", "--stat_path", dest="stat_path", action="store_true",
                        help="stats url path and sorted to top N")

    (options, args) = parser.parse_args()
    if options.source_url:
        highlight_source_url()
        exit()
        
    if options.remote_ip:
        highlight_remote_ip()
        exit()
    
    if options.stat_remote_ip:
        stat_remote_ip(20) 
        exit()

    if options.loop_stat_remote_ip:
        loop_stat_remote_ip(20)
        exit()

    if options.stat_domain:
        stat_domain(20)
        exit()

    if options.stat_path:
        stat_path(20)
        exit()

    if options.loop_stat_domain:
        loop_stat_domain(20)
        exit()

    if options.loop_stat_path:
        loop_stat_path(20)
        exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as err:
        print("interrupt ok")
      
