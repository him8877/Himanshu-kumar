import csv

def main():
    input_file = 'family_supertype_update_2.txt'  # input file name
    output_file = 'Family.csv'  # output file name 
    
    try:
        # Read data from the text file
        with open(input_file, 'r') as file:
            lines = file.readlines()
            
        # Process data, each line to strip whitespace, split by '=', and remove additional whitespace around each value
        Familydata = [
            [line.strip().split('=')[-1].strip()]for line in lines]    # Split by '=', last element strip whitespace
        
        # Write the Familydata to the CSV file
        with open(output_file, 'w', newline='') as csvfile:
            csv.writer(csvfile).writerows(Familydata)
            
        # Print a successful message
        print(f"Familydata has been Sucessful in {output_file}")

    except FileNotFoundError:
        # Handle the case where the input file does not exist
        print(f"The file {input_file} does not exist. Please check the file name and try again.")

if __name__ == "__main__":
    main()