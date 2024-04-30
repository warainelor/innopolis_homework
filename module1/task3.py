global_variable = 1


def variable_func(param):
    outer_variable = 2

    def sum_variables(param_variable):
        inner_variable = 3
        return global_variable + outer_variable + inner_variable + param_variable
    return sum_variables(param)


print(variable_func(4)) # 10 = 4 + 3 + 2 + 1
