<h1 align="center">
  <br>
  <a href="https://github.com/Kreusada/OceanScript"><img src="https://raw.githubusercontent.com/Kreusada/OceanScript/main/Resources/oceanscript.png" alt="OceanScript's Python Interpreter Implementation"></a>
  <br>
  OceanScript's Python Interpreter Implementation
  <br>
</h1>

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://user-images.githubusercontent.com/6032823/111363465-600fe880-8690-11eb-8377-ec1d4d5ff981.png)](https://github.com/PyCQA/isort)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

Oceanscript is built with a python interpreter, translator, encoder/decoder, whatever name
fits best. This small library available on PyPi contains two functions, used to encode and decode into oceanscript.

Start by importing the module.

```py
import oceanscript
```

Use the **encoder** method to convert normal text into oceanscript.

```py
oceanscript.encode('hello')
>>> '_-.~-.^>..^>..~>..'
```

Use the **decoder** method to convert oceanscript back into normal text.

```py
oceanscript.decode('_-.~-.^>..^>..~>..')
>>> 'hello'
```

Note that capitalization is ignored for both functions. Oceanscript doesn't and won't support
capitalization, numeracy, or punctuation - as that's not what it was designed for.

These functions may raise exceptions which you can access in the ``oceanscript.errors`` module.
They **all** subclass ``oceanscript.errors.OceanScriptError``.

The encoder can raise the ``UnsupportedCharacterError`` exception, when an unsupported character
is passed to the encoder. Only ascii letters and spaces are supported.

The decoder can also raise ``ParserError``, which is for when the decoder failed to parse a string.

This project is still in partial development. Use for fun, and provide feedback!
