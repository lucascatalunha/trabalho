def face_interval(a, b):
    return min(abs(a - b), 12 - abs(a - b))


if __name__ == "__main__":
    print(face_interval(3, 9))
    print(face_interval(10, 2))
