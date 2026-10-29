from validator_collection import validators, checkers, errors

def main():
    print(check(input("Email: ")))

def check(s):
    try:
        email_address = validators.email(s)
        if checkers.is_email(s): return 'Valid'
        else: return 'Invalid'
    except (errors.InvalidEmailError, errors.EmptyValueError):
        return 'Invalid'

if __name__ == '__main__':
    main()