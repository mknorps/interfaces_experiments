# Interface implementation experiments

For more details see THIS blog post.

# How to run it?
Install virtual environment, open Python terminal and check 
where problems of different interface implementation apper/should have appeared. 
Feel free to extend the list of examples and post a PR.


# Structure
```bash
.
├── README.md
├── interfaces
│   ├── __init__.py
│   ├── formal.py
│   ├── functional.py
│   ├── informal.py
│   └── types.py
└── requirements.txt


```
# Examples

```python
import interfaces.informal as ii
import interfaces.formal as iform
import interfaces.functional as ifun
import interfaces.protocol as ip
```
First, try to initialize correct object:
```python
In [12] ii.XMLPeopleParserInformal()
Out[12]: <interfaces.informal.XMLPeopleParserInformal at 0x1079b6a90>

```
and then incorrect object:
```python
In [4]: ii.FaultyJsonPeopleParserInformal()
Out[4]: <interfaces.informal.FaultyJsonPeopleParserInformal at 0x105e417c0>

```

Now let's try to do the same for formal interface:
```python
In [13]: iform.XMLPeopleParserFormal()
Out[13]: <interfaces.formal.XMLPeopleParserFormal at 0x105d087f0>
```

and for formal interface we get an error on initialization:
```python
In [14]: iform.FaultyJsonPeopleParserFormal()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-9f9324518d0b> in <module>
----> 1 iform.FaultyJsonPeopleParserFormal()

TypeError: Can't instantiate abstract class FaultyJsonPeopleParserFormal with abstract method extract_persons

```

