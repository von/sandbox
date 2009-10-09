#!/bin/sh
files=`find . -name \*.class`
jar cvmf Manifest test.jar $files
