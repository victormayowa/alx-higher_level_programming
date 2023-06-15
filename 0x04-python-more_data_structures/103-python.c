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
	printf("[*] Size of the Python List = %ld\n", size);
	list = (PyListObject *)p;
	printf("[*] Allocated = %zd\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, type);
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
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes:", (size > 10 ? 10 : 10));
	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf(" %02x", (unsigned char)bytes->ob_sval[i]);
		if (i < 9)
			printf(" ");
	}
	printf("\n");
}
