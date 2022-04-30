import math

def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]
def chunk_list(lst: list, c_num=2) -> list:
    return list(func_chunks_generators(lst, c_num))