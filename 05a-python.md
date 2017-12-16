# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are the same in that they are containers. They can hold a sequence of objects and support elements of any type and maintain order. Lists can be identified in syntax via the [] while tuples use (). Inside both container, commas are used to separate the elements from one another. Tuples are immutable and thus their elements cannot be altered. For these reasons methods such as .append() don't exist in tuples. They also are more memory efficient since its length is set. Lists are mutable and can be changed and thus have many methods that can alter its contents available to it. Because its length can change at any given time, memory allocation is generous to accomodate for methods such as append(). Since only immutable objects can be keys in a dictionary, tuples are best suited for this job. In order for a list to be used as keys in a dictionary, these need to be first converted to tuples. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are the same in that they are both containers. I went into a bit of detail in the previous question about lists. Sets contain unordered unique elements since sets cannot contain duplicates. Sets have methods to alter the contents and operations such as intersection, union, difference, and symmetric difference (operations of math's set theory). It uses {} as its syntax. As far as performance, sets are faster when looking for an element in the container using "in". However, looping through it is much slower than that in a list.
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a construct in which an anonymous function is created using a simple expression and that has a return value which works on the fly. It is especially useful because of its compactness when using methods such as sorted where lambda can be used to evaluate each element right before being compared.
```
student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('dave', 'B', 10) ]

>>>sorted(student_tuples, key=lambda student: student[2])
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions is a construct derived from mathematical notations that outputs a list. It has an expression followed by a for clause, then
possibly more for or even if clauses within brackets typical of a list construct. The expressions can be anything, meaning you can
put in all kinds of objects in lists.
```
new_list = [expression(i) for i in old_list if filter(i)]
```
>>Map and filter functions can be used alongside with lambda to make a construct with similar output as that to list comprehensions. Map and filter by themselves seem to call for the creation of an extra function everytime it goes through items in the iterable which makes its performance slightly slower to that of a list comprehension. The usage of lambda is restricted to a simple expression while a list comprehesion can have more than one "for" and even "if" clauses.

```
map(func, iterable)

a = [1,2,3,4]
b = [17,12,11,10]
r = list(map(lambda x,y:x+y, a,b))
[18, 14, 14, 14]

using list comprehension

r = [x + b[y] for y,x in enumerate(a)]
[18, 14, 14, 14]

```
```
filter(func, iterable)

c = [0,1,1,2,3,5,8,13,21,34,55]
r = list(filter(lambda x: x % 2==0, c))
[0, 2, 8, 34]

using list comprehension

r = [x for x in c if x%2 == 0]
[0, 2, 8, 34]
```
>> Dictionary comprehensions follow the same format as list comprehensions but have a dictionary as an output instead. The syntax enveloping the construct is {}.

```
dictionary comprehension 
r = { x: x**2 for x in a}
{1: 1, 2: 4, 3: 9, 4: 16}

```
>> Set comprehensions follow the same as the list and dictionary comprehensions. They too are enclosed by curly braces. However the result is not a distionary but a set. This construct was added by Python 3. The following example uses the same code as that for list comprehension above. Notice the result is a set with unique elements.
```
r = {x + b[y] for y,x in enumerate(a)}
{18, 14}

```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'

```

>> 937 days, 0:00:00

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days
```
c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





