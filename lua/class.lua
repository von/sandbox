#!/usr/bin/env lua
-- Example of a class in Lua
-- Kudos: http://lua-users.org/wiki/ObjectOrientationTutorial

-- The table representing the class, which will double as the metatable for the instances
local MyClass = {}

-- Failed table lookups on the instances should fallback to the class table, to get methods
MyClass.__index = MyClass

-- Calls to MyClass() return MyClass.new()
setmetatable(MyClass, {
  __call = function (cls, ...)
    return cls.new(...)
  end,
})

-- syntax equivalent to "MyClass.new = function..."
function MyClass.new(init)
  local self = setmetatable({}, MyClass)
  self.value = init
  return self
end

-- Examples methods
-- The colon syntact causes 'self' to be automatically set
function MyClass:set_value(newval)
  self.value = newval
end

function MyClass:get_value()
  return self.value
end

-- If module, we would normally return class definition here
-- return MyClass

-- Instead, we'll show it off
c = MyClass(21)
print("The answer is " .. c:get_value())
c:set_value(42)
print("The answer is " .. c:get_value())
