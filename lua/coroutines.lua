#!/usr/bin/env lua

print("Basic coroutine showing passing in of values and receiving them back")
c1 = coroutine.create(
  function(a,b)
    coroutine.yield(a+b)
  end)

status,value = coroutine.resume(c1, 5, 7)
print("5 + 7 = " .. value)

print("Coroutine with state...")
print("Will sum values provided to it.")
c2 = coroutine.create(
  function(i)
    while true do
      i = i + coroutine.yield(i)
    end
  end)

for j = 1,10 do
  status,value = coroutine.resume(c2, j)
  if not status then
    break
  end
  print(value)
end

print("Same coroutine with coroutine.wrap()")
c3 = coroutine.wrap(
  function(i)
    while true do
      i = i + coroutine.yield(i)
    end
  end)

for j = 1,10 do
  -- No access to status, will raise an error if an arror occurrs
  value = c3(j)
  print(value)
end
