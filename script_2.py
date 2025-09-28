# Convert all data to JSON format for the web application
student_json = student_data.to_json(orient='records', force_ascii=False, indent=2)

# Save the complete data as JSON for the web application
with open('complete_student_data.json', 'w', encoding='utf-8') as f:
    f.write(student_json)

print(f"Complete dataset saved with {len(student_data)} student records")

# Show a sample of the JSON data
import json
with open('complete_student_data.json', 'r', encoding='utf-8') as f:
    sample_data = json.load(f)
    
print("\nFirst 3 JSON records:")
for i in range(3):
    print(f"Record {i+1}: {sample_data[i]}")

print("\nLast 3 JSON records:")
for i in range(-3, 0):
    print(f"Record {len(sample_data)+i+1}: {sample_data[i]}")

print(f"\nTotal JSON file size: {len(student_json)} characters")
print(f"Number of students in JSON: {len(sample_data)}")

# Verify all student codes are unique
unique_codes = len(set([record['student_code'] for record in sample_data]))
print(f"Unique student codes: {unique_codes}")
print(f"Total records: {len(sample_data)}")
print(f"All codes unique: {unique_codes == len(sample_data)}")