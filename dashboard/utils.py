# Funções utilitárias para processamento de dados

def calculate_moving_average(data, window=7):
    """Calcula média móvel para suavizar dados"""
    if len(data) < window:
        return data
    
    moving_avg = []
    for i in range(len(data)):
        if i < window:
            moving_avg.append(sum(data[:i+1]) / (i+1))
        else:
            moving_avg.append(sum(data[i-window+1:i+1]) / window)
    
    return moving_avg

def normalize_by_population(count, population):
    """Normaliza dados pela população"""
    if population and population > 0:
        return (count / population) * 1000000  # por milhão de habitantes
    return 0