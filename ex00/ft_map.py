def ft_map(function_to_apply, list_of_inputs):
    try:
        rep = []
        for i in list_of_inputs:
            rep.append(function_to_apply(i))
        return rep
    except ValueError:
        print("ERROR")
        quit()
