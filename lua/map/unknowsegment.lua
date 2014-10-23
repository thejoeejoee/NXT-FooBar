dofile("segment.lua")

UnknowSegment = {}

function UnknowSegment.new(x, y)
	local o = Segment.new(x, y)

	setmetatable(o, {__index = UnknowSegment})
	return o
end