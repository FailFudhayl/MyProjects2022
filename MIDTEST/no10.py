a= input('Masukkan String: ')

a= a.replace('-#-', 'e')
a= a.replace(';--;', 'b')
a= a.replace('_', 'a')
a= a.replace('*', 'c')
a= a.replace('<=+=>', 't')
a= a.replace('###', 'n')
a= a.replace('^^^', ' ')

print('Hasil Dekode:',a)

input_set=[
    ['s_;--;_r^^^i###i^^^*o;--;__###'],
    ['q-#-r;--;i_yy*_###sk_ji###r-#-w<=+=>'],
    ['_ri-#-l^^^p-#-<=+=>-#-rp_###'],
    ['-#-;--;_*<=+=>###']
]