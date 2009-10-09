import cgi
import cgitb
import os
import os.path
import re
import string

cgitb.enable()

class webapp:
    # Name of form variable to use to specify action
    actionVar = "action"

    # Name of form variable used to store names of state variables
    stateVar = "STATE_VARIABLES"

    # Initial state of the web application
    initialState = {}

    def __init__(self, htmlPath=None):
	self.form = cgi.FieldStorage()
	self.htmlPath = htmlPath
	self.state = self._getState()

    def getAction(self):
	return self.getVar(self.actionVar, "default")

    def getVar(self, var, default=None):
	return self.form.getfirst(var, default)
    
    def getList(self, var):
	return self.form.getlist(var)

    def run(self):
	self.dispatch(self.getAction())

    def dispatch(self, action):
	methodName = "action" + action.capitalize()
	method = getattr(self, methodName, None)
	if ((method is None) or
	    (not callable(method))):
	    self.error("Unknown action \"%s\"" % action)
	method()

    def printContentHeader(self, contentType="text/html"):
	print "Content-Type: %s" % contentType
	print ""

    def printHTML(self, filename, dict=None):
	d = self._makeTemplateDict(dict)
	includeRegex = re.compile(r"^\$include\((\S+)\)\s*$")
	path = os.path.join(self.htmlPath, filename)
	f = file(path, "r")
	for line in f:
	    match = includeRegex.search(line)
	    if match:
		self.include(match.group(1))
	    else:
		print string.Template(line).safe_substitute(d)
	f.close()

    def _makeTemplateDict(self, dict):
	d = {}
	d.update(os.environ)
	d.update(self.state)
	if dict is not None:
	    d.update(dict)
	d["FORM_STATE"] = self._getFormStateHTML()
	return d

    def printPage(self, filename, dict=None):
	self.printContentHeader()
	self.printHTML(filename, dict)

    def include(self, filename):
	self.printHTML(filename)

    def error(self, msg):
	self.printContentHeader("text/plain")
	print msg
	sys.exit(1)

    def printEnviron(self):
	"""Print environment as html"""
	cgi.print_environ()

    def printForm(self):
	"""Print contents of form as html."""
	cgi.print_form(self.form)

    def printState(self):
	"""Print contents of form state as html."""
	vars = self.state.keys()
	if len(vars):
	    print "<dl>"
	    for var in self.state.keys():
		print "<dt>%s</dt><dd>%s</dd>" % (var, self.state[var])
	    print "</dl>"
	else:
	    print "No state.<br>"
	    
    def _getState(self):
	stateVars = self.getList(self.stateVar)
	state = self.initialState
	for var in stateVars:
	    value = self.getVar(var)
	    if value.find("int:") != -1:
		value = int(value[4:])
	    state[var] = value
	return state

    def _getFormStateHTML(self):
	"""Return form state in HTML suitable for inclusion in a form."""
	s=""
	for var in self.state.keys():
	    s += "<input type=hidden name=\"%s\" value=\"%s\"/>\n" % (self.stateVar,
								      var)
	    value = self.state[var]
	    if isinstance(value, int):
		value = "int:%d" % value
	    s += "<input type=hidden name=\"%s\" value=\"%s\"/>\n" % (var,
								      value)
	return s
