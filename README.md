
# netpbm

**NetPBM Raster Bitmap Pure Python 3.**

- No dependencies, Python 3.5+ standard libs only.
- No Pillow, No PIL, No Numpy, No Matplotlib, No Compilation required.
- Color (16M Colors), Grayscale (256 Colors) or Black&White (2 Colors).
- Object Class is Encoder and Decoder, `with` context manager support, chaining.
- PNG Export, JSON Import/Export, Pretty-Print to Terminal, etc.
- Useful manipulation functions, Darken, Lighten, Invert, Crop, Shrink, etc.
- Uses simple native Python lists, No Numpy Arrays.
- Single file.

For more information on the Standard see: https://en.wikipedia.org/wiki/Netpbm_format#PPM_example


# Examples

![Procedural](https://raw.githubusercontent.com/juancarlospaco/netpbm/master/example.jpg)

![Fractal](https://raw.githubusercontent.com/juancarlospaco/netpbm/master/fractalito.jpeg)

![Fractal](https://raw.githubusercontent.com/juancarlospaco/netpbm/master/fractalito_Vicsek.jpeg)

![Fractal](https://raw.githubusercontent.com/juancarlospaco/netpbm/master/fractalito_hexaflake.jpg)

![Fractal](https://raw.githubusercontent.com/juancarlospaco/netpbm/master/fractalito_snowflake.jpeg)

![Fractal](https://raw.githubusercontent.com/juancarlospaco/netpbm/master/fractalito_spiral.jpeg)

![Fractal](https://raw.githubusercontent.com/juancarlospaco/netpbm/master/fractalito_tri.jpeg)

Check [the Example file for fractal code](https://github.com/juancarlospaco/netpbm/blob/master/example_fractals.py).


# Reference


##### make_logger
<details>

`netpbm.ImgColor(width: int, height: int, bitmap: list, bg: int=0, comment: str="")`

**Description:** Make an Image object.

**Arguments:**
- `width` Width of Image, required, integer type.
- `height` Height of Image, required, integer type.
- `bitmap` A List of Lists with RGB values `[ [(R,G,B), ... ], ... ]` eg.`[ [(255,0,128), (10,0,250),], ]`, optional, a Blank image will be created if not provided, list type.
- `bg` Default Background color, optional, a Blank Background image will be used if not provided, list type.
- `comment` Comment for Image, optional, an Empty string comment image will be used if not provided, string type.

**Keyword Arguments:** None.

**Returns:** `ImgColor` object, a Color Image.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> ImgColor(10, 10)
```
</details>



# Why?

I cant find anything simple on pure Python without dependencies to make an image:
- https://github.com/search?l=Python&q=netpbm&type=Repositories&utf8=%E2%9C%93
- https://pypi.python.org/pypi?%3Aaction=search&term=netpbm&submit=search
