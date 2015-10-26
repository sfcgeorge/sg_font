# SG Font Scripts

I designed a font using code, with my design-as-code tool [VectorSalad](https://github.com/sfcgeorge/vector_salad). Take a look at my scripts to for inspiration on how to script VectorSalad to do automated design, and script FontForge to generate fonts from SVG.

## Characters

Characters are defined in the `*.txt` files as plain text.
They must be 5 rows high but can be any width (typically 4).
Characters mean different things in the file:

* __.__ empty square
* __0__ square
* __1__ top-left rounded square
* __2__ top-right rounded square
* __3__ bottom-right rounded square
* __4__ bottom-left rounded square

## Generator

The script `generator.rb` will split up the `characters.txt` file and run the individual characters through the `character.rb` VectorSalad file, saving the results as SVGs.

```ruby
ruby generator.rb
```

## Character

The VectorSalad file `character.rb` generates a single character from a character string supplied as ARGV[0]. The string must have newlines replaced with just "n".
Generally this script isn't run directly but is run via `generator.rb`.

## FontForge

Now we can generate an actual font from the SVGs using FontForge.

```python
python fontgen.py
```
