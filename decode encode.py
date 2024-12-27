def decode(encode):
    decoded=" "#final output
    i=0
    while i<len(encode):
        count=int(encode[i])
        i+=1
        decoded+=encode[i]*count
        i+=1#move to next
        
    return decoded
encode="3a2b1c"
d=decode(encode)
print(d)