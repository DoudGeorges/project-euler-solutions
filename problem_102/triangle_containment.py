def safe_division(dividend: int, divisor: int) -> float:
    if divisor == 0:
        if dividend > 0:
            return float("inf")
        elif dividend < 0:
            return float("-inf")
        else:
            return 0
    return dividend / divisor

def contains_origin(points: list) -> bool:
    result = False
    
    ax, ay, bx, by, cx, cy = points

    ma = safe_division(ay, ax)
    mb = safe_division(by, bx)

    if (cy < ma * cx) == (not by < ma * bx):
        if (cx < safe_division(cy, ma)) == (not bx < safe_division(by, ma)):
            if (cy < mb * cx) == (not ay < mb * ax):
                if (cx < safe_division(cy, mb)) == (not ax < safe_division(ay, mb)):
                    result = True

    return result

if __name__ == "__main__":
    count = 0
    with open("Problem 102/triangles.txt") as triangles:
        for triangle in triangles:
            points = [int(point) for point in triangle.split(",")]
            result = contains_origin(points)
            print(result)

            if result:
                count += 1

    print(f"{count} triangles contain the origin.")