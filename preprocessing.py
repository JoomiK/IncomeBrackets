
# Preprocessing functions
def label_map(y):    
    """Encodes labels"""

    # For incomes above 50k
    if y == 50000:
        return 1
    elif y == '50000+.':
        return 1
    elif y == ' 50000+.':
        return 1

    # For incomes below 50k
    elif y == -50000:
        return 0
    elif y == '-50000':
        return 0

def isNan(num):
    """Test for Nan"""
    return num != num

def add_MDcol(df, col_list):
    """Add column for missing categorical data"""
    for col in col_list:
        df[col+'_missing'] = df[col].apply(isNan)