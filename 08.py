phone_book = {}
test_cases = int( input() )
limit = 10 ** 5
if test_cases >= 1 and test_cases <= limit:
    for i in range( 0, test_cases ):
        info_person_arr = input().rstrip().split()
        name = info_person_arr[0].lower()
        phone = info_person_arr[1]
        phone_book[ name ] = phone
    while True:
        try: 
            search_name = input().lower()
            if len( search_name ) <= 0:
                break
            if search_name in phone_book:
                text_to_show = search_name + "=" + phone_book[search_name]
                print( text_to_show )
            else:
                print( "Not found" )
        except (EOFError):
            break
