<h1 align="center">
  <br>
  <a href="https://github.com/OceanScript-Devs/OceanScript"><img src="https://raw.githubusercontent.com/Kreusada/OceanScript/main/Resources/oceanscript.png" alt="OceanScript Esoteric Language"></a>
  <br>
  OceanScript Esoteric Language
  <br>
</h1>

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://user-images.githubusercontent.com/6032823/111363465-600fe880-8690-11eb-8377-ec1d4d5ff981.png)](https://github.com/PyCQA/isort)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

Welcome! This library is home to oceanscript - An extensive esolang built with a python interpreter.
It's purpose is simple - for fun. This "esolang" shouldn't be used for anything more than a bit
of fun, but also can be used for mind games, as it takes infuriatingly long just to write a single
sentence.

Oceanscript was given it's name due to the fact that the script looks like waves in the ocean when it is written.
See the image above, for example.

It's sheer complexity means that nothing is supported aside from alphanumeric characters. Punctuation is unsupported.
Capitalization is ignored. You'll see why further down this page.

Oceanscript uses a range of three to six characters PER letter, with each letter joined together, and each *word* joined
together by a line break. A single word can take up quite a few spaces on each line of a document or notepad.

Let's start of with a basic example - to see what I'm really talking about:

```alp
_-.~-.^>..^>..~>..
~-...~>.._>..^>..~<.
```

Yep. Complicated right? The text you see above says "hello world". Don't worry -  it really is much easier
to understand when we learn how the letter structure works.

### Building letters

Visualize **4** boxes. Each box has **9** squares inside, with **3** columns, and **3** rows.
So basically, four 3x3 boxes. This is what we need to start building our letters.

```alp
# Box 1
[A] [B] [C]
[D] [E] [F]
[G] [H] [I]

# Box 2
[J] [K] [L]
[M] [N] [O]
[P] [Q] [R]

# Box 3
[S] [T] [U]
[V] [W] [X]
[Y] [Z] [0]

# Box 4
[1] [2] [3]
[4] [5] [6]
[7] [8] [9]
```

Each letter and number has its own square in this configuration. However, each column and row in this configuration
are joined together. For example, this means that A, D, G, J, M, P, S, V, Y, 1, 4 and 7 are all in column 1.

We need to first take a look at our **markers**. These are essentially pointers towards where our letter is in
this configuration. The following characters are known as markers: which make up oceanscript as a whole.

### Markers

* ``^``: Denotes the **top** row
* ``~``: Denotes the **middle** row
* ``_``: Denotes the **bottom** row

* ``<``: Denotes the **left** column
* ``-``: Denotes the **middle** column
* ``>``: Denotes the **right** column

* ``.``: Denotes box **1**
* ``..``: Denotes box **2**
* ``...``: Denotes box **3**
* ``....``: Denotes box **4**

We use the markers in the following order: ``row -> column -> box``. Let's start of with an example, with letter A.
We will zoom in on A's box, so it's slighty easier for us:

```alp
# Box 1
[A] [B] [C]
[D] [E] [F]
[G] [H] [I]
```

We need to first identify the row for letter A - it's on the top row in our box. Now let's refer back to our markers.
The top row character is a carot (``^``). This character signifies the top row, as it's pointing upwards.
This is the first character for our letter A in oceanscript!

Next, we need to find out the column for our letter. A is in the left column, so looking at our markers, our next character
is a less than sign (``<``). This character signifies the left column, as it's pointing left.

Finally, we need to identify the box our letter is in. It's clearly in box **1**, so we add **1** dot to the end of our character.

This means that the letter A in oceanscript is ``^<.``.

It's really important to reference from the boxes. It's very difficult to memorise the boxes in your head. However, with time,
you will be able to memorise the markers.

You can see more how-to guides in the Doc directory.

## Python Implementation

Oceanscript is built with a python interpreter, translator, encoder/decoder, whatever name
fits best. This small library available on PyPi contains two functions, used to encode and decode into oceanscript.

Start by importing the module.

```py
import oceanscript
```

Use the **encode** function to convert normal text into oceanscript.

```py
oceanscript.encode('hello')
>>> '_-.~-.^>..^>..~>..'
```

Use the **decode** function to convert oceanscript back into normal text.

```py
oceanscript.decode('_-.~-.^>..^>..~>..')
>>> 'hello'
```

Note that capitalization is ignored for both functions. Oceanscript doesn't and won't support
capitalization or punctuation - as that's not what it was designed for.

These functions may raise exceptions which you can access in the ``oceanscript.errors`` module.
They **all** subclass ``oceanscript.errors.OceanScriptError``.

The encoder can raise the ``UnsupportedCharacterError`` exception, when an unsupported character
is passed to the encoder. Only ascii letters and spaces are supported.

The decoder can also raise ``ParserError``, which is for when the decoder failed to parse a string.

This project is still in partial development. Use for fun, and provide feedback!

## Command Line Interface

As well as it's standard python implementation, OceanScript also has a command line interface 
(built with argparse) which allows you to encode and decode oceanscript.

Top level command name is ``oceanscript``.

```sh
$ oceanscript
```

Use the ``--encode`` and ``--decode`` arguments to convert oceanscript to and from.

```sh
$ oceanscript --encode testing
>>> 'Encoded oceanscript: ^-...~-.^<...^-..._>.~-.._<.'

$ oceanscript --decode "^-...~-.^<...^-..._>.~-.._<."
>>> 'Decoded oceanscript: testing'
```

It's important that you wrap your decode arguments with quotation marks. Most noticeably, important
oceanscript characters cannot be parsed due to the nature of command line interfaces.

## License

This project is under the MIT license.
