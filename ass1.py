class MathTools:
    total_calls = 0
    
    def derivative(self, func, x, h=1e-10):
        MathTools.total_calls += 1
        return (func(x + h) - func(x)) / h
    
    def gradient(self, func, point, h=1e-10):
        MathTools.total_calls += 1
        grad = []
        for i in range(len(point)):
            original_value = point[i]
            point[i] = original_value + h
            f_plus_h = func(point)
            point[i] = original_value - h
            f_minus_h = func(point)
            grad.append((f_plus_h - f_minus_h) / (2 * h))
            point[i] = original_value
        return grad