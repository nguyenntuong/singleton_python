import threading
__singleton_instances_mn={}
#Python decorator for singleton pattern
def singleton(_class):
    global __singleton_instances_mn
    if _class.__name__ not in __singleton_instances_mn:
        def get_singleton(*args,**kargs):
            # Multithread locker
            locker = threading.Lock()
            locker.acquire()
            if _class.__name__ not in __singleton_instances_mn:
                __singleton_instances_mn[_class.__name__]=_class(*args,**kargs)
            locker.release()
            return __singleton_instances_mn[_class.__name__]
    else:
        def get_singleton():
            return __singleton_instances_mn[_class.__name__]
    return get_singleton
