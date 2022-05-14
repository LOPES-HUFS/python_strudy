# unprinted_designs = ['phone case', 'robot pendant', 'dodecaheron']
# completed_models = []

# while unprinted_designs :
#     current_design = unprinted_designs.pop()
#     print(f"unprinted_designs model:{unprinted_designs}")
#     print(f"Printing model:{current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

print("\n함수로 만든 것 실행하기")

def print_models(unprinted_designs, completed_models):
    while unprinted_designs :
        print(f"사본:{unprinted_designs}")
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_model(completed_model):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecaheron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_model(completed_models)
print(f"원본:{unprinted_designs}")