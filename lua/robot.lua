nxt.dofile("directions")

Robot = {}
 
function Robot.new(grid, robotHardware, position)
	local o = {}

	o.__grid = grid
    o.__hardware = robotHardware

    if type(position) == "table" and #position == 2 then
        o.__x = position[1]
        o.__y = position[2]
        o.__position = position
    end

	setmetatable(o, {__index = Robot})
    return o
end

function Robot:solveClosedWay(source_side, source_position)
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

    for k, v in pairs(Directions) do
        if not(Grid:oppositeSide(source_side) == source_side) then
           table.insert(sides, v)
        end
    end

    for _, side in pairs(sides) do
        local position = Grid:nextPosition(side, target_position)

        if not Grid:positionExists(position) then
            goto continue
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
        ::continue::
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