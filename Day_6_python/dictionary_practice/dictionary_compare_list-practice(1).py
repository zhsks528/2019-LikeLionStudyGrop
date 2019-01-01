def check_and_clear(box):
    print("불량품이 있으면 box를 clear합니다.")
    if '불량품' in box.keys():
        box.clear()
        
box = {"불량품" : 10}
check_and_clear(box)

box = {"정상품": 10}
check_and_clear(box)
