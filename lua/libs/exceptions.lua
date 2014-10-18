exceptions = {
	["exIndexingNil"] = "exIndexingNil", 
	["exCallingNil"] = "exCallingNil",
	["exIndexingWithNil"] = "exIndexingWithNil"
}

function try(testedFunc)
	status, exception = pcall(testedFunc)

	--překopání názvů exceptionů na lepší názvy
	if(status) then
		return

	elseif(string.find(exception, "attempt to index")) then
		exception = exceptions.exIndexingNil

	elseif(string.find(exception, "attempt to call")) then
		exception = exceptions.exCallingNil

	elseif(string.find(exception, "table index is nil")) then
		exception = exceptions.exIndexingWithNil
	end

	passed = false
end

function catch(err, doFunc)
	--if it is not wanted exception
	if(status or passed) then return end 	--žádnej exception

	if(not string.find(exception, err)) then
		return

	--but if it is
	elseif(string.find(exception, err)) then
		passed = true
		doFunc()
	end
end