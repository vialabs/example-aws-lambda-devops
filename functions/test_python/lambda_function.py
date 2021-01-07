
def main():

    print('Hello World 2')

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'body': 'Sucesso!'
    }

if __name__ == "__main__":
    
    main()
