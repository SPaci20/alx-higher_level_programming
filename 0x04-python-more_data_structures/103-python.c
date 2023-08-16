#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic information about Python lists.
 * @p: PyObject pointer to a Python list object.
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;

    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid PyListObject\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic information about Python bytes objects.
 * @p: PyObject pointer to a Python bytes object.
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid PyBytesObject\n");
        return;
    }

    printf("[.] bytes object info\n");
    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes:", size + 1 < 10 ? size + 1 : 10);
    for (i = 0; i < size + 1 && i < 10; i++) {
        printf(" %02x", (unsigned char)str[i]);
    }
    printf("\n");
}
