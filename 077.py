t = 'maritaca', 'carambola', 'pistola', 'cicatriz', 'cigarro'
vog = 'a', 'e', 'i', 'o', 'u'
s = []
for i in t:
    for c in i:
        if c in vog:
            s.append(c)
    print(f'Na palavra {str(i).upper()} temos {str(",").join(s)}')
    s.clear()
