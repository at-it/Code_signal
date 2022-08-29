"""Given an array of integers, find the pair of adjacent elements that has the largest product and return that product."""


def solution(inputArray):
    products = [x * y for x, y in zip(inputArray, inputArray[1:])]
    return max(products)
    