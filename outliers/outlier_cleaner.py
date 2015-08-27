#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """

    errors = predictions - net_worths
    errors = errors.tolist()
    ages = ages.tolist()
    net_worths = net_worths.tolist()
    l = len(errors)
    p = 0.9
    n = l
    while (n > p*l):
        m = max(errors)
        i = errors.index(m)
        errors.pop(i)
        ages.pop(i)
        net_worths.pop(i)
        n = n-1

    age = []
    for a in ages:
        age.append(a[0])
    net_worth = []
    for nw in net_worths:
        net_worth.append(nw[0])
    error = []
    for e in errors:
        error.append(e[0])

    cleaned_data = zip(tuple(age), tuple(net_worth), tuple(error))
    return cleaned_data

