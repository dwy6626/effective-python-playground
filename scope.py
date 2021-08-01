def func():
    a = 0
    def func_inner():
        nonlocal a
        a = 1

    func_inner()
    print(a)

func()
