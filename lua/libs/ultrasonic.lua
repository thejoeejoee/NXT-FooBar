nxt.dofile("sensor")

UltraSonic = {}
 
nxt.I2Cversion    = string.char(0x02, 0x00)
nxt.I2Cproduct    = string.char(0x02, 0x08)
nxt.I2Ctype       = string.char(0x02, 0x10)
nxt.I2Ccontinuous = string.char(0x02, 0x41, 0x02)
nxt.I2Cdata       = string.char(0x02, 0x42)

function UltraSonic.new(port)
        local o = Sensor.new(port)
 
        --init I2C
        nxt.I2CInitPins(port)
        nxt.InputSetType(port, 2)
        nxt.InputSetDir(port, 1, 1)
        nxt.InputSetState(port, 1, 1)
        nxt.I2CSendData(3, nxt.I2Cproduct, 8)
 
        setmetatable(o, {__index = UltraSonic})
        return o
end
 
function UltraSonic:scan()
	nxt.I2CSendData(self.p_Port, nxt.I2Cdata, 8)
	
	while( 0 ~= nxt.I2CGetStatus( self.p_Port ) ) do
  	end

    local s = nxt.I2CRecvData(self.p_Port, 8)
    result = string.byte(s,1,8)

    return result
end

sen = UltraSonic.new(Sensor.Port1)
mot = Motor.new(Motor.PortA)
mot:setSpeed(100, Motor.Forward)
angle = mot:status()
res = Motor.Forward
scans = 0

repeat	
	stat = mot:status()
	if(stat>=angle-3 and stat<=angle+3) then
		print(sen:scan())
		if res == Motor.Forward then
			angle = (angle + 90)%360
		else
			angle = (angle - 90)%360
		end
		scans = scans + 1
		mot:limitedRotate(90)
	end
	if scans==4 then
		res = (res == Motor.Backward) and Motor.Forward or Motor.Backward
		mot:setSpeed(100,res)
		scans = 0
	end


until(nxt.ButtonRead() == 8)
