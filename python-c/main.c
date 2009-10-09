#include "Python.h"
#include <stdio.h>

int main()
{
    FILE *pyFile;
    PyObject*main_module, * global_dict, * function, *function2;
    PyObject *i1, *i2;
    PyObject *args;
    PyObject *list, *list2;
    int i;
    
    Py_Initialize();
    pyFile = fopen("test.py", "r");
    PyRun_SimpleString("print \"hello world\"");
    PyRun_SimpleFile(pyFile, "test.py");
    fclose(pyFile);
    pyFile = NULL;

    /* Get pointer to python function */
    main_module = PyImport_AddModule("__main__");
    global_dict = PyModule_GetDict(main_module);
    function = PyDict_GetItemString(global_dict, "myFunction");

    /* Call with native C integers */
    list = PyObject_CallFunction(function, "ii", 7, 9);
    for (i = 0; i<PyList_Size(list); i++)
    {
        printf("%d: %ld\n", i, PyInt_AsLong(PyList_GetItem(list, i)));
    }
    Py_CLEAR(list);
    
    /* Call with PyObjects */
    i1 = PyInt_FromLong(8);
    i2 = PyInt_FromLong(99);    
    args = PyTuple_Pack(2, i1, i2);
    list = PyObject_CallObject(function, args);
    for (i = 0; i<PyList_Size(list); i++)
    {
        printf("%d: %ld\n", i, PyInt_AsLong(PyList_GetItem(list, i)));
    }
    Py_CLEAR(list);
    Py_CLEAR(args);

    /* Play with lists */
    function2 = PyDict_GetItemString(global_dict, "myListFunction");
    list = PyList_New(0);
    for (i=0;i<10;i++)
    {
        PyList_Append(list, PyInt_FromLong(i));
    }
    args = PyTuple_Pack(1, list);
    list2 = PyObject_CallObject(function2, args);
    for (i = 0; i<PyList_Size(list2); i++)
    {
        printf("%d: %ld\n", i, PyInt_AsLong(PyList_GetItem(list2, i)));
    }

    /* Clean up */
    Py_CLEAR(i1);
    Py_CLEAR(i2);
    Py_CLEAR(function);
    Py_CLEAR(list);
    /* These cause problems...
    Py_CLEAR(global_dict);
    Py_CLEAR(main_module);
    */

    Py_Finalize();
}


