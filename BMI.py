#Body Mass index Calculator

weight = float(input('Enter your weight in kg:\n'))
height = float(input('Enter your height in m:\n'))
BMI = float(weight/(height*height))
print(f'Your Body Mass Index is: {BMI:.2f}')

if BMI <= 18.5:
	print(f'Your Body Mass Index of {BMI:.2f} indicates that you are underweight.')
	
elif BMI >= 18.5 and BMI <= 24.9:
    print(f'Your Body Mass Index of {BMI:.2f} indicates that you are of normal weight.')
    
elif BMI >= 25.0 and BMI <= 29.9:
	print(f'Your Body Mass Index of {BMI:.2f} indicates that you are overweight.')
	
else:
	print(f'Your Body Mass Index of {BMI:.2f} indicates that you are obese.')

