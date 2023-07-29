class MetaS(type):
    def __call__(cls, *args, **kwargs):
        istance = object.__new__(cls, *args, **kwargs)
        if cls not in cls._instance.keys():
            cls._instance[cls] = istance
        return cls._instance[cls]
    def __new__(cls, name, bases, attrs):
        attrs.update({'_instance':{}})
        return type.__new__(cls, name, bases, attrs)

class Hundred(metaclass=MetaS): 
	def __new__(cls): 
	    new_instance = super().__new__(cls) 
	    setattr(new_instance, 'name', 'hundred') 
	    setattr(new_instance, 'value', 100) 
	    return new_instance

#test

s = Hundred()
p = Hundred()
print("s is p:", s is p)
t = Hundred()
print("p is t:", p is t)
print("s is t:", s is t)
