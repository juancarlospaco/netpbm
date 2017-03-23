#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""NetPBM Raster Bitmap Pure-Python Image."""


import datetime
import os
import re

from json import dumps, loads
from mimetypes import guess_type
from pprint import pprint
from random import randint
from shutil import which
from subprocess import run
from tempfile import NamedTemporaryFile
from webbrowser import open_new_tab


__version__ = "0.0.1"
__license__ = "GPLv3+ LGPLv3+"
__author__ = "Juan Carlos"
__all__ = ("ImgColor", "ImgBW", "ImgGrayscale")


_NETPBM = """{header}\n# {comment}\n{width} {height}\n{maxvalue}\n{data}"""


class __Bitmap(object):

    """Base Class Raster Graphic Image, using a list of lists."""

    def __init__(self, width, height, bitmap=None, bg=0, comment=""):
        self.bg, self.comment, self.ext = int(bg), str(comment).strip(), ""
        self.width, self.height = int(abs(width)), int(abs(height))
        self.header, self.maxvalue = None, None
        self.map = list(bitmap) if bitmap else None
        self.init_bitmap()
        self._auto_adjust_size()

    def write(self, filename):
        """Write itself to file."""
        filename = filename if filename else NamedTemporaryFile().name
        return self.to_file(filename)

    def close(self):
        """Close actions if any, actually none required."""
        pass

    def __enter__(self, *args, **kwargs):
        """Used for context manager for 'with'."""
        return self

    def __exit__(self, *args, **kwargs):
        """Used for context manager for 'with'."""
        return self.close()

    def init_bitmap(self):
        """Method can be override with an initial value for the Bitmap."""
        raise NotImplementedError("eeffoc dna snettik erom deen"[::-1])

    def show(self):
        """Open with browser or default program,autoconverts to PNG."""
        return open_new_tab(self.to_png(NamedTemporaryFile().name))

    def from_string(self, stringy):
        """Get Bitmap data from a string.

        This first get contents as a UTF-8 str,removes empty lines,strips,
        gets Header data using a Regex, which includes Height of Bitmap,
        then slice lines from string from bottom to top according to Height,
        make all str to int and sets them as Bitmap, returns Bitmap."""
        strng = "\n".join([_ for _ in stringy.strip().split("\n") if _])
        self.get_header(strng)
        _temp = [_.split() for _ in strng.splitlines()[-self.height::]]
        lst = [[int(_) for _ in x] for x in _temp]
        if self.header in ("P1", "P2"):  # List of integers [ [0,255,...], ]
            self.map = lst
        else:  # List of lists [ [ [R,G,B], ... ], ]
            self.map = [[x[_:_ + 3] for _ in range(0, len(x), 3)] for x in lst]
        return self.map

    def from_file(self, filepath):
        """Get data from a file path string,this sets bitmap,header,etc."""
        if os.path.isfile(filepath):
            with open(filepath, encoding="utf-8") as _file:
                self.from_string(_file.read())
            return self.map

    def get_header(self, data_str):
        """Get header data using a Regex from argument string."""
        re_groups = re.search("".join((
            r"(^(P[123])\s+(?:#.*[\r\n])*",
            r"\s*(\d+)\s+(?:#.*[\r\n])*",
            r"\s*(\d+)\s+(?:#.*[\r\n])*",
            r"\s*(\d+)\s(?:\s*#.*[\r\n]\s)*)")), data_str).groups()
        self.header, self.maxvalue = re_groups[1], int(re_groups[4])
        self.width, self.height = int(re_groups[2]), int(re_groups[3])
        return self.header

    def get_mime_type(self):
        """Get the mime type of the current image format as 'type/subtype'."""
        return guess_type("file" + self.ext)[0]

    def pprint(self):
        """Pretty Print the bitmap data matrix using std lib pprint."""
        return pprint(self.map, indent=4)

    def set_datetime_as_comment(self):
        """Set actual date and time UTC-aware ISO-Format as the comment."""
        self.comment = datetime.datetime.now(datetime.timezone.utc).replace(
            microsecond=0).astimezone().isoformat(" ")
        return self

    def _auto_adjust_size(self):
        """Adjust width and height from Bitmap mapping data."""
        self.width, self.height = len(self.map[0]), len(self.map)

    def mirror_x(self):
        """Mirror image Horizontally."""
        self.map = [list(reversed(items)) for items in self.map]
        return self

    def mirror_y(self):
        """Mirror image Vertically."""
        self.map = list(reversed(self.map))
        return self

    def crop_x(self, x):
        """Crop image Horizontally,crops from right-bottom,only reduce size."""
        self.map = [lista[:x] for lista in self.map]
        self._auto_adjust_size()
        return self

    def crop_y(self, y):
        """Crop image Vertically,crops from right-bottom,only reduce size."""
        self.map = self.map[:y]
        self._auto_adjust_size()
        return self

    def crop(self, x, y):
        """Crop image,crops from right-bottom,only cuts to reduce size."""
        self.crop_x(x)
        self.crop_y(y)
        return self

    def crop_centered_x(self, x):
        """Centered Crop image Horizontally,crops from borders,reduce size."""
        self.map = [l[int(x / 2):len(l) - int(x / 2)] for l in self.map]
        self._auto_adjust_size()
        return self

    def crop_centered_y(self, y):
        """Centered Crop image Vertically,crops from borders,reduce size."""
        self.map = self.map[int(y / 2):len(self.map) - int(y / 2)]
        self._auto_adjust_size()
        return self

    def crop_centered(self, x, y):
        """Centered Crop image,crops from borders,only cuts to reduce size."""
        self.crop_centered_x(x)
        self.crop_centered_x(y)
        return self

    def expand_x(self, x):
        """Expand image Horizontally,grow from right-bottom,increments size."""
        self.map = [l + [self.bg] * (x - len(self.map[0])) for l in self.map]
        self._auto_adjust_size()
        return self

    def expand_y(self, y):
        """Expand image Vertically,grow from right-bottom,increments size."""
        _expanded = [[self.bg for i in range(len(self.map[0]))]
                     for a in range(y - len(self.map))]
        self.map = self.map + _expanded
        self._auto_adjust_size()
        return self

    def expand(self, x, y):
        """Expand image,grow from right-bottom,increments size."""
        self.expand_x(x)
        self.expand_y(y)
        return self

    def expand_centered_x(self, x):
        """Expand image centered Horizontally,grow from right-bottom."""
        _x = int(round(int(x + 1 if x % 2 else x) - len(self.map[0])) / 2)
        self.map = [[self.bg] * _x + l + [self.bg] * _x for l in self.map]
        self._auto_adjust_size()
        return self

    def expand_centered_y(self, y):
        """Expand image centered Vertically,grow from right-bottom."""
        _y = int(round(int(y + 1 if y % 2 else y) - len(self.map)) / 2)
        self.map = [
            [self.bg for i in range(len(self.map[0]))] for a in range(_y)
            ] + self.map + [[self.bg for i in range(len(self.map[0]))]
                            for a in range(_y)]
        self._auto_adjust_size()
        return self

    def expand_centered(self, x, y):
        """Expand image centered,grow from right-bottom."""
        self.expand_centered_x(x)
        self.expand_centered_y(y)
        return self

    def shrink_x(self, amount):
        """Shrink image horizontally."""
        _map = []
        for _list in self.map:
            new_list = []
            for index, item in enumerate(_list):
                new_item = None
                try:
                    next_item = _list[index + 1]
                except IndexError:
                    break
                if isinstance(item, int) and index % amount:
                    new_item = int(abs(round((item + next_item) / 2)))
                elif index % amount:
                    new_item = (int(abs(round((item[0] + next_item[0]) / 2))),
                                int(abs(round((item[1] + next_item[1]) / 2))),
                                int(abs(round((item[2] + next_item[2]) / 2))))
                if new_item:
                    new_list.append(new_item)
            if new_list:
                _map.append(new_list)
        self.map = _map
        self._auto_adjust_size()
        return self

    def shrink_y(self, amount):
        """Shrink image vertically."""
        _map = []
        for index, _list in enumerate(self.map):
            new_items = []
            try:
                next_list = self.map[index + 1]
            except IndexError:
                break
            if isinstance(_list[0], int) and index % amount:
                for pares in zip(_list, next_list):
                    _item = int(abs(round((pares[0] + pares[1]) / 2)))
                    new_items.append(_item)
            elif index % amount:
                for pares in zip(_list, next_list):
                    _item = (int(abs(round((pares[0][0] + pares[1][0]) / 2))),
                             int(abs(round((pares[0][1] + pares[1][1]) / 2))),
                             int(abs(round((pares[0][2] + pares[1][2]) / 2))))
                    new_items.append(_item)
            if new_items:
                _map.append(new_items)
        self.map = _map
        self._auto_adjust_size()
        return self

    def shrink(self, amount_x, amount_y):
        """Shrink image horizontally and vertically."""
        self.shrink_x(amount_x)
        self.shrink_y(amount_y)
        return self

    def lighten(self, amount):
        """Lighten the image according to amount argument. Do nothing on BW."""
        if self.header == "P2":
            self.map = [_ + amount if _ < 255 else _ for _ in self.map]
        elif self.header == "P3":
            self.map = [[(_[0] + amount if _[0] < 255 else _[0],
                          _[1] + amount if _[1] < 255 else _[1],
                          _[2] + amount if _[2] < 255 else _[2])
                        for _ in a] for a in self.map]
        return self.map

    def darken(self, amount):
        """Darken the image according to amount argument. Do nothing on BW."""
        if self.header == "P2":
            self.map = [_ - amount if _ > 0 else _ for _ in self.map]
        elif self.header == "P3":
            self.map = [[(_[0] - amount if _[0] > 0 else _[0],
                          _[1] - amount if _[1] > 0 else _[1],
                          _[2] - amount if _[2] > 0 else _[2])
                        for _ in a] for a in self.map]
        return self.map

    def fillrect(self, x, y, width, height, color=None):
        """Fill up a rectangle on the image with given color."""
        for h in range(height):
            for w in range(width):
                self.map[y + h][x + w] = color if color else self.bg
        return self

    def fillrect_stripe_x(self, x, y, width, height, color0, color1, stroke):
        """Fill up a rectangle on the image with striped colors."""
        for h in range(height):
            for w in range(width):
                self.set_pixel_stripe(x + w, y + h, False,
                                      color0, color1, stroke)
        return self

    def fillrect_stripe_y(self, x, y, width, height, color0, color1, stroke):
        """Fill up a rectangle on the image with striped colors."""
        for h in range(height):
            for w in range(width):
                self.set_pixel_stripe(x + w, y + h, True,
                                      color0, color1, stroke)
        return self

    def set_pixel(self, x, y, color=None):
        """Set a pixel to the image."""
        self.map[y][x] = color if color else self.bg
        return self

    def set_pixel_stripe(self, x, y, vertical, color0, color1, stroke=2):
        """Set a stripe pixel to the image,on X or Y."""
        self.map[y][x] = \
            color0 if int(y if vertical else x) % stroke else color1
        return self

    def fillrect_grid(self, x, y, width, height, color0, color1, stroke):
        """Fill up a rectangle on the image with grid-like colors."""
        for h in range(height):
            for w in range(width):
                self.set_pixel_grid(x + w, y + h, color0, color1, stroke)
        return self

    def set_pixel_grid(self, x, y, color0, color1, stroke=2):
        """Set a stripe pixel to the image,on X or Y."""
        self.map[y][x] = color0 if bool(y % stroke and x % stroke) else color1
        return self

    def fillrect_dotted(self, x, y, width, height, color0, color1, stroke):
        """Fill up a rectangle on the image with dotted colors."""
        for h in range(height):
            for w in range(width):
                self.set_pixel_dotted(x + w, y + h, color0, color1, stroke)
        return self

    def fillrect_random(self, x, y, width, height):
        """Fill up a rectangle on the image with random colors."""
        for h in range(height):
            for w in range(width):
                self.set_pixel_random(x + w, y + h)
        return self

    def set_pixel_random(self, x, y):
        """Set a random pixel to the image, on X or Y."""
        pass

    def set_pixel_dotted(self, x, y, color0, color1, stroke=2):
        """Set a dotted pixel to the image,on X or Y."""
        self.map[y][x] = color0 if bool(y % stroke or x % stroke) else color1
        return self

    def get_pixel(self, x, y):
        """Get a pixel from the image."""
        return self.map[y][x]

    def to_file(self, fyle):
        """Write the full image content to a local file path."""
        fyle = fyle if fyle.lower().endswith(self.ext) else fyle + self.ext
        with open(fyle, "w", encoding="utf-8") as img_file:
            img_file.write(self.__str__().strip())
        return fyle

    def to_png(self, fyle):
        """Write the full image content to a local *.PNG file path."""
        fyle = fyle if fyle.lower().endswith(".png") else fyle + ".png"
        if which("pnm2png"):
            pnm = self.to_file(NamedTemporaryFile().name)
            run((which("pnm2png"), pnm, fyle), timeout=99)
            return fyle

    def to_json(self, fyle=None):
        """Return full image content as JSON string or write to JSON file."""
        jotason = {"header": self.header, "comment": self.comment,
                   "width": self.width, "height": self.height,
                   "maxvalue": self.maxvalue, "bitmap": self.map}
        if fyle:  # if file then write to file
            fyle = fyle if fyle.lower().endswith(".json") else fyle + ".json"
            with open(fyle, "w", encoding="utf-8") as _file:
                _file.write(dumps(jotason, sort_keys=1, indent=4))
            return fyle
        else:  # if no file then return str
            return dumps(jotason, sort_keys=1, indent=4)

    def from_json(self, file_or_json):
        """Return all values from argument JSON string or JSON file path."""
        if os.path.isfile(file_or_json):  # is file
            with open(file_or_json, encoding="utf-8") as _file:
                json_data = loads(_file.read())
        else:  # is a string with json data
            json_data = loads(file_or_json)
        self.header, self.comment = json_data["header"], json_data["comment"]
        self.width, self.height = json_data["width"], json_data["height"]
        self.maxvalue, self.map = json_data["maxvalue"], json_data["bitmap"]
        return json_data


