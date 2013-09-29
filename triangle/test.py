from triangle import detect_triangle
import unittest
import math
import decimal

class TriangleTest(unittest.TestCase):
	def test_1(self) :
		self.assertEqual(detect_triangle('1.0',1.2,3.1), "Nhap sai kieu du lieu.")
	def test_2(self) :
		self.assertEqual(detect_triangle(-1.0,1.2,3.1), "Nhap cac gia tri >= 0 va <= 2^32-1.")
	def test_3(self) :
		self.assertEqual(detect_triangle(float(2**32),32.1,3.1), "Nhap cac gia tri >= 0 va <= 2^32-1.")
	def test_4(self) :
		self.assertEqual(detect_triangle(float(2**32-1),43.3,34.1), "Day khong phai tam giac")
	def test_5(self) :
		self.assertEqual(detect_triangle(float(2**32-2),454.2,3132.3), "Day khong phai tam giac")
	def test_6(self) :
		self.assertEqual(detect_triangle(4.0,1.0,2.0), "Day khong phai tam giac")
	def test_7(self) :
		self.assertEqual(detect_triangle(3.0,3.0,3.0), "Day la tam giac deu")
	def test_8(self) :
		self.assertEqual(detect_triangle(2.0,2.0,math.sqrt(8.0)), "Day la tam giac vuong can")
	def test_9(self) :
		self.assertEqual(detect_triangle(6.0,9.0,6.0), "Day la tam giac can")
	def test_10(self) :
		self.assertEqual(detect_triangle(5.0,3.0,4.0), "Day la tam giac vuong")
	def test_11(self) :
		self.assertEqual(detect_triangle(3.0,7.0,5.0), "Day la tam giac thuong")
	def test_12(self) :
		self.assertEqual(detect_triangle(10.0,100.0,100.0), "Day la tam giac can")
	def test_13(self) :
		self.assertEqual(detect_triangle(float(2**32-1),5.0,float(2**32-1)), "Day la tam giac can")
	def test_14(self) :
		self.assertEqual(detect_triangle(4,7.8,2.3), "Nhap sai kieu du lieu.")
	def test_15(self) :
		self.assertEqual(detect_triangle(5.4, 43.2, 5.5), "Day khong phai tam giac")
	def test_16(self) :
		self.assertEqual(detect_triangle(25.0, 10.0, 25.0), "Day la tam giac can")

if __name__ == '__main__':
    unittest.main()
