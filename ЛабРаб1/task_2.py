# TODO Найдите количество книг, которое можно разместить на дискете

sym_in_str = 25
str_on_page = 50
page_in_book = 100

sym_in_book = sym_in_str * str_on_page * page_in_book

inf_mb = 1.44

inf_kb = inf_mb * 1024
inf_b = inf_kb * 1024

sym_b = inf_b // 4

books = sym_b // sym_in_book

books = int(books)

print("Количество книг, помещающихся на дискету:", books)