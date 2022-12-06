# singleton pattern
使用python實作singleton pattern
## 使用方式：

* python 裝飾器: 
```python=
def singleton(cls):
    _instance=dict()
    def inner(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]
        obj=cls(*args, **kwargs)
        _instance[cls]=obj
        return obj
    return inner
```
* python 裝飾器 : hasattr/getattr/setattr
```python=
def singleton_attr(cls):
    def inner(*args, **kwargs):
        if hasattr(cls,'__instance'):
            return getattr(cls,'__instance')
        obj=cls(*args, **kwargs)
        setattr(cls,'__instance',obj)
        return obj
    return inner
```
* python 裝飾器 : metaclass
```python=
class singleton_metaclass(type):
    def __call__(cls, *args, **kwargs):
        if hasattr(cls,'__instance'):
            return getattr(cls,'__instance')
        obj=super().__call__(*args, **kwargs)
        setattr(cls,'__instance',obj)
        return obj
```