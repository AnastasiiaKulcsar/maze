# To be able to specify the return type which is the type of the class under definition as in
# def transpose(self) -> Matrix2Dim:
from __future__ import annotations

class IncorrectDimensionsException(Exception):
    def __init__(self, msg="The dimensions of the matrix are incorrect"):
        self.msg = msg
        super().__init__(self.msg)


class IncoherentException(Exception):
    def __init__(self, msg="The matrix is incoherent"):
        self.msg = msg
        super().__init__(self.msg)


class Matrix2Dim:
    """
    Two-dimensional matrix of integers based on a list of lists of items and a tuple that defines the dimensions
    of the matrix (number of rows and number of columns).
    """

    def __init__(self, dimensions: tuple[int, int], elements: list[list[int]] = None) -> None:
        """ Constructor
        If elements are not given, then the whole matrix is initialized with the 0 value.
        :param dimensions: tuple (pair) of the size of both the dimensions.
        (first item of dimensions corresponds to the rows, second item to the columns)
        Important: -both the dimensions must be greater or equal to 1.
                   -the matrix must be coherent.
        :param elements: content of the matrix (list of lists of elements).
        :raises IncorrectDimensionsException: if the dimensions of the matrix are incorrect.
        :raises IncoherentException: if the matrix is incoherent.
        """

        if dimensions[0] < 1 or dimensions[1] < 1:
            raise IncorrectDimensionsException()

        self._dimensions = dimensions

        if elements is None:  # initialize the elements of the matrix with 0
            self._elements = []
            for i in range(self._dimensions[0]):
                xs = [0] * self._dimensions[1]
                self._elements.append(xs)
        else:
            self._elements = elements
            if not self.is_coherent():
                raise IncoherentException()


    def get_element(self, row: int, col: int) -> int:
        """
        Getter to get an element at a given row.
        :param row: row we want to access (0...dimensions[0]-1)
        :param col: column we want to access (0...dimensions[1]-1)
        :return: the element at position (row, col)
        :raises IndexError: in case of row and col out of bound
        """
        if not (0 <= row < self._dimensions[0]) or not (0 <= col < self._dimensions[1]):
            raise IndexError("Row or column index out of bounds")
        return self._elements[row][col]


    def set_element(self, row: int, col: int, value: int) -> None:
        """
        Setter, to set an element at a given row.
        :param row: row we want to access (0...dimensions[0]-1)
        :param col: column we want to access (0...dimensions[1]-1)
        :param value: value assigned to the element at position (row, col)
        :raises IndexError: in case of row and col out of bound
        """
        if not (0 <= row < self._dimensions[0]) or not (0 <= col < self._dimensions[1]):
            raise IndexError("Row or column index out of bounds")
        self._elements[row][col] = value

    def __str__(self):
        """
        Define the way that class instance should be displayed. The __str__ method is called when
        the following functions are invoked on the object and return a string: print() and str().
        Without this function print() displays a class instance as an object and not as a human-readable way.
        :return: the human-readable string of a class instance (object).
        """
        output = "(" + str(self._dimensions[0]) + ", " + str(self._dimensions[1]) + ")" + "\n"
        for row in self._elements:
            for element in row:
                output += "|" + str(element) + "|"
            output += "\n"
        return output

    def __eq__(self, other: Matrix2Dim) -> bool:
        """
        Define the equality as structural equality, i.e. two matrices are equal if and only if
        they have the same dimensions and the same elements. With this definition of __eq__ the
        comparison of two matrices with == is now the structural equality.
        The assertion assertEqual is based on == which, that's why we have to override __eq__ like this.
        :param other: the other matrix to compare to.
        :return: true if the two matrices are equal, false otherwise.
        """
        return other._dimensions == self._dimensions and other._elements == self._elements

    def transpose(self) -> Matrix2Dim:
        """
        Perform the matrix transposition based on swapping row and column.
        :return: the transposed matrix.
        """
        transposed = [[self._elements[r][c] for r in range(self._dimensions[0])]
                      for c in range(self._dimensions[1])]
        return Matrix2Dim((self._dimensions[1], self._dimensions[0]), transposed)

    def is_symmetric(self) -> bool:
        """
        Determine if a matrix is symmetric or not.
        :return: true if the matrix is symmetric, false otherwise.
        """
        if self._dimensions[0] != self._dimensions[1]:
            return False
        for i in range(self._dimensions[0]):
            for j in range(self._dimensions[1]):
                if self._elements[i][j] != self._elements[j][i]:
                    return False
        return True

    def total(self) -> int:
        """
        :return: the sum of all the elements of the matrix.
        """
        return sum(sum(row) for row in self._elements)

    def average(self) -> float:
        """
        :return: the average of the elements of the matrix.
        """
        num_elements = self._dimensions[0] * self._dimensions[1]
        return self.total() / num_elements

    def is_coherent(self) -> bool:
        """
        Determine if the matrix is coherent.  A matrix is coherent if and only if all the lines (sub-lists) of
        elements have the same number of elements which is the number of lines in the dimension tuple and the
        number of sub-lists of elements is the same as the number of columns in the dimension tuple.
        :return: true if the matrix is coherent, false otherwise.
        """
        if len(self._elements) != self._dimensions[0]:
            return False
        for row in self._elements:
            if len(row) != self._dimensions[1]:
                return False
        return True

def main():
    matrix = Matrix2Dim((2, 3), [[0, 1, 2], [3, 4, 5]])
    print(matrix)
    print(matrix.get_element(1, 1))
    print(matrix)
    matrix2 = Matrix2Dim((3, 3))
    matrix2.set_element(1, 1, 9)
    print(matrix2)

if __name__ == "__main__":
    main()
