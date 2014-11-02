nxt.dofile("directions")

Grid = {
	Width = 4,
	Height = 4,
	MaxCountBlock = 11,
    MaxGridRecursiveDepth = 20,

    UnknownSegment = "u",
    Block = "b",
    Point = "p",
    CollectedPoint = "c"
}
 
function Grid.new()
	local o = {}

	o.__grid = {}

	for y = 0, Grid.Height - 1 do
		o.__grid[y] = {}

		for x = 0, Grid.Width - 1 do
			o.__grid[y][x] = "u"
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
		self.__grid[position[2]][position[1]] = segment
	end
end

function Grid:checkSegment(position, list)
	local segment = self:get(position)

	for k, v in pairs(list) do
		if v == segment then
			return true
		end
	end

	return false
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
	if side == Sides.Top then
		return {position[1], position[2] - 1}
	elseif side == Sides.Right then
		return {position[1] + 1, position[2]}
	elseif side == Sides.Bottom then
		return {position[1], position[2] + 1}
	elseif side == Sides.Left then
		return {position[1] - 1, position[2]}
	else
		error("exBadIndex")
	end
end

function Grid:oppositeSide(side)
	if side == Sides.Top or side == Sides.Right then
		return side + 2
	elseif side == Sides.Bottom or side == Sides.Left then
		return side - 2
	end
end
