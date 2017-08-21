# -*- coding: utf-8 -*-

import asyncio
import os
import sys

#------------------------------------------------------------------------------

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root)

#------------------------------------------------------------------------------

import ccxt.async as ccxt  # noqa: E402

#------------------------------------------------------------------------------

async test_gdax():
    gdax = ccxt.gdax()
    print(await gdax.load_markets())

#------------------------------------------------------------------------------

asyncio.get_event_loop().run_until_complete(test_gdax()))