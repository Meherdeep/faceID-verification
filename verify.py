from pyDes import *
import streamlit as st
st.title('Verify Your OTP')
st.header("OTP Verification")
f=open("otp.txt", "r")
contents =f.read()
data = str(contents)
k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
#print("Encrypted Key : ", d)
st.write("Encrypted Key : ",d)
#st.text("Enter your secure OTP: ")
check = st.text_input("Enter your secure OTP","0000")
#check = input("Enter your secure OTP: ")
if(str(check)==contents):
	#print("OTP verified, Thank you")
	st.write("OTP Verified, Thank You")
	#print(k.decrypt(d))
	st.write("Decrypted Key : ",k.decrypt(d))

else:
	#print("Incorrect OTP")
	st.write("Incorrect OTP")