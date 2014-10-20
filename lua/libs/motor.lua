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

	o.p_Port = port or 1
	o.p_Speed = 0
	o.p_Brake = false
	o.p_Direction = Motor.Forward
	o.p_RotationType = 0
	o.p_Control = false

	setmetatable(o, {__index = Motor})
	return o
end

function Motor:setSpeed(value, direction)
	if(value > 100 or value < -100) then
		error("exSetSpeedOutOfRange")
	end

	self.p_Direction = direction or Motor.Forward
	self.p_Speed = (self.p_Direction == Motor.Forward) and value or (-value)
end

function Motor:status()
	_, tacho = nxt.OutputGetStatus(self.p_Port)
	return tacho%360
end

function Motor:continuouslyRotate()
	self.p_RotationType = Motor.Continuously
	nxt.OutputSetSpeed(self.p_Port, 32, self.p_Speed)
end

function Motor:limitedRotate(angle)
	angle = angle or 0
	self.p_RotationType = Motor.Limited
	self.p_Control = true

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

function Motor:direction()
	return self.p_Direction
end

function Motor:raw_status()
	_, tacho = nxt.OutputGetStatus(self.p_Port)
	return tacho
end

function Motor:controlRotation()
	if self.p_RotationType == Motor.Continuously then
		error("exBadRotationType")
	end
		

	_, _, _, _, _, _, remaining = nxt.OutputGetStatus(self.p_Port)
	if remaining <= 1 and self.p_Control then
		self.p_Control = false
		error("RotationFinished")
	end
end	

function Motor:invertDirection()
	self.p_Direction = (self.p_Direction == Motor.Forward) and Motor.Backward or Motor.Forward
	self.p_Speed = -self.p_Speed
end