# Ansi-Print (function aprint)
## Function to print (Ansi-)colored and (Ansi-)positioned text on Python3, no libraries used

### Why not using colorama or other already tested solution?
Basically, to train my Python. Also to aid in a future project, where I want as minimum dependencies as possible.

However, I recommend Colorama: [(link to pypi page)](https://pypi.python.org/pypi/colorama)   [(link to GitHub page)](https://github.com/tartley/colorama) if cross-compatibility is needed
(And/Or anything more robust than a random python script ;) )

### What can I do with this?

Print strings in a terminal( + clearing the screen). But with more options, like:

#### -Colors (foreground and background)
  * Available: black, white, blue, green, red, cyan, yellow, magenta

#### -Styling
  * Bold, italic, underline...

#### -Position
  * Position given in (line, collumn)

#### - ... and return to the line it was before
  * 'fix_line'
  *  Pseudo status messages;

Note: Some functions may not work in some terminals.

### Known Issues:
-Returning to the same line does not work in some X-terminal emulators/Shells. Styling probably also won't work on those terminals. Colors are widely supported.

-It is impossible to go to the very first and last line (due to Ansi); for now, it uses the last line for an optional "Status message".

## How can I use it?

1.Import it in your python interpreter/ script

2.Run the magic function:

To clear the screen:
```python
aclear()
```

To print:
```python
aprint('Foobar' {, ...}*)
```

Where '...' can be:

|Syntax            |Meaning                                            |Example                                      |
|------------------|---------------------------------------------------|---------------------------------------------|
|('c1','c2')       |colors the text: c1-font; c2-background            |`aprint('Foobar',('red','white'))           `|
|'style'           |styles the text;underline, bold, italic...         |`aprint('Foobar','italic','dim','underline')`|
|(line, collumn)   |prints string in specified line and collumn        |`aprint('Foobar', (20,30))                  `|
|'fix_line'        |after printing 'Foobar', return to current line    |`aprint('Foobar', 'fix_line')               `|
|('fix_line','s')  |same as fixline, but prints 's' under current line |`aprint('Foobar', ('fix_line','Written'))   `|

It is possible to combine commands:

```python
aprint('Foo', (40,100), 'underline', ('magenta','white'), ('fix_line','Bar') ,'bold')
```

### Accepted parameters:

-Colors:

  * black
  * red
  * green
  * yellow
  * blue
  * magenta
  * cyan
  * white

-Styles

  * reset
  * bold
  * dim
  * italic
  * underline
