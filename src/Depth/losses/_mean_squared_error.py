from .. import Tensor
from ._base_loss import base_loss

import numpy as np

class MeanSquaredError(base_loss):
    def call(self, y_true: Tensor, y_pred: Tensor) -> Tensor:
        return Tensor(
            data=np.sum(np.square(y_true.data - y_pred.data), axis=-1),
            prev=(y_true, y_pred), requires_grad=y_true.requires_grad or y_pred.requires_grad, dtype=y_true.dtype
        )
    
    def backward(self, y_true: Tensor, y_pred: Tensor) -> np.ndarray:
        L = y_pred.data - y_true.data
        return (2 / y_pred.size) * L