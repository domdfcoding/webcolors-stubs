# Stubs for webcolors
# https://github.com/ubernostrum/webcolors

# Copyright (c) 2020, Dominic Davis-Foster
# Copyright (c) 2008-2020, James Bennett
# BSD Licensed

# this package
from ._conversion import hex_to_name as hex_to_name
from ._conversion import hex_to_rgb as hex_to_rgb
from ._conversion import hex_to_rgb_percent as hex_to_rgb_percent
from ._conversion import name_to_hex as name_to_hex
from ._conversion import name_to_rgb as name_to_rgb
from ._conversion import name_to_rgb_percent as name_to_rgb_percent
from ._conversion import rgb_percent_to_hex as rgb_percent_to_hex
from ._conversion import rgb_percent_to_name as rgb_percent_to_name
from ._conversion import rgb_percent_to_rgb as rgb_percent_to_rgb
from ._conversion import rgb_to_hex as rgb_to_hex
from ._conversion import rgb_to_name as rgb_to_name
from ._conversion import rgb_to_rgb_percent as rgb_to_rgb_percent
from ._definitions import CSS2 as CSS2
from ._definitions import CSS3 as CSS3
from ._definitions import CSS21 as CSS21
from ._definitions import HTML4 as HTML4
from ._definitions import names as names
from ._html5 import html5_parse_legacy_color as html5_parse_legacy_color
from ._html5 import html5_parse_simple_color as html5_parse_simple_color
from ._html5 import html5_serialize_simple_color as html5_serialize_simple_color
from ._normalization import normalize_hex as normalize_hex
from ._normalization import normalize_integer_triplet as normalize_integer_triplet
from ._normalization import normalize_percent_triplet as normalize_percent_triplet
from ._types import HTML5SimpleColor as HTML5SimpleColor
from ._types import IntegerRGB as IntegerRGB
from ._types import IntTuple as IntTuple
from ._types import PercentRGB as PercentRGB
from ._types import PercentTuple as PercentTuple

__all__ = [
		"HTML4",
		"CSS2",
		"CSS21",
		"CSS3",
		"name_to_hex",
		"name_to_rgb",
		"name_to_rgb_percent",
		"hex_to_name",
		"hex_to_rgb",
		"hex_to_rgb_percent",
		"names",
		"rgb_to_hex",
		"rgb_to_name",
		"rgb_to_rgb_percent",
		"rgb_percent_to_hex",
		"rgb_percent_to_name",
		"rgb_percent_to_rgb",
		"html5_parse_simple_color",
		"html5_parse_legacy_color",
		"html5_serialize_simple_color",
		"normalize_hex",
		"normalize_integer_triplet",
		"normalize_percent_triplet",
		"IntegerRGB",
		"PercentRGB",
		"HTML5SimpleColor",
		"IntTuple",
		"PercentTuple"
		]
