
def main():
    n_items=int(input("Enter the number of items: "))
    n_items_box=int(input("Enter the number of items: "))

    n_boxes = calculate(n_items,n_items_box)

    print(f'For {n_items} items, packing {n_items_box} items in each box, you will need {n_boxes} boxes.')

def calculate(items, items_box):
    
    if items%items_box==0:
        boxes_f=items//items_box
    else:
        boxes_f=items//items_box + 1

    return boxes_f

main()