dofile("unknowsegment.lua")

Grid = {
	Width = 9,
	Height = 6,
	MaxCountBlock = 11
}
 
function Grid.new()
	local o = {}

	o.p_Grid = {}

	for x = 1, Grid.Width do
		o.p_Grid[x] = {}

		for y = 1, Grid.Height do
			o.p_Grid[x][y] = UnknowSegment.new(x, y)
		end
	end

	setmetatable(o, {__index = Grid})
    return o
end

function Grid:get(position)
	if type(position) == "table" and #position == 2 then
		return self.p_Grid[position[0]][position[1]]
	end
end

function Grid:set(position, segment)
	print(segment)
	print(segment.new(1,2))
end