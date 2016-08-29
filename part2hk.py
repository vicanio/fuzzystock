
def followBB:
	N = 999 #回测天数
	p00[] = 0 #价格
	v00[] = 0 #成交量
	dir00[] = 0  #日期
	for k in range(1,N):
		p00[k] = 0  
		v00[k] = 0  
		dir00[k] = 0   
	n1 = 2000   #'2013-1-4'
	n2 = 2300   $'2014-6-5'
	if n1 < 1 
		n1 = 1
	p0[] = 0
	for k in range(n1-245,n2):
		p[k] = p00[k]
	ns=0
	pm=0
	pv=0
	p4=0
	r[] = 0
	for k in range(n1+1,n2):
		r[k] = math.log(p[k]/p[k-1])
		if abs(r(k))<0.1:
			ns=ns+1
			pm=pm+abs(r(k))
			pv=pv+r(k)*r(k)
			p4=p4+r(k)^4
	pm=pm/ns
	pv=pv/ns
	p4=p4/ns
	lmd=0.95
	c=0.01
    
		
	
