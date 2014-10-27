dofile("segment.lua")
dofile("point.lua")

UnknownSegment = {}

function UnknownSegment.new(x, y)
	local o = Segment.new(x, y)
	local meta = getmetatable(o)

	o.__type = "unknownsegment"
	meta.__index = UnknownSegment

	setmetatable(o, meta)
	return o
end

t = UnknownSegment.new(1,2)
print(t("point","unknownsegment"))