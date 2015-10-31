
def wrapper(func):
    def checker(a, b): # 1
        if a.x < 0 or a.y < 0:
            a = 3
        if b.x < 0 or b.y < 0:
            b = 5
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = 12
        return ret
    return checker

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

#print get_text("John")

def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       print "Wrapper: "
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        print "Get Fullname"
        return self.name+" "+self.family

my_person = Person()

#print my_person.get_fullname()


#from functools import wraps
def my_decorator(f):
    #@wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        ret = f(*args, **kwds)
        print "Here: ", ret
        return ret
    return wrapper

@my_decorator
def example():
    """Docstring"""
    return 'Called example function'


example()