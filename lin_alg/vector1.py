import math

class Vector:
	def __init__(self, coordinates):
		#if not self._coordinates:
		#	raise ValueError('Provide coordinates')
		self._coordinates = tuple(coordinates)
		self.dimension = len(coordinates)

	@property
	def coordinates(self):
		return tuple([math.ceil(x * 1000) / 1000 for x in self._coordinates])
	
	def __str__(self):
		return 'Vector {}'.format(self.coordinates)

	def __eq__(self, v):
		return self.coordinates == v.coordinates

	def __add__(self, other):
		if (self.dimension != other.dimension):
			raise ValueError('The dimensions doesnt match')

		return Vector([x[0] + x[1] for x in zip(self.coordinates, other.coordinates)])

	def __mul__(self, v):
		if (isinstance(v, Vector)):
			return self.dot_prod(v)
		else:
			return Vector([x * v for x in self.coordinates])

	def __sub__(self, other):
		return self + other * -1

	def __truediv__(self, v):
		return Vector([x / v if x != 0 else 0 for x in self.coordinates ])

	def magn(self):
		return math.sqrt(sum(map(lambda x: x**2, self.coordinates)))

	def norm(self):
		v = self / self.magn()
		return v

	def dot_prod(self, other):
		return sum([x[0] * x[1] for x in zip(self.coordinates, other.coordinates)])

	def angle_between(self, other):
		cos_a = (self * other) / (self.magn() * other.magn())
		return math.acos( cos_a )

	def is_parr(self, other):
		return self.norm() == other.norm() or self.norm() == other.other_dir().norm()

	def is_ort(self, other):
		return self * other == 0

	def other_dir(self):
		return Vector([-1 * x for x in self.coordinates])


	def cross_product(self, other):
		if (self.dimension != 3 or other.dimension != 3):
			raise ValueError('Only 3 dimensional vectors have cross product')

		a = self.coordinates[1] * other.coordinates[2]  - self.coordinates[2] * other.coordinates[1]
		b = -1*(self.coordinates[0] * other.coordinates[2]  - self.coordinates[2] * other.coordinates[0])
		c = self.coordinates[0] * other.coordinates[1]  - self.coordinates[1] * other.coordinates[0]
		return Vector((a, b, c))


a = Vector((10,11,3))
b = Vector((7, 4,44))

c = a.cross_product(b)

print (a * c)
print (b * c)

print (a.magn(), b.magn(), c.magn())
