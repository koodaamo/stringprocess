from stringprocess.processors.registry import remover, converter, validator, registry, TYPES
from stringprocess import process_term, process_terms


def test_custom_transformer():
   "custom remover can be created, registered and used"

   KEY = "dr"

   @remover(KEY)
   def dummyremover(term):
      "just a dummy remover"
      return term.replace("dummy", "")


   customremover = registry[KEY]
   assert customremover("dummyremoved") == "removed"


def test_custom_converter():
   "custom converter can be created, registered and used"

   KEY = "nc"

   @converter(KEY)
   def notconverter(term):
      "pass-through converter"
      return term
    
   customconverter = registry[KEY]
   assert customconverter("nochange") == "nochange"


def test_term_transform():

   KEY = "nc"

   @converter(KEY)
   def notconverter(term):
      "pass-through converter"
      return term
   
   assert process_term(KEY, "nochange") == "nochange"


def test_termlist_transforms():

   KEY = "nc"

   @converter(KEY)
   def notconverter(term):
      "pass-through converter"
      return term

   terms = ("nochange1", "nochange2", "nochange3")
   assert tuple(process_terms(KEY, terms)) == terms


def test_termlist_validation():

   KEY = "rl"

   @validator(KEY)
   def nostars(term):
      "do not allow terms with * chars"
      return None if "*" in term else term

   terms = ("nochange1", "**a**", "nochange3")
   result = tuple(process_terms(KEY, terms))
   assert result == (terms[0], terms[2])