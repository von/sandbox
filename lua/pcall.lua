#!/usr/bin/env lua
-- Demonstration of protected calling with pcall()
-- Kudos:
-- https://www.lua.org/pil/8.4.html
-- https://riptutorial.com/lua/example/16000/using-pcall

function f1(v)
  error("Fail..." .. v)
end

-- First argument to pcall() is function, others are passed as arguments to function
result, err = pcall(f1, "Alas")

if not result then
  print("f1() failed as expected: " .. err)
end

-- Use xpcall() to get stack trace
-- Kudos: https://stackoverflow.com/a/45788987/197789
function f1wrapper(...)
  f1(...)
end

result, err = xpcall(f1wrapper, debug.traceback, "Alas")

print("f1wrapper() trace: " .. err)

function f2()
  return "Hello world"
end

-- One can get results out of pcall with a closure
-- (Assuming the closure doesn't throw an error)
local msg=""
result, err = pcall(function() msg=f2() end)
print("Return value from f2(): " .. msg)

-- Example of non-string
function f3()
  error({code=10, msg="Crash and burn"})
end

result, err = pcall(f3)
print(string.format("Code = %d, msg=%s", err.code, err.msg))

os.exit(0)
