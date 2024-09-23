import csv
import os

# Define the folder containing athlete data
athlete_folder = "ExampleAthletes"
output_folder = "Output"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Read each athlete's CSV file and generate an HTML file
for filename in os.listdir(athlete_folder):
    if filename.endswith(".csv"):
        csv_file_path = os.path.join(athlete_folder, filename)

        with open(csv_file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

        # Extract athlete's name from the filename
        athlete_name = filename.split('.')[0]  # e.g., "Becca Van Lent"

        # Get athlete's performance data (skipping header)
        athlete_data = data[1:]

        # Create HTML content
        html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{athlete_name} Performance</title>
</head>
<body>
    <header>
        <h1>{athlete_name}</h1>
    </header>
    <section id="athlete-results">
        <h2>Performance Results</h2>
        <table id="athlete-table">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Meet</th>
                    <th>Time</th>
                    <th>Overall Place</th>
                    <th>Comments</th>
                    <th>Image</th>
                </tr>
            </thead>
            <tbody>
        '''

        # Add each performance record to the HTML table
        for row in athlete_data:
            if len(row) < 8:  # Check if the row has enough columns
                continue  # Skip empty or incomplete rows

            date = row[4] if len(row) > 4 else "N/A"
            meet = row[5] if len(row) > 5 else "N/A"
            time = row[3] if len(row) > 3 else "N/A"
            overall_place = row[1] if len(row) > 1 else "N/A"
            comments = row[6] if len(row) > 6 else "N/A"
            image = row[7] if len(row) > 7 else ""

            html_content += f'''
                <tr>
                    <td>{date}</td>
                    <td>{meet}</td>
                    <td>{time}</td>
                    <td>{overall_place}</td>
                    <td>{comments}</td>
                    <td><img src="athleteImages/{image}" alt="{athlete_name} at {meet}" width="100"></td>
                </tr>
            '''

        html_content += '''
            </tbody>
            </table>
        </section>
    </body>
</html>
        '''

        # Write the HTML content to a file
        output_file_path = os.path.join(output_folder, f"{athlete_name.replace(' ', '_').lower()}.html")
        with open(output_file_path, 'w') as output_file:
            output_file.write(html_content)

print("HTML files generated for each athlete.")

