# from .cli import main  # pragma: no cover

def run_this(no=50):
    lst = []
    for item in range(no):
        lst.append(item*2)
    del lst
    

# if __name__ == "__main__":  # pragma: no cover
#     main()