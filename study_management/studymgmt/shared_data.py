# Column names or field names will be used for templates and in study info view
field_names = ['STUDY NAME','STUDY PHASE', 'SPONSER NAME','STUDY DESCRIPTION']

# Example for the need of values_as_list
# if there is a list_dic = [{'id':1},{'id':2},{'id':3}]
# result of values_as_list() = [1,2,3]
def values_as_list(list_dict,key):
    l = []
    for d in list_dict:
        l.append(d[key])
    return l


