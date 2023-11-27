import numpy as np

class ComplexCodeGenerator:
    def __init__(self, size):
        self.size = size
        self.matrix_a = np.random.rand(size, size)
        self.matrix_b = np.random.rand(size, size)

    def multiply_matrices(self):
        result_matrix = np.zeros((self.size, self.size))
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    result_matrix[i][j] += self.matrix_a[i][k] * self.matrix_b[k][j]
        return result_matrix

    def run_complex_algorithm(self):
        intermediate_result = self.multiply_matrices()
        flattened_result = intermediate_result.flatten()
        sorted_result = sorted(flattened_result, reverse=True)
        final_result = np.array(sorted_result).reshape(self.size, self.size)
        return final_result

# Example usage
size_of_matrices = 5
complex_code_gen = ComplexCodeGenerator(size_of_matrices)
result = complex_code_gen.run_complex_algorithm()

print("Result of the randomly complex algorithm:")
print(result)
