
import math

def main():
    n_items=int(input("Enter the number of items: "))
    n_items_box=int(input("Enter the number of items: "))

    n_boxes = calculate(n_items,n_items_box)

    print(f'For {n_items} items, packing {n_items_box} items in each box, you will need {n_boxes} boxes.')

def calculate(items, items_box):
    
    boxes_f=math.ceil(items/items_box)
    return boxes_f

main()