class ImgBW(__Bitmap):

    """PBM Raster Graphic Image,Black&White,using 0 or 1,a list of lists."""

    def init_bitmap(self):
        """Initialize a blank bitmap, set the file extension."""
        self.ext, self.header, self.maxvalue = ".pbm", "P1", None
        if not self.map:
            self.map = [[self.bg for w in range(self.width)]
                        for h in range(self.height)]
        return self

    def set_random_bitmap(self):
        """Set random bitmap data."""
        self.map = [[randint(0, 1) for w in range(self.width)]
                    for h in range(self.height)]
        return self

    def set_pixel_random(self, x, y):
        """Set a pixel to the image."""
        self.set_pixel(x, y, randint(0, 1))
        return self

    def invert_colors(self):
        """Reverse the Matrix, making the image to negative."""
        self.map = [[0 if _ else 1 for _ in items] for items in self.map]
        return self

    def __str__(self, mini=False):
        """The full standard PBM content as a string."""
        tmpl = "\n" if mini else "\n\n"
        mapstr = tmpl.join([" ".join([str(_) for _ in i]) for i in self.map])
        return _NETPBM.format(
            header=self.header, comment=self.comment, maxvalue="",
            width=self.width, height=self.height, data=mapstr)


class ImgGrayscale(__Bitmap):

    """PGM Raster Graphic Image,Grayscale,using 0 to 255,a list of lists."""

    def init_bitmap(self):
        """Initialize a blank bitmap, set the file extension."""
        self.ext, self.header, self.maxvalue, self.bg = ".pgm", "P2", 255, 255
        if not self.map:
            self.map = [[self.bg for w in range(self.width)]
                        for h in range(self.height)]
        return self

    def set_random_bitmap(self):
        """Set random bitmap data."""
        self.map = [[randint(0, 255) for w in range(self.width)]
                    for h in range(self.height)]
        return self

    def set_pixel_random(self, x, y):
        """Set a pixel to the image."""
        self.set_pixel(x, y, randint(0, 255))
        return self

    def invert_colors(self):
        """Reverse the Matrix, making the image to negative."""
        maxval = tuple(range(0, 256))
        self.map = [[maxval[~maxval.index(_)] for _ in i] for i in self.map]
        return self

    def __str__(self, mini=False):
        """The full standard PGM content as a string."""
        tmpl = "\n" if mini else "\n\n"
        mapstr = tmpl.join([" ".join([str(_) for _ in i]) for i in self.map])
        return _NETPBM.format(
            header=self.header, comment=self.comment, maxvalue=self.maxvalue,
            width=self.width, height=self.height, data=mapstr)


