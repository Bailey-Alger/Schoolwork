rectOneLength = float(input('Enter the length of Rectangle One: '))
rectOneWidth = float(input('Enter the width of Rectangle One: '))
rectTwoLength = float(input('Enter the length of Rectangle Two: '))
rectTwoWidth = float(input('Enter the width of Rectangle Two: '))

rectOneArea = float(rectOneLength*rectOneWidth)
rectTwoArea = float(rectOneLength*rectOneWidth)

if rectOneArea > rectTwoArea:
    text = 'Rectangle One has the greater area'
if rectTwoArea > rectOneArea:
    text = 'Rectangle Two has the greater area'
if rectOneArea == rectTwoArea:
    text = 'The two rectangles have the same area'
else:
    text = 'error'


print(text)
