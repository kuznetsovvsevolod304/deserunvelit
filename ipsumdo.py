import inquirer

file_name = inquirer.Text('file_name', message="Please enter the output Excel file name (without extension)").execute()
