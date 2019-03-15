#!/usr/bin/osascript
// Print list of Chrome windows getting list directly and via System
var chromeApp = Application('Google Chrome');
var appWindows = chromeApp.windows();

var system = Application('System Events');
var app = system.processes['Google Chrome'];
// Filter windows without titles
var sysWindows = app.windows().filter(function hasTitle(w) {return w.title()});

console.log("These two lists of windows seem to match")
console.log("App windows");
for (var i in appWindows) {console.log(appWindows[i].title())}
console.log("Sys windows");
for (var i in sysWindows) {console.log(sysWindows[i].title())}
