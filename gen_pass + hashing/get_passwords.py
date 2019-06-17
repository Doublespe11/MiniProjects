import passlib

if __name__=="__main__":

    passwords = passlib.get_passwords(file+".txt")
    facebook = passwords[0]
    gmail = passwords[1]
    github = passwords[2]
    email = "xyz@gmail.com"

    try:
        file=input("Enter file name:  ")
    except:
        "WRONG Name file!!"
        quit()

    cmd = input("change password(change) or open browsers(open): ")
    if cmd=="change":
        passlib.data_gen(file + ".txt")

    if cmd=="open":
        facebook(email, facebook)
        gmail(email, gmail)
        github(email, github)
