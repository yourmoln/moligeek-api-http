import sys,os
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(script_path)


import core.network as network
import core.localhost as localhost