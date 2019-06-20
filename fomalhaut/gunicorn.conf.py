import multiprocessing

bind = "127.0.0.1:8000"   
workers = 2                
errorlog = './gunicorn.error.log' 
accesslog = './gunicorn.access.log'
proc_name = 'gunicorn_project'
