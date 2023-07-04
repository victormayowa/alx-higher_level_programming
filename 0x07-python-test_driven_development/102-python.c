#include <Python.h>

/**
 * print_python_string - functiom
 * @p: args
 * Return: null
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	const char *value;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	length = PyUnicode_GET_LENGTH(p);
	value = PyUnicode_AsUTF8(p);
	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
	printf("  length: %ld\n", length);
	printf("  value: %s\n", value);
}
