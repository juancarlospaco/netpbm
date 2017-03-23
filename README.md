
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


- The Documentation uses `ImgColor` as Example, but `ImgGrayscale` and `ImgBW` share the same functions, since they all inherit from the same internal-only `__Bitmap` Dummy Base Private Class.


##### ImgColor
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



##### show
<details>

`netpbm.ImgColor.show()`

**Description:** Opens Image with browser or default program, auto-converts to PNG.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image = ImgColor(10, 10)
>>> image.show()
```
</details>



##### from_string
<details>

`netpbm.ImgColor.from_string(stringy: str)`

**Description:** Get Bitmap data from a string.
This first get contents as a UTF-8 string, removes all empty lines, strips the string,
gets Header data using a Regex, which includes Height of Bitmap,
then it slices lines from string from bottom to top according to Height, that gives the Bitmap data from the string slice,
make all strings to integers and sets them as Bitmap, returns that Bitmap.

**Arguments:**
- `stringy` A string with a valid image file, required, string type.

**Keyword Arguments:** None.

**Returns:** A Bitmap, a list of lists.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.from_string(open("image.ppm").read())
```
</details>



##### from_file
<details>

`netpbm.ImgColor.from_file(filepath: str)`

**Description:** Get Bitmap data from an existent valid file path string.
Internally is a shortcut to `netpbm.ImgColor.from_string()` that opens and reads the file.

**Arguments:**
- `filepath` A string with an existent valid image file path, required, string type.

**Keyword Arguments:** None.

**Returns:** A Bitmap, a list of lists.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.from_file("image.ppm")
```
</details>



##### get_header
<details>

`netpbm.ImgColor.get_header(data_str: str)`

**Description:** Get Header data using a Regex from an string.
Sets Header. Returns Header.

**Arguments:**
- `data_str` A string with an valid image file contents, required, string type.

**Keyword Arguments:** None.

**Returns:** A Header, one of `"P1"`, `"P2"`, `"P3"`, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.get_header(open("image.ppm").read())
```
</details>



##### get_mime_type
<details>

`netpbm.ImgColor.get_mime_type()`

**Description:** Get the mime type of the current image format as `'type/subtype'`.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** A MIME Type, string type.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.get_mime_type()
```
</details>



##### pprint
<details>

`netpbm.ImgColor.pprint()`

**Description:** Pretty Print to standard output the bitmap data matrix, a list of lists, using standard libs `pprint`.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.pprint()
```
</details>



##### set_datetime_as_comment
<details>

`netpbm.ImgColor.set_datetime_as_comment()`

**Description:** Set actual date and time UTC-aware ISO-Format as the comment.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.set_datetime_as_comment()
```
</details>



##### mirror_x
<details>

`netpbm.ImgColor.mirror_x()`

**Description:** Mirror image Horizontally.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.mirror_x()
```
</details>



##### mirror_y
<details>

`netpbm.ImgColor.mirror_y()`

**Description:** Mirror image Vertically.

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.mirror_y()
```
</details>



##### crop_x
<details>

`netpbm.ImgColor.crop_x(x: int)`

**Description:** Crop image Horizontally, crops from right-bottom, only can reduce size.

**Arguments:**
- `x` New Width for the Image, required, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.crop_x(5)
```
</details>



##### crop_y
<details>

`netpbm.ImgColor.crop_y(y: int)`

**Description:** Crop image Vertically, crops from right-bottom, only can reduce size.

**Arguments:**
- `y` New Height for the Image, required, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.crop_y(6)
```
</details>



##### crop
<details>

`netpbm.ImgColor.crop(x: int, y: int)`

**Description:** Crop image Horizontally and Vertically, crops from right-bottom, only can reduce size.
Internally is a shortcut to `crop_x()` and `crop_y()`.

**Arguments:**
- `x` New Width for the Image, required, integer type.
- `y` New Height for the Image, required, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.crop(6, 6)
```
</details>



##### crop_centered_x
<details>

`netpbm.ImgColor.crop_centered_x(x: int)`

**Description:** Centered Crop image Horizontally, crops from borders instead of from bottom-right, can  only reduce size.

**Arguments:**
- `x` New Width for the Image, required, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.crop_centered_x(6)
```
</details>



##### crop_centered_y
<details>

`netpbm.ImgColor.crop_centered_y(y: int)`

**Description:** Centered Crop image Vertically, crops from borders instead of from bottom-right, can  only reduce size.

**Arguments:**
- `y` New Height for the Image, required, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.crop_centered_y(6)
```
</details>



##### crop_centered
<details>

`netpbm.ImgColor.crop_centered(x: int, y: int)`

**Description:** Centered Crop image Horizontally and Vertically, crops from borders instead of from bottom-right, can  only reduce size.

**Arguments:**
- `x` New Width for the Image, required, integer type.
- `y` New Height for the Image, required, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.crop_centered(6, 6)
```
</details>



##### expand_x
<details>

`netpbm.ImgColor.expand_x(x: int)`

**Description:** Expand image Horizontally, grow from right-bottom, increments size.

**Arguments:**
- `x` New Width for the Image, required, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.expand_x(14)
```
</details>



##### expand_y
<details>

`netpbm.ImgColor.expand_y(y: int)`

**Description:** Expand image Vertically, grow from right-bottom, increments size.

**Arguments:**
- `y` New Height for the Image, required, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.expand_y(14)
```
</details>




##### expand
<details>

`netpbm.ImgColor.expand(x: int, y: int)`

**Description:** Expand image Horizontally and Vertically, grow from right-bottom, increments size.
Internally is shortcut to `expand_x()` and `expand_y()`.

**Arguments:**
- `x` New Width for the Image, required, integer type.
- `y` New Height for the Image, required, integer type.

**Keyword Arguments:** None.

**Returns:** None.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.expand_y(14)
```
</details>















# Why?

I cant find anything simple on pure Python without dependencies to make an image:
- https://github.com/search?l=Python&q=netpbm&type=Repositories&utf8=%E2%9C%93
- https://pypi.python.org/pypi?%3Aaction=search&term=netpbm&submit=search
