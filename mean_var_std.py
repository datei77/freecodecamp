import numpy as np

def calculate(no):
    if len(no) != 9:
        raise ValueError("List must contain nine numbers."
    
    ma = np.array(no).reshape((3, 3)
    result = {
        'mean': 
        [
            np.mean(ma, axis=0).tolist(),   
            np.mean(ma, axis=1).tolist(),   
            float(np.mean(ma))              
        ],
        'variance': 
        [
            np.var(ma, axis=0).tolist(),
            np.var(ma, axis=1).tolist(),
            float(np.var(ma))
        ],
        'standard deviation': 
        [
            np.std(ma, axis=0).tolist(),
            np.std(ma, axis=1).tolist(),
            float(np.std(ma))
        ],
        'max': 
        [
            np.max(ma, axis=0).tolist(),
            np.max(ma, axis=1).tolist(),
            int(np.max(ma))
        ],
        'min': 
        [
            np.min(ma, axis=0).tolist(),
            np.min(ma, axis=1).tolist(),
            int(np.min(ma))
        ],
        'sum': 
        [
            np.sum(ma, axis=0).tolist(),
            np.sum(ma, axis=1).tolist(),
            int(np.sum(ma))
        ]
    }
    return result
