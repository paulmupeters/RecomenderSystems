import numpy as np 

class MaFactor:

	original_M = None
	k = num_iter = lr = regu = None
	left_matrix = right_matrix = None


	def __init__(self, _original_M, num_users, num_items, _k = 10, _num_iter = 75, _lr = 0.005, _regu = 0.05):

		# use the original matrix instead of creating a larger new one to save memoreies
		self.original_M = _original_M



		self.k = _k
		self.num_iter = _num_iter
		self.lr = _lr
		self.regu = _regu


		self.left_matrix = abs(np.random.rand(num_users, self.k))
		self.right_matrix = abs(np.random.rand(self.k, num_items))



	def iteration(self):

		for i in range(self.num_iter):
			for row in self.original_M:

				error = row[2] - self.left_matrix[row[0]-1,:].dot(self.right_matrix[:,row[1]-1])

				# update entries
				for j in range(self.k):
					left_entry = self.left_matrix[row[0]-1,j]
					self.left_matrix[row[0]-1,j] = (1 - self.lr * self.regu) * left_entry + 2 * error * self.lr * self.right_matrix[j,row[1]-1]
					self.right_matrix[j,row[1]-1] = (1 - self.lr * self.regu) * self.right_matrix[j,row[1]-1] + 2 * error * self.lr * left_entry


	def predict(self, user_id, iterm_id):

		return self.left_matrix[user_id-1,:].dot(self.right_matrix[:,iterm_id-1])














