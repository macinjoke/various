# coding: UTF-8
# for ループ (辞書)
users = {"taguchi":200, "fkoji":300, "dotinstall":500}
for key, value in users.items():
    print("key: %s value: %d" % (key, value))
for key in users.keys():
    print("key: %s" % key)
for value in users.values():
    print("value: %d" % value)
