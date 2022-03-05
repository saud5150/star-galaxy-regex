import re
mylist = ["our_sun-123#hd186302.milkyway", "cat", "wildcat", "thundercat", "cow", "hooo"]
r = re.compile("[a-zA-Z]+_[a-zA-Z]+-.*#[a-zA-Z]+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?[a-zA-Z]+")
newlist = list(filter(r.match, mylist)) 
print(newlist)
