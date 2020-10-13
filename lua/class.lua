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


-- Inheritance
-- Kudos: https://ozzypig.com/2018/05/10/object-oriented-programming-in-lua-part-5-inheritance
local MySubClass = {}

-- Failed table lookups on the instances should fallback to the subclass table
MySubClass.__index = MySubClass

setmetatable(MySubClass, {
  -- Calls to MySubClass() return MySubClass.new()
  __call = function (cls, ...)
    return cls.new(...)
  end,
  -- Inheritance
  -- Failed lookips on class, go to superclass
  __index = MyClass
})

function MySubClass.new(init)
  -- Create a new instance of MyClass, but give it metatable of subclass
  local self = setmetatable(MyClass.new(init), MySubClass)
  return self
end

function MySubClass:increment_value()
  self.value = self.value + 1
end

s = MySubClass(21)
print("The answer is " .. s:get_value())
s:set_value(42)
print("The answer is " .. s:get_value())
s:increment_value()
print("The answer is " .. s:get_value())
