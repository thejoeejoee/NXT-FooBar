--nxt.dofile("directions")

RobotHardware = {}

function RobotHardware.new(starDirection, mainMotor_Port, directionMotor_Port, sensorMotor_Port, ultrasonic_Port)
	local o = {}

	o.__direction = starDirection or Directions.Vertical
	o.__sensorSide = Sides.Bottom
	
	o.__mainMotor = Motor.new(mainMotor_Port)
	o.__directionMotor = Motor.new(directionMotor_Port)
	o.__sensorMotor = Motor.new(sensorMotor_Port)
	o.__ultrasonic = UltraSonic.new(ultrasonic_Port)

	setmetatable(o, {__index = RobotHardware})
	return o
end

function RobotHardware:changeDirection(direction)
	if direction == self.__direction then
		return
	end

	self.__delay = true

	if direction == Directions.Horizontal then
		self.__directionMotor:setSpeed(100, Motor.Backward)
		self.__direction = Directions.Horizontal

	else
		self.__directionMotor:setSpeed(100, Motor.Forward)
		self.__direction = Directions.Vertical
	end

	self.__directionMotor:limitedRotate(6*360)

	repeat
		try(
			function()
				self.__directionMotor:controlRotation()
			end
		)

		catch("RotationFinished_"..tostring(self.__directionMotor.__port),
			function()
				self.__delay = false
			end
		)
	until(not self.__delay)
end

function RobotHardware:rotateSensor(side)
	local angle_90 = 210

	if side == self.__sensorSide then
		return
	end

	if side < self.__sensorSide then
		self.__sensorMotor:setSpeed(100, Motor.Forward)

	else
		self.__sensorMotor:setSpeed(100, Motor.Backward)
	end

	self.__sensorMotor:limitedRotate(angle_90 * math.floor(math.abs(side - self.__sensorSide)))
	self.__sensorSide = side
end

function RobotHardware:move(side)
	local verticalRotation = 3*360-37
	local horizontalRotation = 672
	
	self:rotateSensor(side)

	if (side == Sides.Right or side == Sides.Left) and self.__direction == Directions.Vertical then
		self:changeDirection(Directions.Horizontal)

	elseif (side == Sides.Top or side == Sides.Bottom) and self.__direction == Directions.Horizontal then
		self:changeDirection(Directions.Vertical)
	end

	if side == Sides.Right or side == Sides.Top then
		self.__mainMotor:setSpeed(100, Motor.Backward)
	else
		self.__mainMotor:setSpeed(100, Motor.Forward)
	end

	if self.__direction == Directions.Vertical then
		self.__mainMotor:limitedRotate(verticalRotation)
	else
		self.__mainMotor:limitedRotate(horizontalRotation)
	end

	self.__delay_1 = true

	repeat
		try(
			function()
				self.__mainMotor:controlRotation()
				print(self.__mainMotor.__port)
			end
		)

		catch("RotationFinished_"..tostring(self.__mainMotor.__port),
			function()
				print(3)
				self.__delay_1 = false
			end
		)
	until(not self.__delay_1)
end