class ImgColor(__Bitmap):

    """PPM Raster Graphic Image,RGB Color,using 0 to 255,a list of tuples."""

    def init_bitmap(self):
        """Initialize a blank bitmap, set the file extension."""
        self.ext, self.bg = ".ppm", (255, 255, 255)
        self.header, self.maxvalue = "P3", 255
        if not self.map:
            self.map = [[(0, 0, 0) for w in range(self.width)]
                        for h in range(self.height)]
        return self

    def set_random_bitmap(self):
        """Set random bitmap data."""
        self.map = [[(randint(0, 255), randint(0, 255), randint(0, 255))
                     for w in range(self.width)] for h in range(self.height)]
        return self

    def set_pixel_random(self, x, y):
        """Set a pixel to the image."""
        self.set_pixel(x, y,
                       (randint(0, 255), randint(0, 255), randint(0, 255)))
        return self

    def invert_colors(self):
        """Reverse the Matrix, making the image to negative."""
        p = tuple(range(0, 256))
        self.map = [[[p[~p.index(a)] for a in _] for _ in i] for i in self.map]
        return self

    def __str__(self, mini=False):
        """The full standard PPM content as a string."""
        tmpl, tmpl2 = "\n" if mini else "\n\n", " " if mini else "    "
        map_str = tmpl.join([tmpl2.join([" ".join(
            [str(a).rjust(3) for a in _]) for _ in i]) for i in self.map])
        return _NETPBM.format(
            header=self.header, comment=self.comment, maxvalue=self.maxvalue,
            width=self.width, height=self.height, data=map_str)


