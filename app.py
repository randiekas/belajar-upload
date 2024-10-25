#step 1: import semua package yang dibutuhkan
import streamlit as st
import boto3

#step 2: membuat general variable
endpoint_url='https://s3.ap-southeast-1.wasabisys.com'
bucket_name = 'bpksmak1-demo'

#step 3: membuat varible untuk konek ke s3
s3 = boto3.client(
    's3',
    endpoint_url=endpoint_url,
    aws_access_key_id='5FJG96G643BUOU3REVBW',
    aws_secret_access_key='MQZF7FCjimdS4oqyq8AbLmSVNjWAgAa88eb8yT5C',
)

#step 4: membuat fungsi untuk upload ke s3
def upload_file_to_s3(file, bucket_name, object_name, content_type):
    s3.upload_fileobj(file, bucket_name, object_name, ExtraArgs={'ACL': 'public-read', 'ContentType': content_type})
    st.success(f"File {endpoint_url}/{bucket_name}/{object_name} uploaded successfully to {bucket_name}")

 
#step 5: membuat judul dan subjudul menggunakan streamlit
st.title("My First App")
st.text("Upload file to s3 from kelomok xyz")

#step 6: membuat input type file 
uploaded_file = st.file_uploader("Choose a file")


#step 7: jika file dipilih, maka panggil fungsi upload file
if uploaded_file is not None:
    object_name = "kelompok1/"+uploaded_file.name  # You can customize the object name here
    content_type = uploaded_file.type
    upload_file_to_s3(uploaded_file, bucket_name, object_name, content_type)
