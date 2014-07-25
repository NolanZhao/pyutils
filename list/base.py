#!/usr/bin/env python
# encoding: utf-8

# source: https://github.com/defnull/bottle/blob/master/bottle.py
def makelist(data): # This is just to handy
    if isinstance(data, (tuple, list, set, dict)):
        return list(data)
    elif data:
        return [data]
    else:
        return []
