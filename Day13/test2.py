word_per_page = 0
pages = int(input("Enter number of pages:     "))
word_per_page = int(input("Enter number of words per page:    ")) #there was double assignment sign ("=")
total_words = pages*word_per_page
print(total_words)