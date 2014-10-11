nxt.dofile("sensor")

TouchSensor = {}

function TouchSensor.new(port)
	local o = Sensor.new(port)

	setmetatable(o, {__index = TouchSensor})
    return o
end

function TouchSensor:status()
	nxt.InputSetType(self.p_Port,1,0x20)
	_, _, _, result = nxt.InputGetStatus(self.p_Port)
	return result
end