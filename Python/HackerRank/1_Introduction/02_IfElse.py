#!/bin/python3

import math
import os
import random
import re
import sys


def solution(n):
    if n % 2:
        return "Weird"
    else:
        if 2 <= n <= 5:
            return "Not Weird"
        elif 6 <= n <= 20:
            return "Weird"
        elif n > 20:
            return "Not Weird"


if __name__ == '__main__':
    n = int(input().strip())

    print(solution(n))
