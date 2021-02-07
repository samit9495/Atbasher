# Atbasher

Instructions to Run the Atbasher
  1. clone the Project using git clone https://github.com/samit9495/Atbasher.git
  2. Place all the files that you want to encrypt in the root directory of the folder i.e. in the same directory in which atbasher.py files is present.
  3. Use the below command to run the code.
        python atbasher.py -f file1.txt file2.txt file3.txt . . .
     you can encrypt any number of files in one go just provide all the file names in command line seperated by space. As shown in above command.
  4. The code will encrypt N number of files in parellel using multi threads, where N is the number of cpu_count
  5. Files after encryption will be store in a folder named "Encrypted Files".
  
  
  
Instructions to run test cases.
  1. Make sure you have pytest installed in your system. if not, the install it using the below command
        pip install pytest
  2. Run the test cases using the below command.
  
        pytest --file file1.txt file2.txt . . .
     
     provide the actual file names that you want to encrypt in place of file1.txt, file2.txt and so on.
     
  3. Test Cases will check for:
      1. File names provided in command line or not.
      This test case will pass only if you have provided a filenames prefixed with --file otherwise it will fail.
      2. File Format.
      This test case will only pass if the file format provided is of ".txt" type otherwise it will fail.
      3. Files Generated.
      This test case will only pass if the process is successful and encrypted files are generated otherwise it will fail.
          
          
  

