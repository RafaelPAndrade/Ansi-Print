# Ansi-Print(function aprint)
## Function to print (Ansi-)colored and (Ansi-)positioned text on Python3, no libraries used

### Why not using colorama or other already tested solution?
Basically, to train my Python. Also to aid in a future project, where I want as minimum dependencies as possible.

### What can I do with this?
Print strings in a terminal. But with more options, like:
#### -Colors (foreground and background)
  * Available:black, white, blue, green, red, cyan, yellow, magenta
#### -Styling
  * Bold, italic, underline, reverse...
#### -Position
  * Position given in (line, collumn)
#### - ... and return to the line it was before
  * 'fix_line'
Note: Some.

## How can I use it?

1.Load it in your python interpreter/ script

2.Run the magic function:

```python
aprint('Foobar', ...)
```

