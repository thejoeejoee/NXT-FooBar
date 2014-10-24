Motor = {
	PortA = 1,
	PortB = 2,
	PortC = 3,

	Forward = 1,
	Backward = 2,

	Continuously = 1,
	Limited = 2
}

function Motor.new(port)
	local o = {}

	o.__port = port or 1
	o.__speed = 0
	o.__brake = false
	o.__direction = Motor.Forward
	o.__rotationType = 0
	o.__control = false

	setmetatable(o, {__index = Motor})
	return o
end

function Motor:setSpeed(value, direction)
	if(value > 100 or value < -100) then
		error("exSetSpeedOutOfRange")
	end

	self.__direction = direction or Motor.Forward
	self.__speed = (self.__direction == Motor.Forward) and value or (-value)
end

function Motor:status()
	_, tacho = nxt.OutputGetStatus(self.__port)
	return tacho%360
end

function Motor:continuouslyRotate()
	self.__rotationType = Motor.Continuously
	nxt.OutputSetSpeed(self.__port, 32, self.__speed)
end

function Motor:limitedRotate(angle)
	local angle = angle or 0
	self.__rotationType = Motor.Limited
	self.__control = true

	nxt.OutputSetRegulation(self.__port,1,1)
	nxt.OutputSetSpeed(self.__port, 0x20, self.__speed, angle)
end

function Motor:setBrake(value)
	if value then
		nxt.OutputSetRegulation(self.__port, 1, 1)
	else
		nxt.OutputSetRegulation(self.__port, 0, 0)
	end
end

function Motor:stop(brake)
	local brake = brake or false

	nxt.OutputSetRegulation(self.__port, 1, tonumber(brake))

	if brake then
		nxt.OutputSetSpeed(self.__port, 0x20, 0)
	else
		nxt.OutputSetSpeed(self.__port, 0, 0)
	end
end

function Motor:direction()
	return self.__direction
end

function Motor:raw_status()
	local _, tacho = nxt.OutputGetStatus(self.__port)
	return tacho
end

function Motor:controlRotation()
	if self.__rotationType == Motor.Continuously then
		error("exBadRotationType")
	end
		

	local _, _, _, _, _, _, remaining = nxt.OutputGetStatus(self.__port)
	if remaining <= 1 and self.__control then
		self.__control = false
		error("RotationFinished")
	end
end	

function Motor:invertDirection()
	self.__direction = (self.__direction == Motor.Forward) and Motor.Backward or Motor.Forward
	self.__speed = -self.__speed
end