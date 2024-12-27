def fare(miles,minutes,surge_multiplier):
    base=2.5
    if miles<0 and minutes<0:
        raise ValueError ("-ve values so error")
    miles*=1.5
    minutes*=0.25
    s=(base+miles+minutes)*surge_multiplier
    return s
    
try:
    miles=float(input())
    minutes=float(input())
    surge_multiplier=float(input())
    