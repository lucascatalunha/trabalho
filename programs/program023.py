def area_of_circle(radio: int) -> int:
    return float(f"{(radio**2) * pi:.2f}")


pi = 3.1416

if __name__ == "__main__":
    print(area_of_circle(10))
