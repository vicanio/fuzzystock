def meb(x,a,b,c):
	if x < a :
		return 0
	if x > a and x <= b:
		return (x-a)/(b-a)
	if (x > b) and (x <= c):
		return (c-x)/(c-b)
	if x > c:
		return 0
	if a == b :
		if x <= b:
			return 1
		if (x > b) and (x <= c):
			return (c-x)/(c-b)
		if x > c:
			return 0
	if b == c:
		if x <= a:
			return 0
    if (x > a) and (x <= b):
        return (x-a)/(b-a)
    if x > b:
        return 1
