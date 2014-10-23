Grid = {
	Width = 9
	Height = 6
	MaxCountBlocks = 11
}

function Grid.new()
	local o = {}

	o.p_Grid = {}

	for y = 1, Grid.Height do
		o.p_Grid[y] = {}

		for x = 1, Grid.Width do
			o.p_Grid
	end

	setmetatable(o, {__index = Grid})
    return o
end