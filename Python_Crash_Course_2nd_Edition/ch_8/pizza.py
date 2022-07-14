def make_pizza(size, *toppings):
    print("\n 다음과 같은 토핑으로 {size}인치 피자를 만들려고 합니다:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza(12, "페파로니","추가 치즈")