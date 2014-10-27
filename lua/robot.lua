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
    self.testedPostitions = {}
    return self:isClosedWay(source_side, source_position)
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

    if self.__grid:get(target_position)('block') then
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
 
        local segment = self.__grid:get(position)
        print(segment.__type)
        if segment("point", "unknownsegment") then
            print("foobar")
            table.insert(free_sides, side)
        end
        ::continue::
    end

    if #free_sides == 0 then
        print("free sides")
        return true
    end
    
    for _, side in pairs(free_side) do
        table.insert(blocked, self:isClosedWay(side, target_position, length+1))
    end

    for _, bool in pairs(blocked) do
        if bool == false then
            all = true
        end
    end

    return all
end

nxt.dofile("block")
g = Grid:new()

g:set({1, 0}, Block)
--g:set({1, 1}, Block)
g:set({2, 1}, Block)
g:set({3, 2}, Block)
g:set({0, 3}, Block)
g:set({2, 3}, Block)

r = Robot.new(g, nil, {0, 0})
print(r:solveClosedWay(Directions.Bottom))












