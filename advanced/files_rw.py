def write_to_file(file_name, data=None):

    with open(file_name, 'a+') as file:
        print('Storage unit created successfully...')

        if not data:
            print('\nNo data to inscribe !\n')
        else:
            print('\nInscribing preservation data...')
            file.write(f'{data}')
            file.seek(0)
            print(file.read())
            print('\nData inscription complete. Storage unit sealed.')

    print(f"Archive '{file_name}' ready for long-term preservation.")


def main():
    file_name = 'test.txt'
    data = 'New quantum algorithm discovered'

    print(f'\nInitializing new storage unit: {file_name}')
    write_to_file(file_name, data)


if __name__ == "__main__":
    main()
