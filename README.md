# python-OOP-Lec9-25-JUN-25
args_kwargs

* args_kwargs: optional input parameter as a tuple, as a collection of values.
  * must be the last input parameter in the function signature.
    * if there are other parameters:
      * they are defined before the args 
      * without default values
  ```
  def print_numbers(x,*args):....
  
  print_numbers(1,2,3)
  ```
* kwargs: as key-word args: must be in the format of key=value
  * it's in a type of dictionary
```
 def print_numbers(x,**kwargs)...
 
 print_numbers(name='danny',age=30)

```

* decorator: a function that wraps another function and calls it, if needed, according to the decorator logic:
  * decorator must return the inner function
  * the inner function is usually called wrapper
  * implement decorator:
  ```
  def before_after(function_name):
    def wrapper(*args):
      print("before")
      function_name(*args)
      print("after")
    return wrapper
  ```    
  * usage: 
  ```
  @before_after
  def say_hello(a,b):
    print(a+b)
  
  say_hello(3,4)
  ```
    * the function say_hello doesn't immediately called, because of the decorator.
    * the decorator function is called first. 
    * than according to the wrapper function, the function say_hellow will be called
* the standard is to send the  

  