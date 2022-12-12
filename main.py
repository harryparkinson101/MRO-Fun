class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

# Depth first search algorithm is responsible for the MRO order

  
print(M.__mro__)