nxt.dofile("segment")

Block = {}

function Block.new(x, y)
	local o = Segment.new(x, y)
	local meta = getmetatable(o)

	o.__type = "block"
	meta.__index = Block

	setmetatable(o, meta)
	return o
end