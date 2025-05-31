import json



def to_json(filename,data):

    with open(f'{filename}.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
        if content:
            payments = list(json.loads(content))

            payments.append(data)
        else:
            payments = [data]

    with open(f'{filename}.json','w',encoding='utf-8') as fp:

        json.dump(payments,fp, ensure_ascii=False,indent=4)


    return True

