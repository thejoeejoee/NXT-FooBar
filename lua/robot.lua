dofile("directions.lua")
dofile("grid.lua")

Robot = {

}
 
function Robot.new(grid, robotHardware, position)
	local o = {}

	o.__grid = grid
    o.__hardware = robotHardware
    if type(position) == "table" and #position == 2 then
        o.__x = position[0]
        o.__y = position[1]
    end

	setmetatable(o, {__index = Robot})
    return o
end

function Robot:solveClosedWay(source_position, source_side)
    self.testedPostitions = {}
    self:isClosedWay(source_position, source_side)
end

function Robot:isClosedWay(source_side, source_position, length)
    local source_position = source_position or self.__position
    local length = length or 1
    if length > Grid.MaxGridRecursiveDepth then
       return false
    end
    local target_position = Grid.getNextPosition(source_side, source_position)
    if not Grid.Positionexists(target_position) then
       return true
    end

    if self.__grid:get(target_position)('block') then
       return True
    end
    local sides = {}
    for k, v in pairs(Directions) do
        if not Grid.opositeSide(source_side) == source_side then
           table.insert(sides, v)
        end
    end
    local free_sides = {}
    for _, side in pairs(free_sides) do
        local position = grid.getNewPosition(side, target_position)
        if not grid.Positionexists(position) then
            continue
        end
        -- zde to sony musi udelat -> viz. python
       local segment = self.__grid:get(position)
       if segment({"point", "unknownsegment"}) then
           table.insert(free_sides, side)
       end
    end
    if #free_sides == 0 then
        return true
    end
    local blocked = {}
    for _, side in pairs(free_side) do
        table.insert(blocked, self:isClosedWay(side, target_position, length+1))
    end
    local all = true
    for _, bool in pairs(blocked) do
        if bool == false then
            all = true
        end
    end
    return all


end
















