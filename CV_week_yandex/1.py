#В этом задании мы устроили подлянку, и mnist, с которым вы будете работать, теперь сломан!

#В чем проблема? У него неправильный shape.

#Ваша задача реализовать функцию transpose_from_scratch которая будет принимать list или tensor и переставлять его первые две размерности. Простенькая задачка, но использовать любые вспомогательные функции из pytorch или #numpy запрещено!

#Ниже указан формат посылки для вашего решения.

import torch
from typing import Union, List, Any

def transpose_from_scratch(
    lst: Union[List[List[Any]], torch.Tensor]
) -> torch.Tensor:
    pass
import torch
def transpose_from_scratch(lst):
    if isinstance(lst, torch.Tensor):
        lst = lst.tolist()
    transposed_lst = []
    for i in range(len(lst[0])):
        new_row = []
        for j in range(len(lst)):
            new_row.append(lst[j][i])
        transposed_lst.append(new_row)
    return torch.tensor(transposed_lst)
