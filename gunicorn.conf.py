bind = "*:80"                   # Don't use port 80 becaue nginx occupied it already. 
errorlog = '/Users/seal/Desktop/oneoffnotes/gunicorn-error.log'  # Make sure you have the log folder create
accesslog = '/Users/seal/Desktop/oneoffnotes/gunicorn-access.log'
loglevel = 'debug'
workers = 1
