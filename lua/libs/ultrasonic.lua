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