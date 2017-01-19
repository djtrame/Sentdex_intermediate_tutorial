#args are a list
#kwargs are like a dictionary
#keyword arguments

blog_1 = 'I am so awesome!'
blog_2 = 'Cars are cool'
blog_3 = 'Dunder Mifflin fan club'

site_title = 'My Blog Title'

# def blog_posts(title, *args):
#     print(title)
#     for post in args:
#         print(post)

def blog_posts(title, *args, **kwargs):
    print(title)
    for arg in args:
        print(arg)
    for p_title, post in kwargs.items():
        print(p_title, post)

#throw in unlimited # of arguments
# blog_posts(site_title, blog_1, blog_2, blog_3)
blog_posts(site_title, '1', '2', '3',
           blog_1 = 'I am so awesome!',
            blog_2 = 'Cars are cool',
            blog_3 = 'Dunder Mifflin fan club')

#######################

def graph_operation(x, y):
    print('function that graphs {} and {}'.format(str(x), str(y)))

x1 = [1,2,3]
y1 = [2,3,1]

graph_me = [x1, y1]

#passing a list
graph_operation(*graph_me)