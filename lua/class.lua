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
  local instance = setmetatable({}, MyClass)
  instance.value = init
  return instance
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
print("Subclass stuff...")

-- Given a class, return a table set up as a subclass
-- Could easily be a method on class
function make_subclass(cls)
  local subcls = {}

  -- Failed table lookups on the instances should fallback to the subclass table
  subcls.__index = subcls

  -- Syntaxic sugar
  subcls.__super = cls

  -- Inheritance: Failed lookups on subclass go to superclass
  setmetatable(subcls, {
    __index = cls
  })

  return subcls
end

local MySubClass = make_subclass(MyClass)

function MySubClass.new(init)
  -- Create a new instance of MyClass, but give it metatable of subclass
  local instance = setmetatable(MyClass.new(init), MySubClass)
  return instance
end

-- Calls to MySubClass() return MySubClass.new()
-- Could do this in make_subclass(), but isn't actually
-- required for subclass.
getmetatable(MySubClass).__call = function (cls, ...) return cls.new(...) end

function MySubClass:increment_value()
  self.value = self.value + 1
end

s = MySubClass(21)
print("The answer is " .. s:get_value())
s:set_value(42)
print("The answer is " .. s:get_value())
s:increment_value()
print("The answer is " .. s:get_value())
