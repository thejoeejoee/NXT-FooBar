exceptions = {
	["exIndexingNil"] = "exIndexingNil", 
	["exCallingNil"] = "exCallingNil",
	["exIndexingWithNil"] = "exIndexingWithNil"
}

function try(testedFunc)
	__status, __exception = pcall(testedFunc)

	--překopání názvů exceptionů na lepší názvy
	if(__status) then
		return

	elseif(string.find(exception, "attempt to index")) then
		__exception = exceptions.exIndexingNil

	elseif(string.find(exception, "attempt to call")) then
		__exception = exceptions.exCallingNil

	elseif(string.find(exception, "table index is nil")) then
		__exception = exceptions.exIndexingWithNil
	end

	__passed = false
end

function catch(err, doFunc)
	--if it is not wanted exception
	if(__status or __passed) then return end 	--žádnej exception

	if(not string.find(__exception, err)) then
		return

	--but if it is
	elseif(string.find(__exception, err)) then
		__passed = true
		doFunc()
	end
end