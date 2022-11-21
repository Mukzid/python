import country_converter as coco

def find_country_match(input):
    cc = coco.convert(names=[input], to='ISO2')
    print("cc iso2: ",cc)
    cc = coco.convert(names=[input], to='name_short')
    print("name_short: ",cc)
    cc = coco.convert(names=[input], to='long_name')
    print("name_long: ",cc)
    cc = coco.convert(names=[input], to='name_official')
    print("name_official: ",cc)
        
input = "United Kingdom"
find_country_match(input)

def test():
    cc = " "
    if cc:
        print("yes")
    else:
        print("no")
        
test()