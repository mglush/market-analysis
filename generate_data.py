'''
File that runs the update files routine.
'''

from td_price_history import TdPriceHistory as Td

if __name__ == '__main__':
    util = Td()
    util.update_files('day', 10, 'minute', 1)
    util.update_files('year', 20, 'daily', 1)
