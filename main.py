def lambda_handler(event=None, context=None):
    print('Hello world')
    return 'Hello world', 200

if __name__ == '__main__':
    print(lambda_handler())
