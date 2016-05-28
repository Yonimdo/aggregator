
from concurrent import futures

###
# takes a list of tupples  of (function , *args, **kwargs ) or a function as job
def do_jobs(job, *args, **kwargs):
    if type(job) != type(do_jobs):
        job = [(job, args, kwargs), ]
    with futures.ThreadPoolExecutor(max_workers=len(job)) as executor:
        for function in job:
            executor.submit(function[0], function[1], function[2])
