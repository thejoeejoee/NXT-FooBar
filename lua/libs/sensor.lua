Sensor = {
	Port1 = 1,
	Port2 = 2,
	Port3 = 3,
	Port4 = 4
}
 
function Sensor.new(port)
        local o = {}
 
        o.__port = port or 1
 
        setmetatable(o, {__index = Sensor})
        return o
end