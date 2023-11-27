import sys

print('test')
for i in sys.argv:
    print(i)


print('\n\nThe PYTHONPATH is', sys.path, '\n')


print(dir(sys))