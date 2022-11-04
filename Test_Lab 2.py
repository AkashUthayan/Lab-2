import Ex4

def test_find_min_max():
    testarr=[1,2,3]
    testarr2=[1,3]
    result = Ex4.calc_min_max_temperature(testarr)
    assert(testarr2 == result)

def test_calc_average():
    testarr=[1,2,3]
    testarr2=2
    result = Ex4.calc_average_temperature(testarr)
    assert(testarr2 == result)

def test_calc_median_temperature():
    testarr = [1, 2, 3, 4]
    testarr2 = 2.5
    result = Ex4.calc_average_temperature(testarr)
    assert (testarr2 == result)