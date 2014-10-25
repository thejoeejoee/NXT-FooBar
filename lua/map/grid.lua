dofile("unknowsegment.lua")
dofile("directions.lua")

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

function Grid:position_exits(position)
	if position[0] < 0 or position[1] < 0 then
		return false
	elseif position[0] > Grid.Width - 1 or position[1] > Grid.Height - 1 then
		return false
	end

	return true 
end

function Grid:getNextPosition(side, position)
	if side == Directions.Top then
		return {position[0], position[1] - 1}
	elseif side == Directions.Right then
		return {position[0] + 1, position[1]}
	elseif side == Directions.Bottom then
		return {position[0], position[1] + 1}
	elseif side == Directions.Left then
		return {position[0] - 1, position[1]}
	else
		error("exBadIndex")
	end
end

function Grid:oppositeSide(side)
	if side == Directions.Top or side == Directions.Right then
		return side + 2
	elseif side == Directions.Bottom or side == Directions.Left then
		return side - 2
	end
end










