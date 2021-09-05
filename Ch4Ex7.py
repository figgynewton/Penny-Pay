Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> salary = 0.01
>>> total = 0.01
>>> time = 0.0
>>> days = int(input(" Enter the amount of days: "))
 Enter the amount of days: 27
>>> for days in range(days):
	print(days,"\t\t$",format(total, ".2f"), sep = "")
	total = salary * 2
	salary = total

	
0		$0.01
1		$0.02
2		$0.04
3		$0.08
4		$0.16
5		$0.32
6		$0.64
7		$1.28
8		$2.56
9		$5.12
10		$10.24
11		$20.48
12		$40.96
13		$81.92
14		$163.84
15		$327.68
16		$655.36
17		$1310.72
18		$2621.44
19		$5242.88
20		$10485.76
21		$20971.52
22		$41943.04
23		$83886.08
24		$167772.16
25		$335544.32
26		$671088.64
>>> 
