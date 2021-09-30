def slices(series, largo):
    if (series and largo <= len(series) and largo > 0):
        return [series[offset:offset+largo] for offset in range(len(series)-largo+1)]
    else:
        raise ValueError('Error')