import math
import decimal

def detect_triangle(a, b, c):
	e = 1e-9
	if type(a)!=float or type(b)!=float or type(c)!=float :
		return "Nhap sai kieu du lieu."
	elif a<=0 or b<=0 or c<=0 or a>2**32-1 or b>2**32-1 or c>2**32-1 :
		return "Nhap cac gia tri > 0 va <= 2^32-1."
	else:
		temp = a
		a = max(a,b,c)
		if b==a : b = temp
		elif c==a : c = temp
		if (decimal.Decimal(b+c)<=decimal.Decimal(a)) :
			return "Day khong phai tam giac"
		elif (a==b or a==c) and b!=c:
			return "Day la tam giac can"
		elif b==c :
			if a==b :
				return "Day la tam giac deu"
			elif math.fabs(b*b*2 - a*a)<e :
				return "Day la tam giac vuong can"
			else :
				return "Day la tam giac can"
		elif math.fabs(b*b + c*c - a*a)<e :
			return "Day la tam giac vuong"
		else :
			return "Day la tam giac thuong"