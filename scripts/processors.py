from itertools import groupby
from stringprocess.processors import converters, removers, validators
from stringprocess import registry


with open("PROCESSORS.in", "r") as input:
   intro = input.read()

with open("PROCESSORS.md", "w") as output:
   output.write(intro)
   for category, processors in groupby(registry.items(), lambda i: i[1].type):
      category = category.name.lower().capitalize() + "s"
      output.write(f"## {category}\n\n")
      for key, func in processors:
         name = func.__name__.capitalize().replace("_", " ")
         doc = func.__doc__.capitalize()
         output.write(f"### {name} - *{key}*\n\n{doc}\n\n")
   
