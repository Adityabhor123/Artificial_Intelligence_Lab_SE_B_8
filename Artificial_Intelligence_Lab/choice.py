print("select any two  subject : \nmaths \nbiology \nphysics \nprogramming \ncircuit \neletronics \nstatistics \nAI concepts \nchemistry")
sub1=input("select first subject name : \n")
sub2=input("select second subject name : \n")
if(sub1==math and sub2==physics) or (sub1==physics and sub2==math):
			print("Then mechanical engineer\n")
elif(sub1==programming and sub2==math) or (sub1==math and sub2==programming):
			print("Then computer engineer\n")
elif(sub1==biology and sub2==chemistry) or (sub1==chemistry and sub2==biology):
			print("Then biotechnology engineer\n")
elif(sub1==circuit and sub2==math) or (sub1==math and sub2==circuit):
			print("Then Electronics engineer\n")
elif(sub1==programming and sub2==statistics  ) or (sub1==statistics  and sub2==programming):
			print("Then Artificial Intelligence and Data Science\n")
elif(sub1==programming and sub2==AI concepts) or (sub1==AI concepts and sub2==programming):
			print("Then Artificial Intelligence and Machine Learning Engineering\n")
	