if __name__ in "__main__":
    print(__doc__, __version__, __license__, __author__)
    # Simple examples.
    ImgColor(99, 99).set_random_bitmap().to_file("color")
    ImgGrayscale(99, 99).set_random_bitmap().to_file("gray")
    ImgBW(99, 99).set_random_bitmap().to_file("mono")
    # More elaborated example.
    image = ImgColor(300, 300)
    image.set_random_bitmap()
    image.fillrect(0, 0, 50, 50, [0, 255, 99])
    image.fillrect_stripe_y(50, 50, 50, 50, [0, 0, 0], [250, 250, 9], 6)
    image.fillrect_stripe_x(100, 100, 50, 50, [0, 9, 9], [9, 255, 250], 8)
    image.fillrect_grid(150, 150, 50, 50, [9, 9, 99], [9, 255, 9], 8)
    image.fillrect_dotted(200, 200, 50, 50, [0, 99, 0], [0, 0, 255], 8)
    image.fillrect_random(250, 250, 50, 50)
    image.mirror_x()
    image.mirror_y()
    image.expand_centered(350, 350)
    image.invert_colors()
    image.expand(400, 400)
    image.shrink(8, 8)
    image.set_datetime_as_comment()
    image.darken(2)
    image.lighten(2)
    image.to_file("example")
    image.from_file("example.ppm")
    image.to_file("example2")
    image.to_json("example")
    image.from_json("example.json")
    image.to_png("example")
    image.show()
    # Context manager simple example.
    with ImgColor(4, 4) as with_context_manager_example:
        with_context_manager_example.set_random_bitmap()
        with_context_manager_example.pprint()
        with_context_manager_example.write("example3")
