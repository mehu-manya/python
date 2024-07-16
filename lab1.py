def print_box(symbol,width,height):
    if len(symbol)!=1:
        raise ValueError("symbol length must be 1")
    if width <=2 or height <=2 :
        raise ValueError("width and height must be greater than 2")
    for i in range(height):
        if i==0 or i==height-1:
            print(symbol*width)
        else:
            print(symbol + " " *(width-2)+ symbol)


try:
    symbol =input("enter a symbol(use '*'or 'O'):")
    width=int(input("enter the width:"))
    height=int(input("enter the height:"))
    print_box(symbol,width,height)
except ValueError as e:
    print(f"error:{e}")