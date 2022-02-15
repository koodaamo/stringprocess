# Built-in string processors

Processors are listed here categorized by type.
The two-letter codes after names are the pipeline identifiers
that can be used to combine processors to be run in a sequence.

For example a pipeline defined as `ws|rl|lc|le` would remove extra whitespace,
require letters, lowercase, and finally remove legal terms from the input.

The built-in processors are:

## Converters

### Case normalization - *lc*

Normalize (to lower-) case

### Diacritics conversion - *as*

Remove diacritics, turning e.g. umlauts into ascii counterparts

## Removers

### Legal entity stripping - *le*

Use cleanco to remove legal entity abbreviations such as inc. or ltd.

### Whitespace removal - *ws*

Remove multiple whitespaces and whitespace around dashes or dots

## Validators

### Require letter content - *rl*

See https://docs.python.org/3/library/re.html for what '\w' matches

