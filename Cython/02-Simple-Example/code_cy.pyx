import math

cpdef list generate_waves(int length):
    cdef list waves = []
    cdef int i
    for i in range(length):
        waves.append(math.sin(i))
    return waves