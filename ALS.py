import numpy as np 


class ALS:

	regu = num_iter = k = None

	# the complete matrix
	R = None

	# the fatorization matrix U and M
	U = M = None

	# avg_rating_movies is a vector with average rating for all movies
	def __init__(self, original_M, avg_rating_movies, num_users, num_items, _k = 10, _num_iter = 10, _regu = 0.05):

		# create a matrix with rows being user and columns being movies
		self.R = np.zeros((num_users, num_items))
		for row in original_M:
			
			self.R[row[0]-1,row[1]-1] = row[2]

		self.regu = _regu
		self.num_iter = _num_iter
		self.k = _k


		self.U = np.zeros((self.k, num_users))
		self.M = abs(np.random.randn(self.k, num_items)/2)
		self.M[0,:] = np.array(avg_rating_movies)



	def iteration(self):
		for itr in range(self.num_iter):
			# fix M, update U
			for i in range(self.U.shape[1]):

				# find the sub matrix sub_M_j of M where the j_th columns of R that the i_th entries are not 0
				js = np.where(self.R[i,:] != 0)[0]
				sub_M_j = self.M[:,js]

				# number of movies this user i rated
				num_i = len(js)

				# if paticular user is not included in test data, skip the training
				if (num_i != 0):
	 				# sub vector of R of only the i_th row and js entries
					sub_R = self.R[i,js]



					self.U[:,i] = np.matmul(np.linalg.inv(np.matmul(sub_M_j,sub_M_j.T) + self.regu * num_i * np.identity(self.k)) ,np.matmul(sub_M_j, sub_R))


			# fix U, update M
			for j in range(self.M.shape[1]):

				i_s = np.where(self.R[:,j] != 0)[0]
				sub_U_j = self.U[:, i_s]

				num_j = len(i_s)

				if (num_j != 0):

					sub_R = self.R[i_s, j]


					self.M[:,j] = np.matmul(np.linalg.inv(np.matmul(sub_U_j, sub_U_j.T) + self.regu * num_j * np.identity(self.k)), np.matmul(sub_U_j, sub_R))



	def predict(self, user_id, iterm_id):
		return (np.dot(self.U[:,user_id - 1], self.M[:,iterm_id - 1]))






