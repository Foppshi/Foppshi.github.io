#采购与招标信息网
#http://www.chinabidding.cn/
#中国电信外部门户招标信息
#http://42.99.33.26/MSS-PORTAL/account/login.do

import urllib.request
import re
import datetime
from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
