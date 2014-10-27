nxt.dofile("unknown")
nxt.dofile("directions")

Grid = {
	Width = 9,
	Height = 6,
	MaxCountBlock = 11,
    MaxGridRecursiveDepth = 10
}
 
function Grid.new()
	local o = {}

	o.__grid = {}

	for y = 0, Grid.Height - 1 do
		o.__grid[y] = {}

		for x = 0, Grid.Width - 1 do
			o.__grid[y][x] = UnknownSegment.new(x, y)
		end
	end

	setmetatable(o, {__index = Grid})
    return o
end

function Grid:get(position)
	if type(position) == "table" and #position == 2 then
		return self.__grid[position[2]][position[1]]
	end
end

function Grid:set(position, segment)
	if type(position) == "table" and #position == 2 then
		self.__grid[position[2]][position[1]] = segment.new(position[1], position[2])
	end
end

function Grid:positionExists(position)
	if position[1] < 0 or position[2] < 0 then
		return false
	elseif position[1] > Grid.Width - 1 or position[2] > Grid.Height - 1 then
		return false
	end

	return true 
end

function Grid:nextPosition(side, position)
	if side == Directions.Top then
		return {position[1], position[2] - 1}
	elseif side == Directions.Right then
		return {position[1] + 1, position[2]}
	elseif side == Directions.Bottom then
		return {position[1], position[2] + 1}
	elseif side == Directions.Left then
		return {position[1] - 1, position[2]}
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
