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


