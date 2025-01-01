# Copy over your a1_partc.py file here

#    Main Author(s): Shayan Ramezanzadeh, Ashkan Rahimpour Harris
#    Main Reviewer(s): Babak Ghafourigivi

class Stack:

	def __init__(self, cap=10):
		self._data = [None] * cap
		self._size = 0
		# cap is an integer showing The initial capacity of the 
		# stack with default value of 10
		self._cap = cap 

	def capacity(self): # Returns the current capacity
		return self._cap

	def push(self, data): # Adds element to top of the stack
		if self._size == self._cap: # resize
			new_data = [None] * (2 * self._cap) # Value to be added to stack
			for i in range(self._size):
				new_data[i] = self._data[i]
			self._data = new_data
			self._cap *= 2
		self._data[self._size] = data
		self._size += 1

	def pop(self): # Removes the top element
		if self._size == 0:
			raise IndexError("pop() used on empty stack")
		value = self._data[self._size - 1]
		self._size -= 1
		return value # Removed element

	def get_top(self): # Returns the top element
		if self._size == 0:
			return None
		return self._data[self._size - 1]

	def is_empty(self): # Checks if the stack is empty
		return self._size == 0

	def __len__(self): # Returns the current number of elements
		return self._size


class Queue:
	def __init__(self, cap=10):
		self._data = [None] * cap
		self._front = 0
		self._size = 0
		self._cap = cap # The initial capacity of the queue with default value of 10

	def capacity(self): # Returns the capacity of the queue
		return self._cap 

	def enqueue(self, data):# Adds an element to the back
		if self._size == self._cap: # resize
			new_data = [None] * (2 * self._cap) #value to be added
			for i in range(self._size):
				new_data[i] = self._data[(self._front + i) % self._cap]
			self._data = new_data
			self._front = 0  # Reset front 
			self._cap *= 2
		idx = (self._front + self._size) % self._cap
		self._data[idx] = data
		self._size += 1

	def dequeue(self): # Removes and returns the front element
		if self._size == 0:
			raise IndexError("dequeue() used on empty queue")
		value = self._data[self._front]
		self._front = (self._front + 1) % self._cap
		self._size -= 1
		return value # value that was removed from the front 

	def get_front(self): # Returns the front element None if empty
		if self._size == 0:
			return None
		return self._data[self._front] # The value at the front

	def is_empty(self): # Checks if queue is empty
		return self._size == 0

	def __len__(self): # Returns the current number of elements
		return self._size



class Deque:

	def __init__(self, cap=10):
		self._data = [None] * cap
		self._front = 0
		self._size = 0
		self._cap = cap #The initial capacity of the deque default 10

	def capacity(self): # Returns the current capacity
		return self._cap

	def push_front(self, data): # Adds an element to front
		if self._size == self._cap: # Resize
			new_data = [None] * (2 * self._cap) # The value to be added
			for i in range(self._size):
				new_data[i] = self._data[(self._front + i) % self._cap]
			self._data = new_data
			self._front = 0  # Reset front 
			self._cap *= 2
		self._front = (self._front - 1) % self._cap
		self._data[self._front] = data
		self._size += 1


	def push_back(self, data): # Adds an element to back
		if self._size == self._cap: # resize
			new_data = [None] * (2 * self._cap) # The value to be added
			for i in range(self._size):
				new_data[i] = self._data[(self._front + i) % self._cap]
			self._data = new_data
			self._front = 0  # Reset front
			self._cap *= 2
		idx = (self._front + self._size) % self._cap
		self._data[idx] = data
		self._size += 1

	def pop_front(self): # Removes and returns the front element
		if self._size == 0:
			raise IndexError("pop_front() used on empty deque")
		value = self._data[self._front]
		self._front = (self._front + 1) % self._cap
		self._size -= 1
		return value # removed value


	def pop_back(self): # Removes and returns the back element
		if self._size == 0:
			raise IndexError("pop_back() used on empty deque")
		idx = (self._front + self._size - 1) % self._cap
		value = self._data[idx]
		self._size -= 1
		return value # removed value

	def get_front(self): # Returns the front element
		if self._size == 0:
			return None
		return self._data[self._front]

	def get_back(self): # Returns the back element
		if self._size == 0:
			return None
		idx = (self._front + self._size - 1) % self._cap
		return self._data[idx]

	def is_empty(self): # Checks if deque is empty
		return self._size == 0

	def __len__(self): # Returns the current number of elements
		return self._size

	def __getitem__(self, k): # k: The index of the element
		if k < 0 or k >= self._size:
			raise IndexError("Index out of range")
		idx = (self._front + k) % self._cap
		return self._data[idx] # element located at index 'k'

# reviewed and all tests paas