# -*- coding: utf-8 -*-
#!/usr/bin/python

'''
    Author: Mert Saygı
    This is a script for making cron automatize account payments
'''

if __name__ == "__main__":

    if not os.geteuid() == 0:
        sys.exit('Script must be run as root')