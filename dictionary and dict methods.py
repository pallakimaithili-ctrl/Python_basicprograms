Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#dict()
a={"name":"lola","month":9,"year":2026}
type(a)
<class 'dict'>
#items()
a.items()
dict_items([('name', 'lola'), ('month', 9), ('year', 2026)])
#values()
a.values()
dict_values(['lola', 9, 2026])
#keys()
a.keys()
dict_keys(['name', 'month', 'year'])
#ways to get the value we want
a["year"]
2026
a["month"]
9
#can't get keys with values though
a[2026]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[2026]
KeyError: 2026
#get()
a.get("year")
2026
#update()
a.update{"day":"saturday","date":19}
SyntaxError: invalid syntax
a.update{"day":"saturday"},{"date":19}
SyntaxError: invalid syntax
#above are wrong methods
a.update({"day":"saturday","date":19})
a
{'name': 'lola', 'month': 9, 'year': 2026, 'day': 'saturday', 'date': 19}
#setdefault()
a={"hour":7,"min":23}
a.setdefault("sec",10)
10
a
{'hour': 7, 'min': 23, 'sec': 10}
>>> #pop()shouldn't be empty in dict
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop(sec)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.pop(sec)
NameError: name 'sec' is not defined. Did you mean: 'set'?
>>> a.pop("sec")
10
>>> a
{'hour': 7, 'min': 23}
>>> #popitem()
>>> a.popitem()
('min', 23)
>>> a
{'hour': 7}
>>> a={"colour":"black","food":"biryani"}
>>> #copy()
>>> a.copy()
{'colour': 'black', 'food': 'biryani'}
>>> #clear()
>>> a.clear()
>>> a
{}
>>> a={"name":"lola"}
>>> #what if we have two same keys
>>> b={"name":"lola","age":109,"name":"lily"}
>>> b
{'name': 'lily', 'age': 109}
>>> #so it is better to have different keys but we can still have same values
>>> #to stores multiple names without repeating it:
>>> a={"IDs":[10,20,30],"names":["lola","lily","lallu"]}
>>> a
{'IDs': [10, 20, 30], 'names': ['lola', 'lily', 'lallu']}
