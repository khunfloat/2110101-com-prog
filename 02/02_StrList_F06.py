def add_vector(u, v):
    u = [float(i) for i in u]
    v = [float(i) for i in v]

    return [u[i]+v[i] for i in range(3)]

exec(input())