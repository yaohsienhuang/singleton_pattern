# decorator
def singleton(cls):
    _instance=dict()
    def inner(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]
        obj=cls(*args, **kwargs)
        _instance[cls]=obj
        return obj
    return inner

# decorator with attr
def singleton_attr(cls):
    def inner(*args, **kwargs):
        if hasattr(cls,'__instance'):
            return getattr(cls,'__instance')
        obj=cls(*args, **kwargs)
        setattr(cls,'__instance',obj)
        return obj
    return inner

# metaclass
class singleton_metaclass(type):
    def __call__(cls, *args, **kwargs):
        if hasattr(cls,'__instance'):
            return getattr(cls,'__instance')
        obj=super().__call__(*args, **kwargs)
        setattr(cls,'__instance',obj)
        return obj

@singleton
class human():
    pass

class human_meta(metaclass=singleton_metaclass):
    pass
    
    
if __name__=='__main__':
    
    h1=human()
    h2=human()
    print(h1 is h2)
    
    h3=human_meta()
    h4=human_meta()
    print(h3 is h4)