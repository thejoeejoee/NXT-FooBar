dofile("segment.lua")

Point = {}

function Point.new(x, y)
	local o = Segment.new(x, y)
	local meta = getmetatable(o)

	o.__type = "point"
	o.__collected = false
	meta.__index = Point

	setmetatable(o, meta)
	return o
end

function Point:collected()
	return self.__collected
end

function Point:collect()
	self.__collected = true
end