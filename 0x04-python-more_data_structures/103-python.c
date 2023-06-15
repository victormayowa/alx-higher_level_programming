#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about a Python list
 * @p: Pointer to the Python object (list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyListObject *list;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	list = (PyListObject *)p;
	printf("[*] Allocated = %zd\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		if (strcmp(Py_TYPE(PyList_GetItem(p, i))->tp_name, "bytes") == 0)
			print_python_bytes(PyList_GetItem(p, i));
	}
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: Pointer to the Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", (size + 1 < 10) ? size + 1 : 10);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02x", string[i] & 0xff);
	printf("\n");
}
