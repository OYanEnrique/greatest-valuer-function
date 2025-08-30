# Number function

print('------Greater Value Function------')
def greater(* numbers):
	for num in numbers:
		print(f'Number informed: {num} ')
	print(f'{len(numbers)} numbers were reported in total')
	greater_number = 0
	if len(numbers) > 0:
		greater_value = max(numbers)
		print(f'The greater value informed was {greater_value}')
			
greater(1,2,9,3,10)