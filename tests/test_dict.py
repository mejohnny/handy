from handy.dict.mixedict import delkey,isin

def test_delkey():
    testdata = {1:111,2:222,3:{1:1111,2:2222},4:{1:1,2:2,3:3,4:4,5:{1:11}}}
    targetkey = list(testdata.keys())[0]
    delkey(testdata,targetkey)
    assert(not isin(testdata,targetkey))