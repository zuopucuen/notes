import pylibmc, web
from web.session import Store
    
class MemStore(Store): 
    def __init__(self): 
 
        self.mc = pylibmc.Client()
        self.timeout = web.config.session_parameters['timeout']
            
    def __contains__(self, key):
        return True if self.mc.get(key) else False  
            
    def __getitem__(self, key): 
        return self.mc.get(key)  
            
    def __setitem__(self, key, value):  
        self.mc.set(key, value, self.timeout)
            
    def __delitem__(self, key): 
        self.mc.delete(key)   
            
    def cleanup(self, timeout): 
        '''''You need nothing to do. Memcache can handle it.''' 
        pass

                                                                               