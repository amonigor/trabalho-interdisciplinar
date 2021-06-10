import numpy as np

class Calcular:
    def coeficiente_correlacao(self, arr1, arr2):
        corr = np.corrcoef(arr1, arr2)
        return corr[0][1]
    
    def regressao_linear(self, arr1, arr2):
        arr2 = np.array([np.ones(np.size(arr2)), arr2])
        mi = np.linalg.inv(np.dot(arr2, np.transpose(arr2)))
        [b, a] = np.dot(mi, np.dot(arr2, np.transpose(arr1)))

        return [b, a]
    
    def regressao_multivariada(self, arr1, arr2, arr3):
        prod = np.dot(arr2, (arr1 * np.ones((np.size(arr1), np.size(arr1))) * np.eye(np.size(arr1))))

        x = np.array([np.ones(np.size(arr1)), arr1, arr2, prod])

        result = np.dot(
            np.linalg.inv(
                np.dot(x, np.transpose(x))
            ),
            np.dot(x, np.transpose(arr3))
        )

        return result