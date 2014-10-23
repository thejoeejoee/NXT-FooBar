Segment = {}

function Segment.new(x, y)
	local o = {} 

	o.p_X = x or error("exBadArgument")
	o.p_Y = y or error("exBadArgument")

	setmetatable(o, {__index = Segment})
	return o
end