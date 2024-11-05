# CustomLogicList

`CustomList` is a Python class that extends the built-in `list` type, adding custom methods for inserting, deleting, searching, and displaying list elements with added flexibility. It also includes static methods to perform operations on lists without modifying the `CustomList` instance itself.


## Features

The `CustomList` class provides several useful methods:

1. **Insert** - Inserts an element at a specified index in the list.
2. **Delete_by_value** - Deletes the first occurrence of a specified value in the list.
3. **Delete_by_index** - Deletes the element at a specified index.
4. **Display** - Custom display method that prints elements in a formatted way.
5. **Append** - Appends an element to the end of the list.
6. **Reverse** - A static method to reverse any given list in place.
7. **Search_by_value** - Searches for the first occurrence of a specified value in the list and returns its index.

## Usage

### Initialization

```python
# Initialize a CustomList object with a list of values
original_array = [1, 2, 3, 4]
array = CustomList(original_array)
```
#### Now use the Metods

## Notes
- `Insert` and `Delete_by_value` create **copies** of the list to maintain a clean structure,  also `Delete_by_value` returns **deleted index number**.
- `Reverse` is a static method, which means it can be used without an instance of CustomList.
- `Display` provides a customized print format for better readability.

<hr>

### Thanks for watching 
#### powered by shinigami110
