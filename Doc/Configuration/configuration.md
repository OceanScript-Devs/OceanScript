# Using the box configuration

This is the oceanscript box configuration which you'll need to refer to as a beginner.
To write the letter, simply find the letter in the boxes. The first character you want to write
is the symbol to the left of the letter - on the outer left column. Then, you want to write
the character above the letter, on the top row of the character's box. Finally, you want to add a dot,
multiplied by the number on the outer right column of the character.

```kt
[ ][<][-][>][ ]
[^][S][T][U][3]
[~][V][W][X][3]
[_][Y][Z][0][3]
```

If we were trying to write 'S', we'd look to the right first (``^``), then above (``<``) and then finally
add the number of dots equivalent to the number on the right (``...``). 'S' would therefore be ``^>...``.

Note: The other files in this directory were only written with the gradle extension because it makes the characters
easier to read with the highlighted syntax.
