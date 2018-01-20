def sort_tupple(a_tupple):
    # works but , 'exceeds' tuple boundaries
    # i = 0
    # new_tupple = ()
    # while i < len(a_tupple):
    #     new_tupple = new_tupple + a_tupple[i:i+1]
    #     i += 2
    # return new_tupple

    # much prettier than above one
    newer_tuple = ()
    for i in range(0, len(a_tupple)):
        if i % 2 == 0:
            newer_tuple += (a_tupple[i],)

    return newer_tuple

    # This works too by using enumerate and the counter i
    # newer_tuple = ()
    # for i, c in enumerate(a_tupple):
    #     if i % 2 == 0:
    #         newer_tuple += (a_tupple[i],)
    #
    # return newer_tuple


print(sort_tupple(('I', 'am', 'a', 'test', 'tuple')))
