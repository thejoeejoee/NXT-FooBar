Motor = {
	PortA = 1,
	PortB = 2,
	PortC = 3,

	Forward = 4,
	Backward = 5
}

function Motor.new(port)
	local o = {}

	o.p_Port = port or 1
	o.p_Speed = 0
	o.p_Brake = false

	setmetatable(o, {__index = Motor})
	return o
end

function Motor:setSpeed(value, direction)
	if(value > 100 or value < -100) then
		error("exSetSpeedOutOfRange")
	end

	direction = direction or Motor.Forward
	self.p_Speed = (direction == Motor.Forward) and value or -value
end

function Motor:status()
	_, tacho = nxt.OutputGetStatus(self.p_Port)
	return tacho%360
end

function Motor:continuouslyRotate()
	nxt.OutputSetSpeed(self.p_Port, 32, self.p_Speed)
end

function Motor:limitedRotate(angle)
	angle = angle or 0

	nxt.OutputSetRegulation(self.p_Port,1,1)
	nxt.OutputSetSpeed(self.p_Port, 0x20, self.p_Speed, angle)
end

function Motor:setBrake(value)
	if value then
		nxt.OutputSetRegulation(self.p_Port, 1, 1)
	else
		nxt.OutputSetRegulation(self.p_Port, 0, 0)
	end
end

function Motor:stop(brake)
	brake = brake or false

	nxt.OutputSetRegulation(self.p_Port, 1, tonumber(brake))

	if brake then
		nxt.OutputSetSpeed(self.p_Port, 0x20, 0)
	else
		nxt.OutputSetSpeed(self.p_Port, 0, 0)
	end
end

--[[
Motor = {
	PortA = 1,
	PortB = 2,
	PortC = 3,

	Forward = 4,
	Backward = 5
}

Motor.new( port )
Motor:setSpeed(value, direction)
Motor:status()
Motor:continuouslyRotate()
Motor:limitedRotate(angle)
Motor:setBrake(value)
Motor:stop(brake)
]]

--[[Example
print(Motor.PortB)
mot = Motor.new(Motor.PortA)
mot:setSpeed(100)
mot:continuouslyRotate()
mot2 = Motor.new(Motor.PortB)
mot2:setSpeed(100)
mot2:continuouslyRotate()
]]