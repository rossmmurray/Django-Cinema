import logging
import sys


logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('output.log')
sh = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] - %(funcName)s - %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(fh)
# uncomment below for stdout output
# logger.addHandler(sh)

