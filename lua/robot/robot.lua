nxt.dofile("directions")

Robot = {
	Waiting = 0,
	InClosedWay = 1
}
 
function Robot.new(grid, robotHardware, position)
	local o = {}

	--o.__mode = Robot.Waiting

	o.__grid = grid
	o.__hardware = robotHardware

	o.__lastDirection = nil
	o.__sidesHistory = {}
	o.__x = position[1]
	o.__y = position[2]
	o.__position = position
	o.__positionHistory = {}
	table.insert(o.__positionHistory, position)

	setmetatable(o, {__index = Robot})
	return o
end

function Robot:checkSides()
	local scan_line 
	local next_position
	local next_segment

	for _, side in pairs(Sides) do
		scan_line = false	
		next_position = Grid:nextPosition(side, self.__position)

		if Grid:positionExists(next_position) then
			while Grid:positionExists(next_position) do
				next_segment = self.__grid:get(next_position)

				if next_segment == Grid.Block then
					break
				end

				if next_segment == Grid.UnknownSegment then
					scan_line = true
				end

				next_position = Grid:next_position(side, next_position)
			end
		end

		if scan_line then
			self:scan_line(side)
		end
	end
end

--[[function Robot:solveClosedWay(source_side, source_position)
	self.testedPositions = {}
	return self:isClosedWay(source_side, source_position)
end

function __valueInTable(value, tab)
	for _, v in pairs(tab) do
		if v[1] == value[1] and v[2] == value[2] then
			return true
		end
	end

	return false
end

function Robot:isClosedWay(source_side, source_position, length)
	local source_position = source_position or self.__position
	local length = length or 1
	local all = true
	local sides = {}
	local free_sides = {}
	local blocked = {}

	if length > Grid.MaxGridRecursiveDepth then
		return false
	end

	local target_position = Grid:nextPosition(source_side, source_position)

	if not Grid:positionExists(target_position) then
		return true
	end

	if self.__grid:checkSegment(target_position, {Grid.Block}) then
		return true
	end

	for k, v in pairs(Sides) do
		if not(Grid:oppositeSide(source_side) == source_side) then
		   table.insert(sides, v)
		end
	end

	for _, side in pairs(sides) do
		local position = Grid:nextPosition(side, target_position)

		if not Grid:positionExists(position) then
			goto continueIsClosedWay
		end
		-- zde to sony musi udelat -> viz. python
		if __valueInTable(position, self.testedPositions) then
			goto continue
		else
			table.insert(self.testedPositions, position)
		end

		local segment = self.__grid:get(position)
		if self.__grid:checkSegment(position, {Grid.Point, Grid.UnknownSegment, Grid.CollectedPoint}) then
			table.insert(free_sides, side)
		end
		::continueIsClosedWay::
	end

	if #free_sides == 0 then
		return true
	end
	
	for _, side in pairs(free_sides) do
		table.insert(blocked, self:isClosedWay(side, target_position, length+1))
	end

	for _, bool in pairs(blocked) do
		if bool == false then
			all = false
		end
	end

	return all
end

function Robot:checkSides()
	for key, side in pairs(Sides) do
		local scan_line = false
		local next_position = Grid:nextPosition(side, self.__position)
		if not Grid:positionExists(next_position) then
			goto continueCheckSides
		end
		while Grid:positionExists(next_position) do
			local next_segment = Grid:get(next_position)
			if next_segment == Grid.Block then
				break
			elseif next_segment == Grid.UnknownSegment then
				scan_line = true
			end
			next_position = Grid:next_position(side, next_position)
		end
		if scan_line then
			self:scanLine(side)
		end
		::continueCheckSides::IsClosedWay
	end
end

function Robot:scanLine(side) 
	local blocks = self.__hardware:getCountOfEmptyBlocks(side)
	local position = self.__position
	for _=1, blocks do
		position = Grid:nextPosition(side, position)
		if not self:setKnownSegment(position, Grid.Point) then
			break
		end

	end
	local end_position = Grid.nextPosition(side, position)
	self:setKnownSegment(end_position, Grid.Block)
end

function Robot:setKnownSegment(position, segment)
	if Grid:positionExists(position) then
		if self.__grid:get(position) == Grid.UnknownSegment then
			self.__grid:set(position, segmet)
		end
		print('fuck!')
		return true
	else
		return false
	end
end]]