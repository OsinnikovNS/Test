class Backpack:
    """Рюкзак"""
    def __init__ (self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)
    def __str__ (self):
        return 'Рюкзак: ' + ','.join(self.content)


    def __eq__ (self, other):
        return self.content == other.content

my_backpack = Backpack(gift='бутерброд, хлеб, масло')
san_backpack = Backpack(gift='бутерброд, хлеб')
print(my_backpack)
print(san_backpack)

if  san_backpack == my_backpack:
    print('соответствие')
else:
    print('не соответствие')
