import numpy as np
from scipy.stats import norm

chat_id = 843200348


def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    p = 0.05
    norm_ppf = norm.ppf(p)
    diff_p = (x_success + y_success) / (x_cnt + y_cnt)
    return (y_success / y_cnt - x_success / x_cnt) / np.sqrt(
        diff_p * (1 - diff_p) / x_cnt + diff_p * (1 - diff_p) / y_cnt) < norm_ppf
