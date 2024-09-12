def test_function():
    def inner_function():
        print('Я в области видимости функции Test_function')
    inner_function()


test_function()
# inner_function() Error