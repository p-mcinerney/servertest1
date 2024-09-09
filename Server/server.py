import streamlit as st

st.write("Private website")

#the password for Patrick
pwinput = st.text_input("Key: ")

if pwinput == "010607":
    st.write("(Decrypted)")
    st.write("Hi patrick, welcome to your online planner!")
    plan = st.text_input("Add a plan: ")
    with open('patrick.txt', 'a+') as file:
        file.write(plan)
        file.write("\n")
        file_content = file.read()
    st.write(f"{file_content}")
elif pwinput == "horseclown":
    #st.write("Working.")
    st.write("(Decyrpted)")
    st.write("Secret Blog")
    blogpost = st.text_input("Add a post here: ")
    with open('Secret_blog_archive.txt', 'a+') as blog:
        blog.write(f"{blogpost}")
        blog.write("\n")
else:
    st.write("Encrypted.")
