#import cryptography
from cryptography.fernet import Fernet # for encryption and decryption
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
import base64
import sys
import os
# if you get an error on the above line, you might need to run 
# pip install INSERT_LIBRARY_NAME or install the library another way.
from types import SimpleNamespace

'''config = SimpleNamespace(
    input_filename = "/windows_data_encrypted.txt", #include original path of text file's parent directory
    
)'''

#Below are some TODO comments.


def generate_mq_key(key_string):
    if(len(key_string)<32):
       key_string = str(key_string + "abcdefghijklmnopqrstuvwxyz012345")
    key_string = key_string[0:32]
    key_string_bytes = str(key_string).encode("ascii")
    key = base64.urlsafe_b64encode(key_string_bytes)
    return key

def encrypt_file(input_filename, output_filename, key = b"fdhsrtsyrjsjyggbbg"):
    secrect_key=generate_mq_key(key)
    engine = Fernet(secrect_key)



    with open(os.path.join(config.input_filename),"rb") as original_file:
        read_original_file = original_file.read() 
        output_filename = engine.encrypt(read_original_file)
        
        
    #TODO: use fernet, open the file input_filename
    #read and encrypt the contents of the file
    #store the encrypted contents in another file who's name
    #is stored in output_filename
    #https://cryptography.io/en/latest/fernet/
    return None


def decrypt_file(input_filename, output_filename, key ):
    secrect_key=generate_mq_key(key)
    engine = Fernet(secrect_key)
    
    #reading file
    #with open("input_filename","rb") as encrypted_file:
    with open(input_filename,"rb") as encrypted_file:
        encrypted = encrypted_file.read()
        #decrypting file
        output = engine.decrypt(encrypted)
    #opening decrypt file is there ....
        with open(output_filename,'wb') as output:
            output.write(output_filename)
        
        
    
    
    #: use fernet, open the file input_filename
    #read and decrypt the contents of the file
    #store the decrypted contents in another file who's name
    #is stored in output_filename
    #https://cryptography.io/en/latest/fernet/
    return None


def generate_hash(input_filename, output_filename, key = "fdhsrtsyrjsjyggbbg"):
    
    digest = hashes.Hash(hashes.SHA256())
    input_filename = "mypassword8099"
    
    #calling key from the function 
    key = b"fdhsrtsyrjsjyggbbg"
    secrect_key=generate_mq_key(key)
    engine = Fernet(secrect_key)
    
    digest.update(input_filename)
    output_filename=digest.finalize()
    
    
    
    
    
    #TODO: use the hazmat section of cryptography to generate a hash.
    #take the contents from the file named input_filename
    #hash the contents, 
    #store the decrypted contents in another file who's name
    #is stored in output_filename
    #https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/
    return None 


###############################################################################

def task_1(student_id,input_file_name , output_file_name):
    # remember, use the command console to run the argument
    # python   crypto_a1_activity.py   40000000  task1   encrypteddata.txt   decrypteddata.txt
    
    key = generate_mq_key(str(student_id))
    decrypt_file(input_file_name,output_file_name,key)
    
    #decrypt_file(input_file_name, output_file_name, key)
    #TODO: call the functions needed for task 1 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 1"
    print("Completed Task 1")

def task_2(student_id, input_file_name , output_file_name):
    # remember, use the command console to run the argument
    # python   crypto_a1_activity.py   YOUR_STUDENT_NUMBER  task2   datafile.encrypted   datafile_enc_decr
    key = generate_mq_key(str(student_id))
    #TODO: call the functions needed for task 2 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 2"
    print("Task 2 was called... need to update code")

def task_3(student_id, input_file_name , output_file_name):
    #TODO: call the functions needed for task 3 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 3"
    print("Task 3 was called... need to update code")

def task_4(student_id, input_file_name , output_file_name):
    #TODO: call the functions needed for task 4 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 4"
    print("Task 4 was called... need to update code")

def task_5(student_id, input_file_name , output_file_name):
    #TODO: call the functions needed for task 5 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 5"
    print("Task 5 was called... need to update code")

###############################################################################
#You don't need to edit anything below here.
def main():
    if len(sys.argv) < 5:
        print("not enough arguments have been entered. Use the following format from the IDE console:")
        print("\npython crypto_a1_activity.py 41234567 task1 inputFileName outputFileName\n\nor")
        print("\npython3 crypto_a1_activity.py 41234567 task1 inputFileName outputFileName\n\n")
    else:
        student_id = sys.argv[1] # student ID
        encryption_actitiy = sys.argv[2] # encrypt, decrypt, or hash
        input_file_name = sys.argv[3]
        output_file_name = sys.argv[4]
        if(encryption_actitiy == "task1"):
            task_1(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task2"):
            task_2(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task3"):
            task_3(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task4"):
            task_4(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task5"):
            task_5(student_id,input_file_name , output_file_name)
        else:
            print("couldn't work out what to do.")
            print("Please use the following format when running the file:\n")
            print("python   crypto_a1_activity.py   STUDENT_NUMBER  ACTIVITY   INPUT_FILENAME   OUTPUT_FILENAME")
            print("\nACTIVITY can be any of the following words:")
            print("task1")
            print("task2")
            print("task3")
            print("task4")
            print("task5")



if __name__ == "__main__":
    main()