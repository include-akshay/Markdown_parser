import regex as re

def reg(result):
    #heading h1
    regex_h1 = r"^(#\s)(.*)"
    subst_h1 = "<h1>\\2</h1>"
  
    #heading h2
    regex_h2 = r"^(##\s)(.*)"
    subst_h2 = "<h2>\\2</h2>"

    #heading h3
    regex_h3 = r"^(###\s)(.*)"
    subst_h3 = "<h3>\\2</h3>"

    #bold and itlatics
    regex_ib = r"(\*\*\*)(\b)([^\*]*)(\b)(\*\*\*)"
    subst_ib = "<em><b>\\3</b></em>"

    #bold
    regex_b = r"(\*\*)(\b)([^\*]*)(\b)(\*\*)"
    subst_b = "<b>\\3</b>"

    #italics
    regex_i = r"(\*)(\b)([^\*]*)(\b)(\*)"
    subst_i = "<em>\\3</em>"

    #unordered list 
    regex_ul = r"(^(\W{1})(\s)(.*)(?:$)?)+"
    subst_ul = "<ul>\\n\\4</ul>\\n"
   
    

    result = re.sub(regex_h1, subst_h1, result, 0, re.MULTILINE)
    result = re.sub(regex_h2, subst_h2, result, 0, re.MULTILINE)
    result = re.sub(regex_h3, subst_h3, result, 0, re.MULTILINE)
    result = re.sub(regex_ib, subst_ib, result, 0, re.MULTILINE)
    result = re.sub(regex_b, subst_b, result, 0, re.MULTILINE)
    result = re.sub(regex_i, subst_i, result, 0, re.MULTILINE)
    result = re.sub(regex_ul, subst_ul, result, 0, re.MULTILINE)

    
    return result