Segment = {}

Segment_Meta = {
	__index = Segment,

	__call = function(self, list)
		if self.__type == nil then
			error("exTypeNotDefined")
		end

		if type(list) == "table" then
			for k, v in pairs(list) do
				if v == self.__type then
					return true
				end
			end
		end

		return false
	end
}

function Segment.new(x, y)
	local o = {} 

	o.__x = x or 0
	o.__y = y or 0
	o.__position = {x, y}
	o.__type = nil

	setmetatable(o, Segment_Meta)
	return o
end