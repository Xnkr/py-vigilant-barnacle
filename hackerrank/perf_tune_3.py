def minimumLength(text, keys):
    for key in keys:
        if key not in text:
            return -1
    answer = 10000000
    text = "%s %s" % (text, '$')
    lidx = len(text)-1  
    for i in xrange(lidx):
        dup = list(keys)
        leng = 0
        fir = True
        for j in xrange(len(dup)):
            idx = text.find(dup[j],i)
            if idx != -1:
                if fir:
                    leng -= idx
                    fir = False
                else:
                    leng += idx+len(dup[j])
            else:
                break
            print idx,leng, text[:leng]
        if leng > 0:
            answer = min(answer,leng)


    if(answer == 10000000):
        answer = -1

    return answer

print(minimumLength("why how whywhat why what how what when what", ['why','how','what']))