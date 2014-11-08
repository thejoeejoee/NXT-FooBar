--nxt.dofile("directions")

RobotHardware = {}

function RobotHardware.new(starDirection, mainMotor_Port, directionMotor_Port, sensorMotor_Port, ultrasonic_Port)
	local o = {}

	o.__direction = starDirection or Directions.Vertical
	o.__sensorSide = Sides.Bottom
	
	o.__mainMotor = Motor.new(mainMotor_Port)
	o.__directionMotor = Motor.new(directionMotor_Port)
	o.__sensorMotor = Motor.new(sensorMotor_Port)
	o.__ultrasonic = Ultrasonic.new(ultrasonic_Port)

	setmetatable(o, {__index = RobotHardware})
	return o
end

function RobotHardware:changeDirection(direction)
	if direction == self.__direction then
		return
	end

	local done = false

	if self.__direction == Directions.Vertical then
		self.__directionMotor:setSpeed(100, Motor.Backward)
		self.__direction = Directions.Horizontal

	else
		self.__directionMotor:setSpeed(100, Motor.Forward)
		self.__direction = Directions.Vertical
	end

	self.__directionMotor:limitedRotate(8*360)

	repeat
		try(
			function()
				self.__directionMotor:controlRotation()
			end
		)

		catch("RotationFinished"..tostring(self.__directionMotor.__port),
			function()
				done = true
			end
		)
	until(done)
end

function RobotHardware:rotateSensor(side)
	local angle_90 = 210

	if side == self.__sensorSide then
		return
	end

	if side < self.__sensorSide then
		self.__sensorMotor:setSpeed(100, Motor.Backward)

	else
		self.__sensorMotor:setSpeed(100, Motor.Forward)
	end

	self.__sensorMotor:limitedRotate(angle_90 * math.floor(math.abs(side - self.__sensorSide)))
end	