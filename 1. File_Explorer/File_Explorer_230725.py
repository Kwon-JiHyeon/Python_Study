import glob

def FileCollection(L_name, file_types):

    #s_path = str(__import__(L_name)).split('\'')[3][:-11]
    s_path = '/'.join(str(__import__('pandas')).split()[-1].strip('\'').split('/')[:-1]) + '/'

    dummy_arg = s_path + '**\\\*.'+file_types
    print(dummy_arg)
    file_lists = glob.glob(dummy_arg, recursive=True)
    return (file_lists, s_path)

def GetFileSentence(file_list, search_sentences, s_path):
    file_dict = {}
    for filename in file_list:
        sentence_list = []
        with open(filename, 'r', errors='ignore') as f:
            lines = f.readlines()
        for item in lines:
            if search_sentences in item:
                sentence_list.append(item)
        if sentence_list :
            file_dict[filename[len(s_path):]] = sentence_list
    return(file_dict)

def print_result(fdr):
    for i in fdr:
        print(i)
        print('==='*10)
        for j in fdr[i]:
            print('-   ', j.strip())
        print()
