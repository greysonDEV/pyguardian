def allinstance(collection, valid_type):
		"""
		'allinstance' is a helper method that checks if every item contained 
		within a collection are of a specified type.
		"""
		return all(isinstance(item, valid_type) for item in collection)