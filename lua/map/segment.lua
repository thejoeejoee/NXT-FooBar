Segment = {}

Segment_Meta = {
	__index = Segment,

	__call = function(self, ...)
		if self.__type == nil then
			error("exTypeNotDefined")
		end

		if type(arg) == "table" then
			for k, v in pairs(arg) do
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

	o.p_X = x or error("exBadArgument")
	o.p_Y = y or error("exBadArgument")
	o.p_Position = {x, y}
	o.__type = nil

	setmetatable(o, Segment_Meta)
	return o
end