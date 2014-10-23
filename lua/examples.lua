sen = UltraSonic.new(Sensor.Port1)
mot = Motor.new(Motor.PortA)
mot:setSpeed(100, Motor.Forward)
angle = mot:status()
res = Motor.Forward
scans = 0

repeat	
	stat = mot:status()
	--print(angle.."/"..stat)
	step = 168
	if(stat>=angle-3 and stat<=angle+3) then
		print(sen:scan())
		if res == Motor.Forward then
			angle = (angle + step)%360
		else
			angle = (angle - step)%360
		end
		scans = scans + 1
		mot:limitedRotate(step)
	end
	if scans==4 then
		res = (res == Motor.Backward) and Motor.Forward or Motor.Backward
		mot:setSpeed(100,res)
		scans = 0
	end


until(nxt.ButtonRead() == 8)

nxt.dofile("motor")
m = Motor.new(Motor.PortA)
m:setSpeed(100, Motor.Backward)

while true do
	m:limitedRotate(6*360)
	m:invertDirection()
end

m = Motor.new(Motor.PortA)
m:setSpeed(100)
m:continuouslyRotate()

ms = Motor.new(Motor.PortB)
ms:setSpeed(100)

s = UltraSonic.new(Sensor.Port1)

foo = 0
scanning = true

repeat
	try(
		function()
			if scanning then
				s:controlDistance(15)
			else
				ms:controlRotation()
			end
		end
	)

	catch("RotationFinished",
		function()
			scanning = true
		end
	)

	catch("DistanceReached",
		function()
			scanning = false
			ms:limitedRotate(2*378)
			ms:invertDirection()

			--foo = 1
			--m:stop(true)
			m:invertDirection()
			m:continuouslyRotate()
		end
	)
until(nxt.ButtonRead == 8)

mot = Motor.new(Motor.PortB)
mot:setSpeed(100)
--ultrasonic = UltraSonic.new(Sensor.Port1)
scans = 0
first = true
repeat
	try(
		function()
			if first then
				first = false
				error("RotationFinished")
			end

			mot:controlRotation()
		end
	)

	catch("RotationFinished",
		function()
			if scans == 1 then
				scans = 0
				mot:invertDirection()
			end

			--print(ultrasonic:scan())
			scans = scans + 1

			mot:limitedRotate(6*360)
		end
	)
	--print(mot:status())
until(nxt.ButtonRead() == 8)

repeat 
	print(s:scan())
until(nxt.ButtonRead() == 8)
