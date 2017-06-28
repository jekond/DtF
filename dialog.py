def format_text(non_form_text):
    text_list = []
    form_text = ['']
    start_slice = 0
    stop_slice = '.,!?:- '
    line_range = 30
    now_range = 0
    for i in range(len(non_form_text)):
        if(non_form_text[i] in stop_slice):
            text_list+=[non_form_text[start_slice:i+1]]
            start_slice = i+1
    print(text_list)
    start_slice = 0

    for i in range(len(text_list)):
        if(now_range + len(text_list[i]) > line_range+1):
            start_slice += 1
            form_text += ['']
            now_range = 0
        form_text[start_slice] += text_list[i]
        now_range += len(text_list[i])

    return form_text
