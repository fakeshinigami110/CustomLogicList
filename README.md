# CustomLogicList

`CustomList` is a Python class that extends the built-in `list` type, adding custom methods for inserting, deleting, searching, and displaying list elements with added flexibility. All operations are implemented from scratch without using built-in Python list methods, providing a deeper understanding of list manipulation.

## Features

The `CustomList` class provides several custom-implemented methods:

1. **Insert** - Inserts an element at a specified index in the list.
2. **Delete_by_value** - Deletes the first occurrence of a specified value and returns its index.
3. **Delete_by_index** - Deletes the element at a specified index.
4. **Display** - Custom display method that prints elements in a formatted way.
5. **Append** - Appends an element to the end of the list.
6. **Reverse** - A static method to reverse any given list in place.
7. **Search_by_value** - Searches for the first occurrence of a value and returns its index.

### Internal Methods

The class also includes custom implementations of fundamental list operations:

- `_calculate_length` - Custom implementation of length calculation without using `len()`
- `_custom_clear_extend` - Custom implementation of list clearing and extending

## Usage

### Initialization

```python
# Initialize a CustomList object with a list of values
original_array = [1, 2, 3, 4]
array = CustomList(original_array)
print(f"Original array: {array}")  # Output: Original array: [1, 2, 3, 4]
```

### Using the Methods

```python
# Insert value at specific index
array.Insert(1, 10)
print(f"After inserting 10 at index 1: {array}")  # [1, 10, 2, 3, 4]

# Delete by value (returns deleted index)
deleted_index = array.Delete_by_value(4)
print(f"After deleting 4: {array}, deleted from index: {deleted_index}")

# Delete by index
array.Delete_by_index(2)
print(f"After deleting index 2: {array}")

# Append value
array.Append(5)
print(f"After appending 5: {array}")

# Reverse array (static method)
CustomList.Reverse(array)
print(f"After reversing: {array}")

# Display formatted output
print("Display method output:", end=" ")
array.Display()

# Search for value
index = array.Search_by_value(5)
print(f"Index of value 5: {index}")
```

## Implementation Details

- All operations are implemented from scratch without using built-in Python list methods
- `Insert` and `Delete` operations create temporary copies to maintain data integrity
- `Delete_by_value` returns the index of the deleted element (or None if not found)
- `Reverse` is implemented as a static method for broader utility
- `Display` provides a custom format with proper comma separation
- Internal methods use underscore prefix following Python conventions

## Notes

- Operations like clear and extend are implemented without using built-in Python methods
- Length calculations are done manually without using `len()`
- All methods maintain the original list structure while performing operations
- The class provides a complete suite of basic list operations implemented from scratch
- Error handling for edge cases is implemented where necessary

<hr>

### Thanks for watching 
#### powered by shinigami110