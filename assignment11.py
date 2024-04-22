
import traceback
class MyFile:
    def __init__(self, filename, permission):
        self.filename = filename
        self.permission = permission
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.permission)
            print(f"File {self.filename} opened with permission '{self.permission}'")
            return self.file
        except Exception as e:
            tb = e.__traceback__
            print("tb here",tb)
            traceback.print_tb(tb)
            print(f"Failed to open file: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
           
                self.file.close()
                print(f"File {self.filename} closed")
                print(exc_type,exc_value,traceback)
              
                # We return False to propagate any exceptions that occurred in the 'with' block
             

# Example usage of the MyFile class as a context manager
with MyFile("example.txt",'w') as file:
    file.write("Hello, world!")




b ={1:'2',3:'3'}
print(all(b))
print(hash("h"))
a= (1,2,3)
a= a*2
print(a)
z= {1,2,3,[1,2]}#it does not have a hash values (muttable)
