def ft_filter(function_to_apply, list_of_inputs):
    try:
        ret = []
        for key in list_of_inputs:
            if function_to_apply(key):
                ret.append(key)
        return ret
    except ValueError:
        print("ERROR")
        quit()
