#!/usr/bin/env lua
-- Demonstrate use of closures with callbacks.

function callback(msg)
  print("Callback received with state: " .. msg)
end

function backcaller(cb)
  print("Calling callback...")
  cb()
  print("Back from callback...")
end

local message="Hello world"

backcaller(
  function()
    print("In closure, before callback...")
    callback(message)
    print("In closure, after callback...")
  end
  )
os.exit(0)
