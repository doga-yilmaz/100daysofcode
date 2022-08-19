def paint_calc(height, width, cover):
    x =round(int((height * width) / cover) + .5 )
    print(f"You'll need {x} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
