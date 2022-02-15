# stringprocess - process text entries

This is a simple library for easily customizable text processing pipelines.

It provides:

* a run-time registry of processors
* a simple mechanism for creating and automatically registering new processors
* a set of built-in processors
* an easy way to use the processors and pipe them together

The registry can be accessed thus:

```python3
from stringprocess import registry
```

The registry is just an {identifier:function} dict so it's easy to access the processors
or query, filter or generate simple documentation from them.

There are currently three types of processors:

* **removers** remove from input text
* **converters** replace parts of text
* **validators** drop whole input based on criteria

The built-in processors are listed in [PROCESSORS.md](PROCESSORS.md).

Writing a new one is as simple as adding a function to a, say,
`myconverters.py` module:

```python3

from stringprocess.processors.registry import converter

@converter("qr")
def quote_replacer(term):
   "replace double quotes with single quotes"
   return term.replace('"', "'")

```

To use the processor, it is only necessary that the module is imported before the registry is accessed (the decorator does the registration). So:

```python3

>>> import myconverters
>>> from stringprocess import process_terms

>>> terms = [
   'he said "who knows" and was silent',
   'and I responded "yes, who knows" and shrugged'
]
>>> tuple(process_terms('qr', terms))
("he said 'who knows' and was silent", "and I responded 'yes, who knows' and shrugged")
```

The built-in ones are registered automatically when the registry is imported.
