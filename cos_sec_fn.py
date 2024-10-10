## cos function
inp_val=float(input("Enter value in degree: "))
def cos_fn(val):
    rad_val=val*0.01744
    if rad_val>3.14:
        rad_val=(2*3.14)-rad_val
    elif rad_val>(3.14/2):
        rad_val=3.14-rad_val
    res=1-(((rad_val)**2)/2)+(((rad_val)**4)/24)-(((rad_val)**6)/720)
    return res
cos_fn(inp_val)

## sec function
inp_val=float(input("Enter value in degree: "))
def sec_fn(val):
    rad_val=val*0.01744
    if rad_val>3.14:
        rad_val=(2*3.14)-rad_val
    elif rad_val>(3.14/2):
        rad_val=3.14-rad_val
    res=1/(1-(((rad_val)**2)/2)+(((rad_val)**4)/24)-(((rad_val)**6)/720))
    return res
sec_fn(inp_val)
