# encoding=utf-8
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后, 都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)
