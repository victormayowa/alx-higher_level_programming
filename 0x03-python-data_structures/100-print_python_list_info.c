#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - singly linked list
 * @p: integer
 * Description: singly linked list node structure
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}
