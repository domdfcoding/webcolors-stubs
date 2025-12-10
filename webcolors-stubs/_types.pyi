# stdlib
import typing

class IntegerRGB(typing.NamedTuple):
	red: int
	green: int
	blue: int

class PercentRGB(typing.NamedTuple):
	red: str
	green: str
	blue: str

class HTML5SimpleColor(typing.NamedTuple):
	red: int
	green: int
	blue: int

IntTuple = IntegerRGB | HTML5SimpleColor | tuple[int, int, int]
PercentTuple = PercentRGB | tuple[str, str, str]
