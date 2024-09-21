#21.1
def sandvich(*components):
    for component in components:
        print(component)
sandvich('колбаса','сыр','огурцы')
sandvich('колбаса','сыр','огурцы','помидор')
sandvich('колбаса','сыр','огурцы','помидор','соус')
#21.2
def build_profile(*names):
    for name in names:
        print(name)
build_profile("Худи","Егор")
build_profile("Сергиенко","Влад")
build_profile("Карпилянский","Марк")
#21.3
def super_car(first,last,**info):
    info['first_name']=first
    info['last_name']=last
    return info
car_info=super_car('Mersedes','Lada',color='black', horse_power='1000')
print(car_info)
