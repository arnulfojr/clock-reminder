
import multiprocessing

from settings import HOST, PORT


bind = "{}:{}".format(HOST, PORT)

workers = multiprocessing.cpu_count() * 2 - 1

worker_class = 'sync'

threads = 2

accesslog = '-'

errorlog = '-'
