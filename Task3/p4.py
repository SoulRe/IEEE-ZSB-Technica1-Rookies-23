"""constructing a book made of pages which are lists of size 2
    inside a bigger list (the book) which are numbered in a way
    that the odd numbers are always on the left and the even numbers
    are always on the right zero being included as even here"""
def construct_book(booksize):
    book = []
    for i in range(0, booksize+1, 2):
        book.append([i, i+1])
    return book
    
"""checking for the page by going through the "pages" (lists of 2)
    inside the book and seeing if the page number is in page or not"""
def check_for_page(booksize, page):
    book = construct_book(booksize)
    countstart = countend = 0
    for i in range(len(book)):
        if int(page) in book[i]:
            #starting counter is the distance from the beginning = i
            countstart = i 
            #the ending counter is the distance from the end 
            countend = len(book) - i - 1
            break
    pagecount = min(countstart, countend)
    return pagecount
    
    
def main():
    booksize = int(input("Book size: "))
    page = int(input("Page: "))
    check = check_for_page(booksize, page)
    print(check)
    

main()