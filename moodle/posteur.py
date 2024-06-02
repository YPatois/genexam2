#!/usr/bin/env python3
from moodle import Moodle

from myauth import mtoken, murl

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
  moodle = Moodle(murl, mtoken)
  dict_site_info = moodle('core_webservice_get_site_info')
  site_info = moodle.core.webservice.get_site_info()  # return typed site_info

  print(dict_site_info)
  print(site_info)


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

