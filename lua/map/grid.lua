dofile("unknowsegment.lua")

Grid = {
	Width = 9,
	Height = 6,
	MaxCountBlock = 11
}
 
function Grid.new()
	local o = {}

	o.__grid = {}

	for y = 1, Grid.Height do
		o.__grid[y] = {}

		for y = 1, Grid.Width do
			o.__grid[y][x] = UnknowSegment.new(x, y)
		end
	end

	setmetatable(o, {__index = Grid})
    return o
end

function Grid:get(position)
	if type(position) == "table" and #position == 2 then
		return self.__grid[position[0]][position[1]]
	end
end

function Grid:set(position, segment)
	if type(position) == "table" and #position == 2 then
		self.__grid[position[0]][position[1]] = segment.new(position[0], position[1])
	end
end

