#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
 
int call_bot() {
    printf("start cpp function\n");
     
    Py_Initialize();
     
    PyObject * sys = PyImport_ImportModule("sys");
    PyObject * path = PyObject_GetAttrString(sys, "path");
    PyList_Append(path, PyString_FromString("."));
     
    PyObject * ModuleString = PyString_FromString((char*) "bot_config");
    PyObject * Module = PyImport_Import(ModuleString);
    PyObject * Dict = PyModule_GetDict(Module);
    PyObject * Func = PyDict_GetItemString(Dict, "bot_message");
    PyObject * Result = PyObject_CallObject(Func, NULL);
     
    Py_Finalize();
}