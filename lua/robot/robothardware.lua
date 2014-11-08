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

function RobotHardware:changeDirection()
	if self.__direction == Directions.Vertical then
		self.__directionMotor:setSpeed(100, Motor.Backward)
		self.__direction = Directions.Horizontal

	else
		self.__directionMotor:setSpeed(100, Motor.Forward)
		self.__direction = Directions.Vertical
	end

	self.__directionMotor:limitedRotate(8*360)
end

function RobotHardware:rotateSensor()
	
end