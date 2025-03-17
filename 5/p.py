import logging

# import collections

logging.basicConfig(level=logging.DEBUG)


def read_data(path_file: str):
    with open(path_file) as f:
        return [line.strip() for line in f]


def extract_pageRules_and_pageProduces(data: list[str]):
    delimiter_idx = data.index("")
    page_rules = data[:delimiter_idx]
    pages_update_batch = data[delimiter_idx + 1 :]
    page_rules_dict = dict()
    for rule in page_rules:
        rule_elements = rule.split("|")
        if rule_elements[0] in page_rules_dict:
            page_rules_dict[rule_elements[0]].append(rule_elements[1])
        else:
            page_rules_dict[rule_elements[0]] = [rule_elements[1]]
    return page_rules_dict, pages_update_batch

def get_index_occur(value: int, array: list[int]) -> list[int]:
    return [val for val in array if val == value][0]

def check_rules_violation(
    page_rules_dict: dict[str, str], pages_produced: str
) -> bool:
    list_pages_produced = pages_produced.split(",")
    for i, page in enumerate(list_pages_produced):
        not_allowed_pages = page_rules_dict.get(str(page))
        if i == 0:
            pass
        # elif not_allowed_pages != None:
            # if page in list_pages_produced[:i]:
            #     idx = get_index_occur(page, list_pages_produced[:i])
            #     if len(list_pages_produced[:idx]) > 0:
            #         if len(set(not_allowed_pages) & set(list_pages_produced[:idx])) > 0: return False
                    
        elif not_allowed_pages != None and (len(set(not_allowed_pages) & set(list_pages_produced[:i])) > 0):
            return False
    return True


if __name__ == "__main__":
    dico, list_string = extract_pageRules_and_pageProduces(
        read_data("data.txt")
    )
    #logging.info(list_string)
    count = 0
    for string in list_string:
        logging.info(string)
        res = check_rules_violation(dico, string)
        if res:
            tab = string.split(",")
            logging.info(tab)
            idx = len(tab) // 2
            logging.info(idx)
            count += int(tab[idx])
    logging.info(count)
