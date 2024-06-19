import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    A = np.array(list).reshape(3, 3)
    calculations = {}

    calculations.update({'mean' : [np.mean(A, axis=0).tolist(), np.mean(A, axis=1).tolist(), float(np.mean(A))]})
    calculations.update({'variance' : [np.var(A, axis=0).tolist(), np.var(A, axis=1).tolist(), float(np.var(A))]})
    calculations.update({'standard deviation' : [np.std(A, axis=0).tolist(), np.std(A, axis=1).tolist(), float(np.std(A))]})
    calculations.update({'max' : [np.max(A, axis=0).tolist(), np.max(A, axis=1).tolist(), float(np.max(A))]})
    calculations.update({'min' : [np.min(A, axis=0).tolist(), np.min(A, axis=1).tolist(), float(np.min(A))]})
    calculations.update({'sum' : [np.sum(A, axis=0).tolist(), np.sum(A, axis=1).tolist(), float(np.sum(A))]})

    return calculations