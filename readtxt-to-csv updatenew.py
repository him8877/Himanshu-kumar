import csv

def main():
    input_file = 'update_family_number_1.txt'
    output_file = 'Family_update.csv'
    
    try:
        # Read data from the text file
        with open(input_file, 'r') as file:
            lines = file.readlines()
            
        # Process data, each line to strip whitespace, split by '=', ',' and remove additional whitespace around each value
        data = [
            [line.split('=')[1].split(',')[0].strip()]for line in lines]
        
        # Write the processed data to the CSV file
        with open(output_file, 'w', newline='') as csvfile:
            csv.writer(csvfile).writerows(data)
            
        # Print a successful message
        print(f"Familydata has been successfully written to {output_file}")

    except FileNotFoundError:
        # Handle the case where the input file does not exist
        print(f"The file {input_file} does not exist. Please check the file name and try again.")

if __name__ == "__main__":
    main()
