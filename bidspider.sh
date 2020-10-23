#!/bin/sh
echo "start shell run python file"
cd /usr/local/workspace-bid-spider/ && python GJU.py && python processBidSpider.py
