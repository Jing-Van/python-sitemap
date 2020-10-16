#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

import crawler

parser = argparse.ArgumentParser(description='Python SiteMap Crawler')
parser.add_argument('--skipext', action="append", default=[], required=False, help="File extension to skip")
parser.add_argument('-n', '--num-workers', type=int, default=1, help="Number of workers if multithreading")
parser.add_argument('--parserobots', action="store_true", default=False, required=False, help="Ignore file defined in robots.txt")
parser.add_argument('--debug', action="store_true", default=False, help="Enable debug mode")
parser.add_argument('-v', '--verbose', action="store_true", help="Enable verbose output")
parser.add_argument('--output', action="store", default=None, help="Output file")
parser.add_argument('--exclude', action="append", default=[], required=False, help="Exclude Url if contain")
parser.add_argument('--drop', action="append", default=[], required=False, help="Drop a string from the url")
parser.add_argument('--report', action="store_true", default=False, required=False, help="Display a report")
parser.add_argument('--images', action="store_true", default=False, required=False, help="Add image to sitemap.xml (see https://support.google.com/webmasters/answer/178636?hl=en)")

group = parser.add_mutually_exclusive_group()
group.add_argument('--domain', action="store", default="", help="Target domain (ex: https://www.sedna.com)")

arg = parser.parse_args()

dict_arg = arg.__dict__

if dict_arg["domain"] == "":
	print ("You must provide a domain to use the crawler.")
	exit()

crawl = crawler.Crawler(**dict_arg)
crawl.run()

if arg.report:
	crawl.make_report()
