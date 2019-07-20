from cx.common.pricedb import parse_line, build_db

with open('./price.db') as input_file:
    db = build_db(map(parse_line, input_file))
