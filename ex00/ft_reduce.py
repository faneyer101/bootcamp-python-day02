def ft_reduce(function_to_apply, list_of_inputs):
    try:
        ret = list_of_inputs[0]
        for key in list_of_inputs[1:]:
            ret = function_to_apply(key, ret)
        return ret
    except ValueError:
        print("ERROR")
        quit()
