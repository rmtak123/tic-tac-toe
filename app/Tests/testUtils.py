"""
when we receive a parameter from a feature file
we must not consider the outer ' ' 
"""
def parse_parameter_from_feature(parameter):
    return parameter[1:-1]