#!/usr/bin/env hs
-- Demonstrate using hs.canvas with multiple screens.
-- Will show a red circle on each screen moving to each corner of the screen
-- over 8 seeconds.

-- I would use hs.canvas:copy() but it seems broken.
-- https://github.com/Hammerspoon/hammerspoon/issues/3303
function make_canvas()
  local g = {x=50, y=50, h=50, w=50}
  return hs.canvas.new(g):appendElements({
      type = "circle",
      center = { x = ".5", y = ".5" },
      radius = ".5",
      fillColor = { alpha = 1.0, red = 1.0 },
      action = "fill"
    })
end

hs.fnutils.each(
  hs.screen.allScreens(),
  function(s)
    local f = s:fullFrame()
    hs.printf("Screen %s: %d %d", s:name(), f.x, f.y)
    local c = make_canvas()
    c:topLeft({x = f.x + 50, y=f.y + 50})
    c:show()
    hs.timer.doAfter(2,
      function() c:topLeft({ x = f.x + f.w - 100, y = f.y + 50 }) end)
    hs.timer.doAfter(4,
      function() c:topLeft({ x = f.x + f.w - 100, y = f.y + f.h - 100 }) end)
    hs.timer.doAfter(6,
      function() c:topLeft({ x = f.x + 50, y = f.y + f.h - 100 }) end)
    hs.timer.doAfter(8, function() c:delete() end)
  end)
