# from .cli import main  # pragma: no cover

def run_this(no=10000):
    lst = []
    for item in no:
        lst.append(no*2)
    del lst
    

# if __name__ == "__main__":  # pragma: no cover
#     main()