#Write 2 unit tests to test:
#1. calculate_return
#2. avg_return


from Calculate_return import average_return
from Stock import stock
import unittest

class Testavgreturn (unittest.testcase):
    def test_avg_return(self):
        s1=stock("GOOGL",0.6)
        s2=stock("TSLA",0.15)
        s3=stock("BLK",0.20)
        s4=stock("BK",0.1)
Stock=[s1,s2,s3,s4]
expected =0.35
actual=round(average_return(stock),2)
self.assertEqual(expected, actual)
