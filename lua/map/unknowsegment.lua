dofile("segment.lua")

UnknowSegment = {}

function UnknowSegment.new(x, y)
	local o = Segment.new(x, y)
	local meta = getmetatable(o)

	o.__type = "unknowsegment"
	meta.__index = UnknowSegment

	setmetatable(o, meta)
	return o
end