#!/usr/bin/env hs
-- Demonstrate using hs.canvas and changing colors.
-- Will show a red circle and then change it's color twice.

local g = {x=50, y=50, h=50, w=50}
local c = hs.canvas.new(g):appendElements({
    type = "circle",
    center = { x = ".5", y = ".5" },
    radius = ".5",
    fillColor = { alpha = 1.0, red = 1.0 },
    action = "fill"
  })
c:topLeft({50, 50})
c:show()

hs.timer.doAfter(2, function() c[1].fillColor = { alpha = 1.0, green = 1.0 } end)
hs.timer.doAfter(4, function() c[1].fillColor = { alpha = 1.0, blue = 1.0 } end)
hs.timer.doAfter(6, function() c:delete() end)
