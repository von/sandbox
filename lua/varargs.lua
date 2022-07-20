#!/usr/bin/env lua
-- Example of variables arguments and use of ellipses in lua

function foo(...)
  local args = {...}
  for i,v in ipairs(args) do
    print(v)
  end
end

foo(1, 2, 3, 4)
