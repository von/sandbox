#!/usr/bin/env lua
-- Show examples of __index() and __newindex()

-- __index() will be accessed whenever trying to access missing key
-- on a table. It will be called with two parameters, the table
-- and the key, as a string.
-- See https://www.lua.org/pil/13.4.1.html
index = function(tbl, key)
  print(string.format("__index(): Getting key \"%s\" for table %s", key, tbl))
  -- rawget() gets a value from table without using __index
  return rawget(tbl, key)
end

o = {}
print(string.format("Object created: %s", o))
o.a = "An apple"

o.mt = { __index = index }
setmetatable(o, o.mt)

print("Getting 'a' - should be found without invoking __index()")
print(o.a)
print("Getting 'b' - should invoke __index() and then fail")
print(o.b)

print("Setting 'a' - should not invoke __index()")
o.a = "Another apple"
print(o.a)
print("Setting 'b' - should not invoke __index()")
o.b = "Better butter"
print(o.b)

-- __newindex() will be invoked when trying to set a missing key
-- on a table. It will be called with three parameters, the table,
-- the key, and the value.
-- See https://www.lua.org/pil/13.4.2.html
newindex = function(tbl, key, value)
  print(string.format("__newindex(): Setting key \"%s\" for table %s to \"%s\"",
    key, tbl, value))
  -- rawset() gets a value from table without using __newindex
  return rawset(tbl, key, value)
end

print("Setting __newindex in metatable")
o.mt.__newindex = newindex


print("Setting 'a' - should not invoke __newindex()")
o.a = "An amazing apple"
print(o.a)
print("Setting 'c' - should invoke __newindex()")
o.c = "Charming cherry"
print(o.c)
