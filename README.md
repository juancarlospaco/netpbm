
# netpbm

**NetPBM Raster Bitmap Pure Python 3.**

[![GPL License](http://img.shields.io/badge/license-GPL-blue.svg)](http://opensource.org/licenses/GPL-3.0)
[![LGPL License](http://img.shields.io/badge/license-LGPL-blue.svg)](http://opensource.org/licenses/LGPL-3.0)
[![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg)](http://python.org)

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
- Encoding is always `utf-8` for proper Unicode support, unless explicitly stated otherwise.

##### ImgColor
<details>

`netpbm.ImgColor(width: int, height: int, bitmap: list, bg: int=0, comment: str="")`

**Description:** Make an Image object.

**Arguments:**
- `width` Width of Image, required, integer type.
- `height` Height of Image, required, integer type.
- `bitmap` A List of Lists with RGB values `[ [(R,G,B), ... ], ... ]` eg.`[ [(255,0,128), (10,0,250),], ]`, basically a Matrix of Integers, optional, a Blank image will be created if not provided, list type.
- `bg` Default Background color, optional, a Blank Background image will be used if not provided, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`.
- `comment` Comment for Image, optional, an Empty string will be used if not provided, string type.

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
Internally it uses Python standard libs `mimetypes.guess_type()`.

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

**Description:** Pretty Print to standard output the bitmap data matrix, a list of lists.
Internally it uses Pythons standard libs `pprint.pprint()`.

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
eg. `'2017-03-24 07:49:57-03:00'`.
Internally is shortcut to `datetime.datetime.now(datetime.timezone.utc).replace(
    microsecond=0).astimezone().isoformat(" ")`.

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
This can not resize the contents, only crops the canvas.

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
This can not resize the contents, only crops the canvas.

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
This can not resize the contents, only crops the canvas.
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
This can not resize the contents, only crops the canvas.

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
This can not resize the contents, only crops the canvas.

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
This can not resize the contents, only crops the canvas.

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
This can not resize the contents, only expands the canvas.

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
It only resizes the canvas.
This can not resize the contents, only expands the canvas.

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
This can not resize the contents, only expands the canvas.

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
>>> image.expand(14, 14)
```
</details>



##### expand_centered_x
<details>

`netpbm.ImgColor.expand_centered_x(x: int)`

**Description:** Expand image centered Horizontally, grow from right-bottom, increments size.
This can not resize the contents, only expands the canvas.

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
>>> image.expand_centered_x(14)
```
</details>



##### expand_centered_y
<details>

`netpbm.ImgColor.expand_centered_y(y: int)`

**Description:** Expand image Centered Vertically, grow from right-bottom, increments size.
This can not resize the contents, only expands the canvas.

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
>>> image.expand_centered_y(14)
```
</details>



##### expand_centered
<details>

`netpbm.ImgColor.expand_centered(x: int, y: int)`

**Description:** Expand image Centered Horizontally and Vertically, grow from right-bottom, increments size. This can not resize the contents, only expands the canvas.
Internally is shortcut to `expand_centered_x()` and `expand_centered_y()`.

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
>>> image.expand_centered(14, 14)
```
</details>



##### shrink_x
<details>

`netpbm.ImgColor.shrink_x(x: int)`

**Description:** Shrink image horizontally.
It resizes the Bitmap contents itself AND resizes the canvas too. Can only reduce sizes.

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
>>> image.shrink_x(6)
```
</details>



##### shrink_y
<details>

`netpbm.ImgColor.shrink_y(y: int)`

**Description:** Shrink image vertically.
It resizes the Bitmap contents itself AND resizes the canvas too. Can only reduce sizes.

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
>>> image.shrink_y(6)
```
</details>



##### shrink
<details>

`netpbm.ImgColor.shrink(x: int, y: int)`

**Description:** Shrink image horizontally and vertically.
It resizes the Bitmap contents itself AND resizes the canvas too. Can only reduce sizes.
Internally is shortcut to `shrink_x()` and `shrink_y()`.

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
>>> image.shrink(8, 6)
```
</details>



##### lighten
<details>

`netpbm.ImgColor.lighten(amount: int)`

**Description:** Lighten the image according to amount argument.
Do nothing on Black&White images.
Lets imagine your Pixel RGB is `(0, 128, 255)` you set `amount` to `10`,
then it will add `10` to each integer, always on valid limits of `0` or `255`,
then your RGB is `(10, 138, 255)`.

**Arguments:**
- `amount` The amount of lightening to apply to the image, required, integer type.

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
>>> image.lighten(2)
```
</details>



##### darken
<details>

`netpbm.ImgColor.darken(amount: int)`

**Description:** Darken the image according to amount argument.
Do nothing on Black&White images.
Lets imagine your Pixel RGB is `(0, 128, 255)` you set `amount` to `10`,
then it will substract `10` to each integer, always on valid limits of `0` or `255`,
then your RGB is `(0, 118, 245)`.

**Arguments:**
- `amount` The amount of darkening to apply to the image, required, integer type.

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
>>> image.darken(2)
```
</details>



##### fillrect
<details>

`netpbm.ImgColor.fillrect( x: int, y: int, width: int, height: int, color: list=None)`

**Description:** Fill up a rectangle or square on the image with given color.
If no `color` provided then default background color will be used.

**Arguments:**
- `x` Position on the horizontal X axis on the canvas, required, integer type.
- `y` Position on the vertical Y axis on the canvas, required, integer type.
- `width` Width of the rectangle or square, required, integer type.
- `height` Height of the rectangle or square, required, integer type.
- `color` Color of the rectangle or square, optional,
default background color will be used if not provided, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`..

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
>>> image.fillrect(2, 2, 4, 4, [128, 128, 128])
```
</details>



##### fillrect_stripe_x
<details>

`netpbm.ImgColor.fillrect_stripe_x( x: int, y: int, width: int, height: int, color0: list, color1: list, stroke: int)`

**Description:** Fill up a rectangle or square on the image with given colors
using an stripped horizontal pattern of lines of given stroke thickness.
Requires 2 colors for the stripped pattern.

**Arguments:**
- `x` Position on the horizontal X axis on the canvas, required, integer type.
- `y` Position on the vertical Y axis on the canvas, required, integer type.
- `width` Width of the rectangle or square, required, integer type.
- `height` Height of the rectangle or square, required, integer type.
- `color0` Color of the rectangle or square, required, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`..
- `color1` Color of the rectangle or square, required, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`..
- `stroke` Stroke of thickness of the stripped pattern lines, required, integer type.

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
>>> image.fillrect_stripe_x(2, 2, 4, 4, [128, 128, 128], [99, 99, 99], 2)
```
</details>



##### fillrect_stripe_y
<details>

`netpbm.ImgColor.fillrect_stripe_y( x: int, y: int, width: int, height: int, color0: list, color1: list, stroke: int)`

**Description:** Fill up a rectangle or square on the image with given colors
using an stripped vertical pattern of lines of given stroke thickness.
Requires 2 colors for the stripped pattern.

**Arguments:**
- `x` Position on the horizontal X axis on the canvas, required, integer type.
- `y` Position on the vertical Y axis on the canvas, required, integer type.
- `width` Width of the rectangle or square, required, integer type.
- `height` Height of the rectangle or square, required, integer type.
- `color0` Color of the rectangle or square, required, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`..
- `color1` Color of the rectangle or square, required, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`..
- `stroke` Stroke of thickness of the stripped pattern lines, required, integer type.

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
>>> image.fillrect_stripe_y(2, 2, 4, 4, [128, 128, 128], [99, 99, 99], 2)
```
</details>



##### fillrect_grid
<details>

`netpbm.ImgColor.fillrect_grid( x: int, y: int, width: int, height: int, color0: list, color1: list, stroke: int)`

**Description:** Fill up a rectangle or square on the image with given colors
using a Grid pattern of horizontal and vertical lines of given stroke thickness.
Requires 2 colors for the grid pattern.

**Arguments:**
- `x` Position on the horizontal X axis on the canvas, required, integer type.
- `y` Position on the vertical Y axis on the canvas, required, integer type.
- `width` Width of the rectangle or square, required, integer type.
- `height` Height of the rectangle or square, required, integer type.
- `color0` Color of the rectangle or square, required, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`..
- `color1` Color of the rectangle or square, required, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`..
- `stroke` Stroke of thickness of the grid pattern lines, required, integer type.

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
>>> image.fillrect_grid(2, 2, 4, 4, [128, 128, 128], [99, 99, 99], 2)
```
</details>



##### fillrect_dotted
<details>

`netpbm.ImgColor.fillrect_dotted( x: int, y: int, width: int, height: int, color0: list, color1: list, stroke: int)`

**Description:** Fill up a rectangle or square on the image with given colors
using a Dotted pattern of horizontal and vertical Dots of given stroke thickness.
Requires 2 colors for the Dotted pattern.

**Arguments:**
- `x` Position on the horizontal X axis on the canvas, required, integer type.
- `y` Position on the vertical Y axis on the canvas, required, integer type.
- `width` Width of the rectangle or square, required, integer type.
- `height` Height of the rectangle or square, required, integer type.
- `color0` Color of the rectangle or square, required, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`..
- `color1` Color of the rectangle or square, required, list type for Color images, eg `[0,0,0]`, integer for Black&White and Grayscale images, eg `0`..
- `stroke` Stroke of thickness of the Dot pattern, required, integer type.

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
>>> image.fillrect_dotted(2, 2, 4, 4, [128, 128, 128], [99, 99, 99], 2)
```
</details>



##### fillrect_random
<details>

`netpbm.ImgColor.fillrect_random( x: int, y: int, width: int, height: int)`

**Description:** Fill up a rectangle or square on the image with Random colors
using a Random pattern of Random Pixels.

**Arguments:**
- `x` Position on the horizontal X axis on the canvas, required, integer type.
- `y` Position on the vertical Y axis on the canvas, required, integer type.
- `width` Width of the rectangle or square, required, integer type.
- `height` Height of the rectangle or square, required, integer type.

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
>>> image.fillrect_random(2, 2, 4, 4)
```
</details>



##### to_file
<details>

`netpbm.ImgColor.to_file(fyle: str)`

**Description:** Write everything to a file.
Write the full contents of the actual current Image instance to a local file full path string of proper format and extension.
File extension will be added automatically if file extension is not provided.
File extension will be added automatically if file extension is not correct.
File extension for Black&White images is `*.pbm`.
File extension for Grayscale images is `*.ppm`.
File extension for Color images is `*.pgm`.

**Arguments:**
- `fyle` local file path string of proper format and extension.

**Keyword Arguments:** None.

**Returns:** Local file path string of new file created.

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
>>> image.to_file("my_image_file")
```
</details>



##### to_png
<details>

`netpbm.ImgColor.to_png(fyle: str)`

**Description:** Write everything to a PNG file.
Write the full contents of the actual current Image instance to a local file full path string of `*.PNG` format and extension.
File extension will be added automatically if file extension is not provided.
File extension will be added automatically if file extension is not correct.
This uses `pnm2png` executable command line program of the system.
`pnm2png` executable must be working Ok on the system.

**Arguments:**
- `fyle` local file path string of `*.PNG` file extension.

**Keyword Arguments:** None.

**Returns:** Local file path string of new `*.PNG` file created.

**Source Code file:** https://github.com/juancarlospaco/anglerfish/blob/master/anglerfish/netpbm.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :question:         | **Os X**    | Unknown     |
| :question:         | **Windows** | Unknown     |

**Usage Example:**

```python
>>> from netpbm import ImgColor
>>> image= ImgColor(10, 10)
>>> image.to_png("my_png_image_file")
```
</details>



##### to_json
<details>

`netpbm.ImgColor.to_json(fyle: str=None)`

**Description:** Write everything to a JSON string, file or standard output.
Write the full contents of the actual current Image instance to a local JSON file full path string of `*.json` file extension.
File extension will be added automatically if file extension is not provided.
File extension will be added automatically if file extension is not correct.
If `fyle` is not provided then it will return the JSON. This serializes data to JSON.

**Arguments:**
- `fyle` local file path string of `*.json` file extension.
If not provided then it will return the JSON.

**Keyword Arguments:** None.

**Returns:** Local file path string of new `*.json` file created or the JSON string itself.

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
>>> image.to_json("my_json_file")
```
</details>



##### from_json
<details>

`netpbm.ImgColor.from_json(file_or_json: str=None)`

**Description:** Reads everything from a JSON file or string.
Reads the full contents for the actual Image instance from a local JSON file full path string of `*.json` file extension or JSON string itself.
File extension must be provided. File extension will Not be added automatically.
If `file_or_json` is a string with the JSON then it will be used directly as Image data.
This deserializes data from JSON.

**Arguments:**
- `file_or_json` local file path string of `*.json` file or JSON string.

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
>>> image.from_json("my_json_file.json")
```
</details>



##### set_random_bitmap
<details>

`netpbm.ImgColor.set_random_bitmap()`

**Description:** Makes a Random bitmap image.
Fills up all pixels of the Image with Random pixels.

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
>>> image.set_random_bitmap()
```
</details>



##### invert_colors
<details>

`netpbm.ImgColor.invert_colors()`

**Description:** Inverts the image colors.
Inverts all pixels of the Image with the opposite color of pixels.

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
>>> image.invert_colors()
```
</details>

- The Class has `__enter__()`, `__exit__()` and `__str__()` magic methods. Has `with` context manager and chaining support.


# Requisites:

- [Python 3.5+](https://www.python.org "Python Homepage")


# Coding Style Guide:

- Lint, [PEP-8](https://www.python.org/dev/peps/pep-0008), [PEP-257](https://www.python.org/dev/peps/pep-0257), [PyLama](https://github.com/klen/pylama#-pylama), [iSort](https://github.com/timothycrosley/isort) must Pass Ok. `pip install --upgrade pep8 pep257 pylama isort pytest`


# Why?

I cant find anything simple on pure Python without dependencies to make an image with a simple matrix of integers:
- https://github.com/search?l=Python&q=netpbm&type=Repositories&utf8=%E2%9C%93
- https://pypi.python.org/pypi?%3Aaction=search&term=netpbm&submit=search
- Because I can.


# Licence:

- GNU GPL Latest Version *AND* GNU LGPL Latest Version *AND* any Licence YOU Request via Bug Report.


# Ethics and Humanism Policy:

- Politics and Religions is not allowed.
- This project has Feminism Ally conduct.
