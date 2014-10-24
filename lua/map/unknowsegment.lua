dofile("segment.lua")

UnknowSegment = {}

function UnknowSegment.new(x, y)
	local o = Segment.new(x, y)

	o.__type = "point"

	setmetatable(o, getmetatable(o))
	return o
end