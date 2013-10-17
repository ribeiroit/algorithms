#!/usr/bin/python
# 
# A little example to identify missing numbers in an arithmetic progression.
#
# al = progression
# r = progression's reason
#
# :)
al, r = [1, 5, 9], 2; print ([x for x in range(min(al),max(al),r) if x not in al])
