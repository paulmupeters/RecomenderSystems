import numpy as np 
from aignment1DataMining import itemAverage, userAverage

def leastSquare (matrix, i_matrix, u_matrix):
	true_ratings = matrix[:,2]
	item_avg_vector = []

	rows = matrix.shape[0]


	# reform item matrix with the shape of "matrix"
	for i in range(0,rows):

		item_avg_vector.append(i_matrix[matrix[i,1]-1])


	# reform user matrix with the shape of "matrix"
	user_avg_vector = []
	for i in range(0,u_matrix.shape[0]):

		user_avg_vector.extend([u_matrix[i]]*len(np.where(matrix[:,0] == i+1)[0]))

	# calculate least square error


	lin_reg_matrix = np.vstack([item_avg_vector, user_avg_vector, np.ones(rows)]).T 
	result = np.linalg.lstsq(lin_reg_matrix,true_ratings)

	#print least square error
	print('least square error is' , result[1])

	# return a, b, c of ax + by + c
	return result[0]

#predict a rating with values
def predictLR (iterm_avg, user_avg, abc):
	# three factors of linear regression
	a, b, c = abc
	return (a*iterm_avg + b*user_avg + c)

# predict ratings with a test matrix
def predictLR_M(matrix, i_matrix, u_matrix, abc):

	rows = matrix.shape[0]

def nothing()
	return 1

	# calculate a matrix with predicted values
	predicted = []
	for i in range(0, rows):
		predicted.append(predictLR(i_matrix[matrix[i,1]-1], u_matrix[matrix[i,0]-1], abc))

	return np.array(predicted)



