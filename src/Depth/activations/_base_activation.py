from abc import ABC, abstractmethod
from typing import Optional

from .. import Tensor
from .._tensor import _sum_to_shape

import numpy as np

class base_activation(ABC):
    def __init__(self) -> None:
        self.activated: Optional[Tensor] = None

    @abstractmethod
    def call(self, X: Tensor) -> Tensor:
        raise NotImplementedError

    @abstractmethod
    def backward(self, preactivation: Tensor, grad: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def __call__(self, X: Tensor):
        Y = self.call(X)
        self.activated = Y

        if Y.requires_grad:
            def _backward() -> None:
                local_grad = self.backward(preactivation=X, grad=Y.grad)
                X.grad += _sum_to_shape(local_grad, X.shape)
            Y._backward = _backward
                
        return Y